# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:47:54 2022

@author: Nghia
"""

with open('day6_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
sum_i = 0

for d in data:
    w = d[:4]
    i = 4
    if len(set(w)) != 4:
        for c in d[4:]:
            i += 1
            w = w[1:] + c
            if len(set(w)) == 4:
                break
    
    sum_i += i

print(sum_i)
    
#part2
sum_i = 0

for d in data:
    w = d[:14]
    i = 14
    if len(set(w)) != 14:
        for c in d[14:]:
            i += 1
            w = w[1:] + c
            if len(set(w)) == 14:
                break
    
    sum_i += i

print(sum_i)