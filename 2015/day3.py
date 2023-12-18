# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day3_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
d = data[0]
x = 0
y = 0
house = {"0.0": 1}
for c in d:
    if c == ">":
        x += 1
    elif c == "<":
        x -= 1
    elif c == "^":
        y -= 1
    elif c == "v":
        y += 1
    
    k = ".".join([str(x), str(y)])
    if k not in house:
        house[k] = 0
    house[k] += 1

print(len(house))

#part2
d = data[0]
x = 0
y = 0
a = 0
b = 0
house = {"0.0": 2}
for i,c in enumerate(d):
    if i % 2:
        if c == ">":
            x += 1
        elif c == "<":
            x -= 1
        elif c == "^":
            y -= 1
        elif c == "v":
            y += 1
            
        k = ".".join([str(x), str(y)])
        if k not in house:
            house[k] = 0
        house[k] += 1
            
    else:
        if c == ">":
            a += 1
        elif c == "<":
            a -= 1
        elif c == "^":
            b -= 1
        elif c == "v":
            b += 1
    
        k = ".".join([str(a), str(b)])
        if k not in house:
            house[k] = 0
        house[k] += 1

print(len(house))