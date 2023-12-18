# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day18_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
def tsub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def tadd(a, b):
    return (a[0] + b[0], a[1] + b[1])

def tmul(a, b):
    return (a[0] * b[0], a[1] * b[1])

def get_points_in_edges(edges):
    loc, span_a, span_b = edges
    
    h, w = tadd(span_a, span_b)
    y, x = min(loc[0], loc[0]+h), min(loc[1], loc[1]+w)
    h, w = abs(h), abs(w)
    
    points = [(yi, xi) for xi in range(x, x+w+1) for yi in range(y, y+h+1)]
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
            
inout_map = {"UR": "W", "RD": "W", "DL": "W", "LU": "W",
             "RU": "C", "DR": "C", "LD": "C", "UL": "C",}

dir_s = "UDLR"
directions = [(-1,0), (1,0), (0,-1), (0,1)]

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

for d in data + [data[0]]:
    di, n, color = d.split(" ")
    n = int(n)
    color = color[1:-1]

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
        point = get_points_in_edges(edges)
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

upy, upx = np.where(winding_map == "")
while len(upy):
    undecided = []
    for i in range(len(upy)):
        y, x = upy[i], upx[i]
        neighbor((y, x), winding_map)
    
    upy, upx = np.where(winding_map == "")

count = winding_map == "E"
count += winding_map == "W" if winding_counter > 0 else winding_map == "C"
print(np.sum(count))

import matplotlib.pyplot as plt
img_map = np.zeros((h, w), dtype=np.uint8)
img_map[winding_map == "W"] = 255
img_map[winding_map == "E"] = 128
plt.imshow(img_map)