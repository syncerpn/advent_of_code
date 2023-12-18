# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day17_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
import numpy as np

heatmap = np.array([[int(c) for c in d] for d in data])
distmap = np.empty(heatmap.shape, dtype=tuple)

h, w = heatmap.shape

start_loc = (0, 0)

distmap[start_loc] = (0, 0, 0)

next_locs = [(0, 0, 0, 1), (0, 0, 1, 0)]
while next_locs:
    new_locs = []
    for loc in next_locs:
        y, x, cy, cx = loc
        
        dy, dx = 0, 0
        if cy > 0:    
            dy = 1
        elif cy < 0:
            dy = -1
        
        if cx > 0:    
            dx = 1
        elif cx < 0:
            dx = -1
            
        yn = y + dy
        xn = x + dx
        
        if yn > h-1 or yn < 0 or xn > w-1 or xn < 0:
            continue
        
        dist = distmap[y, x][0] + heatmap[yn, xn]
        if distmap[yn, xn] is not None:
            dist_before, cy_before, cx_before = distmap[yn, xn]
            if dist >= dist_before:
                continue

        distmap[yn, xn] = (dist, cy, cx)

        if cy:
            new_locs += [(yn, xn, 0, 1), (yn, xn, 0, -1)]
            if 0 < cy < 3:
                new_locs += [(yn, xn, cy+1, 0)]
            elif 0 > cy > -3:
                new_locs += [(yn, xn, cy-1, 0)]
                
        elif cx:
            new_locs += [(yn, xn, 1, 0), (yn, xn, -1, 0)]
            if cx > 0 and cx < 3:
                new_locs += [(yn, xn, 0, cx+1)]
            elif cx < 0 and cx > -3:
                new_locs += [(yn, xn, 0, cx-1)]
        
    next_locs = new_locs