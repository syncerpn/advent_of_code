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
            return -1, 0, (hl-1, wl)
        if d and (hl+1, wl) not in visited_locs:
            return 1, 0, (hl+1, wl)
        if l and (hl, wl-1) not in visited_locs:
            return 0, -1, (hl, wl-1)
        if r and (hl, wl+1) not in visited_locs:
            return 0, 1, (hl, wl+1)
        return None
    
    def travel_to(self, loc, next_loc):
        hi, wi = loc
        u, d, l, r = self.pipes[hi][wi].u, self.pipes[hi][wi].d, self.pipes[hi][wi].l, self.pipes[hi][wi].r
        nhi, nwi = next_loc
        nu, nd, nl, nr = self.pipes[nhi][nwi].u, self.pipes[nhi][nwi].d, self.pipes[nhi][nwi].l, self.pipes[nhi][nwi].r
        if u and nd and nhi == hi-1:
            return -1, 0
        if d and nu and nhi == hi+1:
            return 1, 0
        if l and nr and nwi == wi-1:
            return 0, -1
        if r and nl and nwi == wi+1:
            return 0, 1
        return 0, 0
    
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
        vert_map = [[0 for _ in range(self.w)] for _ in range(self.h)]
        horz_map = [[0 for _ in range(self.w)] for _ in range(self.h)]
        
        visited_locs = []
        
        loc = stloc
        
        next_loc = self.travel_next_one_direction(loc, visited_locs)
        pv, ph = 0, 0
        while next_loc is not None:
            hi, wi = loc
            visited_locs.append(loc)
            v, h, loc = next_loc
            if v:    
                vert_map[hi][wi] = v
                if ph:
                    horz_map[hi][wi] = ph
            elif h:
                horz_map[hi][wi] = h
                if pv:
                    vert_map[hi][wi] = pv
            pv, ph = v, h
            next_loc = self.travel_next_one_direction(loc, visited_locs)
        
        v, h = self.travel_to(loc, stloc)
        hi, wi = loc
        if v:    
            vert_map[hi][wi] = v
            if ph:
                horz_map[hi][wi] = ph
        elif h:
            horz_map[hi][wi] = h
            if pv:
                vert_map[hi][wi] = pv
        
        pv, ph = v, h
        hi, wi = stloc
        if vert_map[hi][wi]:    
            if ph:
                horz_map[hi][wi] = ph
        elif horz_map[hi][wi]:
            if pv:
                vert_map[hi][wi] = pv
        
        return vert_map, horz_map
        

pipe_network = PipeNetwork(data)
dist_map, max_dist = pipe_network.scanning(pipe_network.stloc)
print(max_dist)


#part2
vert_map, horz_map = pipe_network.scanning_one_direction(pipe_network.stloc)
import numpy as np
vert_map, horz_map = np.array(vert_map), np.array(horz_map)
