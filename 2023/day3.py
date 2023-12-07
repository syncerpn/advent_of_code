# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day3_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]
#part1
sum_pn = 0

import numpy as np

data_np = np.array([[c for c in d] for d in data])

def is_symbol_adjacent(y, x, l, ref_mat):
    if l <= 0:
        return False
    h, w = ref_mat.shape
    coord = []
    for yi in range(max(y-1,0), min(y+2,h)):
        for xi in range(max(x-1,0), min(x+l+1,w)):
            if (yi == y) and (xi >= x) and (xi < x+l):
                continue
            coord.append([yi, xi])
    
    for c in coord:
        y, x = c
        if ref_mat[y, x] != ".":
            return True
    
    return False

h, w = data_np.shape
hi = 0
wi = 0
l = 0
digits = list(map(str, list(range(10))))

while hi < h:
    if data_np[hi, wi] in digits:
        l += 1
    else:
        if is_symbol_adjacent(hi, wi-l, l, data_np):
            num = int("".join(data[hi][wi-l:wi]))
            sum_pn += num
        l = 0
    
    wi += 1
    
    if wi >= w:
        if is_symbol_adjacent(hi, wi-l, l, data_np):
            num = int("".join(data[hi][wi-l:wi]))
            sum_pn += num
        l = 0
        
        hi += 1
        wi = 0
        
print(sum_pn)
#part2
sum_pn = 0

import numpy as np

data_np = np.array([[c for c in d] for d in data])
gear_mat = np.zeros(data_np.shape) + 1
gear_count = np.zeros(data_np.shape)

def check_gear_adjacent(y, x, l, ref_mat, gear_mat, gear_count):
    if l <= 0:
        return False
    
    num = int("".join(ref_mat[y][x:x+l]))
    h, w = ref_mat.shape
    coord = []
    for yi in range(max(y-1,0), min(y+2,h)):
        for xi in range(max(x-1,0), min(x+l+1,w)):
            if (yi == y) and (xi >= x) and (xi < x+l):
                continue
            coord.append([yi, xi])
    
    for c in coord:
        y, x = c
        if ref_mat[y, x] == "*":
            gear_mat[y, x] *= num
            gear_count[y, x] += 1

h, w = data_np.shape
hi = 0
wi = 0
l = 0
digits = list(map(str, list(range(10))))

while hi < h:
    if data_np[hi, wi] in digits:
        l += 1
    else:
        check_gear_adjacent(hi, wi-l, l, data_np, gear_mat, gear_count)
        l = 0
    
    wi += 1
    
    if wi >= w:
        check_gear_adjacent(hi, wi-l, l, data_np, gear_mat, gear_count)
        l = 0
        hi += 1
        wi = 0

sum_pn = np.sum(np.float32(gear_count == 2) * gear_mat)
print(sum_pn)