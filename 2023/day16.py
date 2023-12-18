# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day16_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
import numpy as np
light_map = np.array([[c for c in d] for d in data])

h, w = light_map.shape

locs = np.zeros(light_map.shape)
locs[0, 0] = 1

srcs_dirs = [(0, 0, 0, 1)]
visited_locs = [(0, 0, 0, 1)]

if light_map[0, 0] == "\\":
    srcs_dirs = [(0, 0, 1, 0)]
elif light_map[0, 0] == "/":
    srcs_dirs = [(0, 0, -1, 0)]
elif light_map[0, 0] == "-":
    srcs_dirs = [(0, 0, 0, 1)]
elif light_map[0, 0] == "|":
    srcs_dirs = [(0, 0, 1, 0)]

for s_d in srcs_dirs:
    if s_d not in visited_locs:
        visited_locs += [s_d]

while len(srcs_dirs) > 0:
    s_d_news = []
    for i, s_d in enumerate(srcs_dirs):
        visited_locs.append(s_d)
        
        y, x, dy, dx = s_d
        
        yn = y + dy
        xn = x + dx
        
        if yn < 0 or yn > h - 1 or xn < 0 or xn > w - 1:
            continue
        
        locs[yn, xn] = 1
        
        if light_map[yn, xn] == "\\":
            s_d_news += [(yn, xn, dx, dy)]
        elif light_map[yn, xn] == "/":
            s_d_news += [(yn, xn, -dx, -dy)]
        elif light_map[yn, xn] == "-" and dy:
            s_d_news += [(yn, xn, 0, -1), (yn, xn, 0, 1)]
        elif light_map[yn, xn] == "|" and dx:
            s_d_news += [(yn, xn, -1, 0), (yn, xn, 1, 0)]
        else:
            s_d_news += [(yn, xn, dy, dx)]
    
    srcs_dirs = []
    for s_d in s_d_news:
        if s_d in visited_locs:
            continue
        srcs_dirs += [s_d]

print(np.sum(locs))

#part2
import numpy as np
light_map = np.array([[c for c in d] for d in data])

h, w = light_map.shape
max_loc = 0

starting_srcs_dirs  = [(0, i, 1, 0) for i in range(w)]
starting_srcs_dirs += [(h-1, i, -1, 0) for i in range(w)]
starting_srcs_dirs += [(i, 0, 0, 1) for i in range(h)]
starting_srcs_dirs += [(i, w-1, 0, -1) for i in range(h)]

for starting_s_d in starting_srcs_dirs:
    print(starting_s_d)
    ys, xs, dys, dxs = starting_s_d

    locs = np.zeros(light_map.shape)
    locs[ys, xs] = 1
    
    srcs_dirs = [starting_s_d]
    visited_locs = [starting_s_d]
    
    if light_map[ys, xs] == "\\":
        srcs_dirs = [(ys, xs, dxs, dys)]
    elif light_map[ys, xs] == "/":
        srcs_dirs = [(ys, xs, -dxs, -dys)]
    elif light_map[ys, xs] == "-" and dy:
        srcs_dirs = [(ys, xs, 0, -1), (ys, xs, 0, 1)]
    elif light_map[ys, xs] == "|" and dx:
        srcs_dirs = [(ys, xs, -1, 0), (ys, xs, 1, 0)]
    
    for s_d in srcs_dirs:
        if s_d not in visited_locs:
            visited_locs += [s_d]
    
    while len(srcs_dirs) > 0:
        s_d_news = []
        for i, s_d in enumerate(srcs_dirs):
            visited_locs.append(s_d)
            
            y, x, dy, dx = s_d
            
            yn = y + dy
            xn = x + dx
            
            if yn < 0 or yn > h - 1 or xn < 0 or xn > w - 1:
                continue
            
            locs[yn, xn] = 1
            
            if light_map[yn, xn] == "\\":
                s_d_news += [(yn, xn, dx, dy)]
            elif light_map[yn, xn] == "/":
                s_d_news += [(yn, xn, -dx, -dy)]
            elif light_map[yn, xn] == "-" and dy:
                s_d_news += [(yn, xn, 0, -1), (yn, xn, 0, 1)]
            elif light_map[yn, xn] == "|" and dx:
                s_d_news += [(yn, xn, -1, 0), (yn, xn, 1, 0)]
            else:
                s_d_news += [(yn, xn, dy, dx)]
        
        srcs_dirs = []
        for s_d in s_d_news:
            if s_d in visited_locs:
                continue
            srcs_dirs += [s_d]
    
    max_loc = max(max_loc, np.sum(locs))

print(max_loc)