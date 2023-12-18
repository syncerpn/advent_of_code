# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day5_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
score = 0
for d in data:
    vowels = sum([d.count(c) for c in "aeiou"])
    if vowels < 3:
        continue
    
    forbidwords = sum([1 if c in d else 0 for c in ["ab", "cd", "pq", "xy"]])
    if forbidwords > 0:
        continue
    
    for i in range(len(d)-1):
        if d[i] == d[i+1]:
            score += 1
            break

print(score)

#part2
score = 0
for d in data:
    cond1 = False
    cond2 = False
    
    for i in range(len(d)-3):
        ref = d[i:i+2]
        if ref in d[i+2:]:
            cond1 = True
            break
    
    for i in range(len(d)-2):
        if d[i] == d[i+2]:
            cond2 = True
            break

    if cond1 and cond2:
        score += 1
        
print(score)
