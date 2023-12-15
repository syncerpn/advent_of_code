# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:33:19 2022

@author: NghiaServer
"""

with open('day3_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

rule = {c:i for i,c in enumerate(' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') if c != ' '}

#part1
score = 0

for d in data:
    n = len(d)
    a = d[:n//2]
    b = d[n//2:]
    for c in a:
        if c in b:
            break
    
    score += rule[c]
    
print(score)

#part2
score = 0
group = []
C = ''
for d in data:
    if len(group) < 3:
        if not group:
            group += [d]
        elif len(d) <= len(group[0]): #must include "="
            group = [d] + group
        elif len(d) >= len(group[-1]): #also must include "="
            group = group + [d]
        else:
            group = [group[0]] + [d] + [group[-1]]
                
    if len(group) == 3:
        # print(group)
        gmin = group[0]
        for c in gmin:
            if (c in group[1]) and (c in group[2]):
                C += c
                score += rule[c]
                break
            
        group = []

print(score)