# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day10_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1

UP = "L|J"
DOWN = "F|7"
LEFT = "7-J"
RIGHT = "F-L"
STARTING_MARK = "S"

class Pipe:
    def __init__(self, c):
        self.u = False
        self.d = False
        self.l = False
        self.r = False
        self.s = False
        
        if c in UP:
            self.u = True
        if c in DOWN:
            self.d = True
        if c in LEFT:
            self.l = True
        if c in RIGHT:
            self.r = True
        if c in STARTING_MARK:
            self.s = True

class PipeNetwork:
    def __init__(self, data):
        self.pipes = []
        self.stloc = None
        self.h = len(data)
        self.w = len(data[0])
        
        for di, d in enumerate(data):
            line = []
            for ci, c in enumerate(d):
                p = Pipe(c)
                line.append(p)
                if p.s:
                    self.stloc = (di, ci)
            
            self.pipes.append(line)
        
        self._guess_stloc()
        
    def check_around(self, loc):
        hl, wl = loc
        su = self.pipes[hl][wl].u
        sd = self.pipes[hl][wl].d
        sl = self.pipes[hl][wl].l
        sr = self.pipes[hl][wl].r
        
        u = False
        d = False
        l = False
        r = False
        
        if su and hl > 0:
            u = self.pipes[hl-1][wl].d
    
        if sd and hl < self.h-1:
            d = self.pipes[hl+1][wl].u
                
        if sl and wl > 0:
            l = self.pipes[hl][wl-1].r
    
        if sr and wl < self.w-1:
            r = self.pipes[hl][wl+1].l
        
        return u, d, l, r
    
    def _guess_stloc(self):
        hl, wl = self.stloc
        
        u = False
        d = False
        l = False
        r = False
        
        if hl > 0:
            u = self.pipes[hl-1][wl].d
    
        if hl < self.h-1:
            d = self.pipes[hl+1][wl].u
                
        if wl > 0:
            l = self.pipes[hl][wl-1].r
    
        if wl < self.w-1:
            r = self.pipes[hl][wl+1].l
        
        self.pipes[hl][wl].u, self.pipes[hl][wl].d, self.pipes[hl][wl].l, self.pipes[hl][wl].r = u, d, l, r
    
    def travel_next(self, loc):
        u, d, l, r = self.check_around(loc)
        hl, wl = loc
        
        locs_end = []
        if u:
            locs_end.append((hl-1, wl))
        if d:
            locs_end.append((hl+1, wl))
        if l:
            locs_end.append((hl, wl-1))
        if r:
            locs_end.append((hl, wl+1))
        
        return locs_end
    
    def travel_next_one_direction(self, loc, visited_locs):
        u, d, l, r = self.check_around(loc)
        
        hl, wl = loc
        if u and (hl-1, wl) not in visited_locs:
            return -1, 0, (hl-1, wl), "UU" #return "UU" instead of "U" for expanding and floodfill to deal with some edge cases
        if d and (hl+1, wl) not in visited_locs:
            return 1, 0, (hl+1, wl), "DD"
        if l and (hl, wl-1) not in visited_locs:
            return 0, -1, (hl, wl-1), "LL"
        if r and (hl, wl+1) not in visited_locs:
            return 0, 1, (hl, wl+1), "RR"
        return None
    
    def travel_to(self, loc, next_loc):
        hi, wi = loc
        u, d, l, r = self.pipes[hi][wi].u, self.pipes[hi][wi].d, self.pipes[hi][wi].l, self.pipes[hi][wi].r
        nhi, nwi = next_loc
        nu, nd, nl, nr = self.pipes[nhi][nwi].u, self.pipes[nhi][nwi].d, self.pipes[nhi][nwi].l, self.pipes[nhi][nwi].r
        if u and nd and nhi == hi-1:
            return -1, 0, "UU" #return "UU" instead of "U" for expanding and floodfill to deal with some edge cases
        if d and nu and nhi == hi+1:
            return 1, 0, "DD"
        if l and nr and nwi == wi-1:
            return 0, -1, "LL"
        if r and nl and nwi == wi+1:
            return 0, 1, "RR"
        return 0, 0, ""
    
    def scanning(self, stloc):
        dist_map = [[None for _ in range(self.w)] for _ in range(self.h)]
        hl, wl = stloc
        dist_map[hl][wl] = 0
        
        loc = stloc
        
        visited_locs = [stloc]
        base_dists = []
        next_locs = []
        
        new_locs = [l for l in self.travel_next(loc) if l not in visited_locs]
        base_dists += [0 for _ in range(len(new_locs))]
        next_locs += new_locs
        
        max_dist = 0
        
        while len(next_locs) > 0:
            loc = next_locs[0]
            base_dist = base_dists[0]
            
            next_locs = next_locs[1:]
            base_dists = base_dists[1:]
            
            if loc in visited_locs:
                continue
            
            hl, wl = loc
            if dist_map[hl][wl] is None:
                dist_map[hl][wl] = base_dist + 1
                max_dist = max(max_dist, dist_map[hl][wl])
            
            visited_locs.append(loc)
            
            new_locs = [l for l in self.travel_next(loc) if l not in visited_locs]
            base_dists += [dist_map[hl][wl] for _ in range(len(new_locs))]    
            next_locs += new_locs
        
        
        return dist_map, max_dist
    
    def scanning_one_direction(self, stloc):
        visited_locs = []
        
        loc = stloc
        
        moving_seq = ""
        
        next_loc = self.travel_next_one_direction(loc, visited_locs)
        
        # pv, ph = 0, 0
        while next_loc is not None:
            # hi, wi = loc
            visited_locs.append(loc)
            _, _, loc, di = next_loc
            moving_seq += di
            next_loc = self.travel_next_one_direction(loc, visited_locs)
        
        _, _, di = self.travel_to(loc, stloc)
        moving_seq += di
        
        return moving_seq
        

