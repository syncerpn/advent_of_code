# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day13_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
def reflect_point(pattern):
    for i in range(len(pattern)):
        p1 = pattern[i::-1]
        p2 = pattern[i+1:]
        l = min(len(p1), len(p2))
        if l:
            if p1[0:l] == p2[0:l]:
                return len(p1)
    
    return 0

def transpose(pattern):
    tpattern = ["".join([pattern[hi][wi] for hi in range(len(pattern))]) for wi in range(len(pattern[0]))]
    return tpattern

patterns = []
pattern = []
for d in data:
    if d:
        pattern.append(d)
    else:
        patterns.append(pattern)
        pattern = []
patterns.append(pattern)

score = 0

for pattern in patterns:
    r = reflect_point(pattern)
    
    tpattern = transpose(pattern)
    
    c = reflect_point(tpattern)
    
    score += c + r * 100

print(score)

#part2
import numpy as np
def reflect_point_fixed(pattern):
    for i in range(len(pattern)):
        p1 = pattern[i::-1]
        p2 = pattern[i+1:]
        l = min(len(p1), len(p2))
        if l:
            diff_map = np.array([[c for c in p] for p in p1[0:l]]) != np.array([[c for c in p] for p in p2[0:l]])
            if np.int32(diff_map).sum() == 1:
                return len(p1)
    return 0

def transpose(pattern):
    tpattern = ["".join([pattern[hi][wi] for hi in range(len(pattern))]) for wi in range(len(pattern[0]))]
    return tpattern

patterns = []
pattern = []
for d in data:
    if d:
        pattern.append(d)
    else:
        patterns.append(pattern)
        pattern = []
patterns.append(pattern)

score = 0

for pattern in patterns:
    r = reflect_point_fixed(pattern)
        
    tpattern = transpose(pattern)
    
    c = reflect_point_fixed(tpattern)
    score += c + r * 100

print(score)