# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day1_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
l = []
r = []
sum_d = 0

for d in data:
    li, ri = list(map(int, d.split("  ")))
    l.append(li)
    r.append(ri)

l.sort()
r.sort()

for a, b in zip(l, r):
    sum_d += abs(a - b)

print(sum_d)

#part2
counter = {}
for a in r:
    if a not in counter:
        counter[a] = 0
    counter[a] += 1

sum_s = 0
for b in l:
    if b not in counter:
        continue
    sum_s += b * counter[b]

print(sum_s)