pipe_network = PipeNetwork(data)
dist_map, max_dist = pipe_network.scanning(pipe_network.stloc)
print(max_dist)

#part2

def tsub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def tadd(a, b):
    return (a[0] + b[0], a[1] + b[1])

def tmul(a, b):
    return (a[0] * b[0], a[1] * b[1])

def tuple_range(ta, tb):
    min_y = min(ta[0], tb[0])
    max_y = max(ta[0], tb[0])
    min_x = min(ta[1], tb[1])
    max_x = max(ta[1], tb[1])
    
    return [(yi, xi) for yi in range(min_y, max_y+1) for xi in range(min_x, max_x+1)]

def get_points_in_edges(edges, dip, di):
    loc, span_a, span_b = edges
    
    offs_a = tmul(directions[dir_s.index(dip)], (-1,-1))
    offs_b = directions[dir_s.index(di)]
    
    
    point_a = [tadd(t, offs_b) for t in tuple_range(loc, tadd(loc, span_a))]
    loc = tadd(loc, span_a)
    point_b = [tadd(t, offs_a) for t in tuple_range(loc, tadd(loc, span_b))]
    
    points = list(set(point_a+point_b))
    return points

def neighbor(point, neighbor_map):
    y, x = point
    h, w = neighbor_map.shape
    if y - 1 >= 0:
        if neighbor_map[y-1, x] != "E" and neighbor_map[y-1, x] != "":
            neighbor_map[y, x] = neighbor_map[y-1, x]
            return True
    if y + 1 <  h:
        if neighbor_map[y+1, x] != "E" and neighbor_map[y+1, x] != "":
            neighbor_map[y, x] = neighbor_map[y+1, x]
            return True
    if x - 1 >= 0:
        if neighbor_map[y, x-1] != "E" and neighbor_map[y, x-1] != "":
            neighbor_map[y, x] = neighbor_map[y, x-1]
            return True
    if x + 1 < w:
        if neighbor_map[y, x+1] != "E" and neighbor_map[y, x+1] != "":
            neighbor_map[y, x] = neighbor_map[y, x+1]
            return True
    
    return False
      
moving_seq = pipe_network.scanning_one_direction(pipe_network.stloc)

while (moving_seq[0] == moving_seq[-1]):
    moving_seq = moving_seq[1:] + moving_seq[0]

mdata = []
di = None
dc = 0
for msi in moving_seq:
    if di is None:
        di = msi
        dc = 1
    else:
        if di == msi:
            dc += 1
        if di != msi:
            mdata.append((di, dc))
            di = msi
            
            dc = 1
mdata.append((di, dc))
    
inout_map = {"UR": "W", "RD": "W", "DL": "W", "LU": "W",
             "RU": "C", "DR": "C", "LD": "C", "UL": "C",}

dir_s = "RDLU"
directions = [(0,1), (1,0), (0,-1), (-1,0)]

winding = ""
winding_counter = 0

min_y, max_y, min_x, max_x = 0, 0, 0, 0
hi, wi = 0, 0

shape_dict = {
    "edge": [],
    "point": {},
    }
di_prev = None

loc = (0,0)

edges = [(0,0)]

for d in mdata + [mdata[0]]:
    di, n = d

    winding += di
    if di == "R":
        shape_dict["edge"] += [(loc[0], loc[1] + i) for i in range(1, n+1)]
        wi += n
        edges.append((0,n))
    elif di == "L":
        shape_dict["edge"] += [(loc[0], loc[1] - i) for i in range(1, n+1)]
        wi -= n
        edges.append((0,-n))
    elif di == "U":
        shape_dict["edge"] += [(loc[0] - i, loc[1]) for i in range(1, n+1)]
        hi -= n
        edges.append((-n,0))
    elif di == "D":
        shape_dict["edge"] += [(loc[0] + i, loc[1]) for i in range(1, n+1)]
        hi += n
        edges.append((n,0))
    
    loc = tadd(loc, tmul((n,n), directions[dir_s.index(di)]))
    
    if di_prev is not None:
        g = inout_map[di_prev + di]
        if g == "W":
            winding_counter += 1
        else:
            winding_counter -= 1
        point = get_points_in_edges(edges, di_prev, di)
        for p in point:
            shape_dict["point"][p] = g
        
        el, span_a, span_b = edges
        edges = [tadd(el, span_a), span_b]
    
    di_prev = di
    
    min_y = min(min_y, hi)
    max_y = max(max_y, hi)
    min_x = min(min_x, wi)
    max_x = max(max_x, wi)
    
