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
        
        return u, d, l, r
    
    def _guess_stloc(self):
        hl, wl = self.stloc
        self.pipes[hl][wl].u, self.pipes[hl][wl].d, self.pipes[hl][wl].l, self.pipes[hl][wl].r = self.check_around(self.stloc)
    
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

pipe_network = PipeNetwork(data)
dist_map, max_dist = pipe_network.scanning(pipe_network.stloc)
print(max_dist)


#part2
wall = [[0 for i in d] for d in dist_map]
for di, d in enumerate((dist_map)):
    for i, c in enumerate(d):
        if c is not None:
            wall[di][i] = 1
