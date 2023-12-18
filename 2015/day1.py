# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day1_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
d = data[0]
f = d.count("(") - d.count(")")

print(f)

#part2
d = data[0]
f = 0
for i, c in enumerate(d):
    if c == "(":
        f += 1
    elif c == ")":
        f -= 1
    if f == -1:
        break

print(i+1)