offset = (min_y, min_x)

w = max_x - min_x + 1
h = max_y - min_y + 1

import numpy as np
winding_map = np.array([["" for _ in range(w)] for _ in range(h)])

for p in shape_dict["point"]:
    winding_map[tsub(p, offset)] = shape_dict["point"][p]

for p in shape_dict["edge"]:
    winding_map[tsub(p, offset)] = "E"

if winding_counter > 0:
    print("clockwise is in")
else:
    print("counter-clockwise is in")

import matplotlib.pyplot as plt
img = np.zeros(winding_map.shape, dtype=np.uint8)
img[winding_map == "E"] = 255
img[winding_map == "W"] = 160
img[winding_map == "C"] = 64
plt.imshow(img)

upy, upx = np.where(winding_map == "")
lp = len(upy)
lpp = 0
while len(upy) and lp != lpp:
    undecided = []
    for i in range(len(upy)):
        y, x = upy[i], upx[i]
        neighbor((y, x), winding_map)
    
    lpp = lp
    upy, upx = np.where(winding_map == "")
    lp = len(upy)

# count = winding_map == "W" if winding_counter > 0 else winding_map == "C"
#IMPORTANT: before we "expand" it for floodfill, now we collapse it with only some tiles
count = winding_map[0::2,0::2] == "W" if winding_counter > 0 else winding_map[0::2,0::2] == "C"
print(np.sum(count))

#part2: REDDIT SOLUTION:
# https://adventofcode.com/2023/day/10#part2

with open('day10_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

field = []
for y, line in enumerate(data):
    field.append(line)
    s_location = line.find('S')
    if s_location >= 0:
        x1, y1 = s_location, y
field_marked = [[False for i in range(len(field[0]))] for j in range(len(field))]
if y1 > 0 and field[y1 - 1][x1] in {'7', 'F', '|'}:
    if x1 > 0 and field[y1][x1 - 1] in {'F', 'L', '-'}:
        direction = 0
        start_pipe = 'J'
    elif x1 < len(field[0]) - 1 and field[y1][x1 + 1] in {'J', '7', '-'}:
        direction = 0
        start_pipe = 'L'
if y1 < len(field) - 1 and field[y1 + 1][x1] in {'J', 'L', '|'}:
    if x1 > 0 and field[y1][x1 - 1] in {'F', 'L', '-'}:
        direction = 2
        start_pipe = '7'
    elif x1 < len(field[0]) - 1 and field[y1][x1 + 1] in {'J', '7', '-'}:
        direction = 2
        start_pipe = 'F'
if 0 < x1 < len(field[0]) - 1 and field[y1][x1 - 1] in {'F', 'L', '-'} and field[y1][x1 + 1] in {'7', 'J', '-'}:
    direction = 1
    start_pipe = '-'
if 0 < y1 < len(field) - 1 and field[y1 - 1][x1] in {'F', '7', '|'} and field[y1 + 1][x1] in {'L', 'J', '|'}:
    direction = 0
    start_pipe = '|'
field[y1] = field[y1][:x1] + start_pipe + field[y1][x1 + 1:]
x, y = x1, y1
while True:
    match direction:
        case 0:
            y -= 1
        case 1:
            x += 1
        case 2:
            y += 1
        case 3:
            x -= 1
    match field[y][x]:
        case 'L':
            direction = 1 if direction == 2 else 0
        case 'J':
            direction = 3 if direction == 2 else 0
        case '7':
            direction = 2 if direction == 1 else 3
        case 'F':
            direction = 2 if direction == 3 else 1
    field_marked[y][x] = True
    if x1 == x and y1 == y:
        break
total = 0
for y, line in enumerate(field):
    for x, char in enumerate(line):
        if not field_marked[y][x]:
            n = 0
            for y1 in range(y + 1, len(field)):
                if field_marked[y1][x]:
                    if field[y1][x] == '-':
                        n += 1
                    elif field[y1][x] == '7' or field[y1][x] == 'F':
                        prev = field[y1][x]
                    elif (field[y1][x] == 'J' and prev == 'F') or (field[y1][x] == 'L' and prev == '7'):
                        n += 1
            if n % 2 == 1:
                total += 1
print(total)