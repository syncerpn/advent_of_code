# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day11_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
import numpy as np

universe = np.array([[i for i in d] for d in data])
universe = np.int32(universe == "#")

h, w = universe.shape
empty_rows = []
for hi in range(h):
    if np.sum(universe[hi, :]) == 0:
        empty_rows.append(hi)

new_universe = np.zeros((h + len(empty_rows), w), np.int32)
s = 0
i = 0
for i, r in enumerate(empty_rows):
    new_universe[s+i:r+i,:] = universe[s:r,:]
    s = r

new_universe[s+i+1:,:] = universe[s:,:]

universe = new_universe

h, w = universe.shape
empty_cols = []
for wi in range(w):
    if np.sum(universe[:, wi]) == 0:
        empty_cols.append(wi)

new_universe = np.zeros((h, w + len(empty_cols)), np.int32)
s = 0
i = 0
for i, c in enumerate(empty_cols):
    new_universe[:,s+i:c+i] = universe[:,s:c]
    s = c
new_universe[:,s+i+1:] = universe[:,s:]
    
universe = new_universe

ys, xs = np.where(universe)

distance = 0

for y, x in zip(ys, xs):
    distance += np.sum(abs(y - ys) + abs(x - xs))

distance /= 2
print(distance)

#part2
import numpy as np

EXPAND = 1000000

universe = np.array([[i for i in d] for d in data])
universe = np.int32(universe == "#")

empty_rows = np.where(np.sum(universe, axis=1) == 0)[0]
empty_cols = np.where(np.sum(universe, axis=0) == 0)[0]

ys, xs = np.where(universe)

ys = np.array([y + (EXPAND - 1) * (y > empty_rows).sum() for y in ys])
xs = np.array([x + (EXPAND - 1) * (x > empty_cols).sum() for x in xs])

distance = 0

for y, x in zip(ys, xs):
    distance += np.sum(abs(y - ys) + abs(x - xs))

distance /= 2
print(distance)