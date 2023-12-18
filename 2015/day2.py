# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day2_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
score = 0
for d in data:
    a, b, c = list(map(int, d.split("x")))
    score += 2* (a*b + b*c + c*a) + min(min(a*b, b*c), c*a)

print(score)

#part2
score = 0
for d in data:
    a, b, c = list(map(int, d.split("x")))
    score += 2* (a+b+c - max(max(a,b),c)) + a*b*c

print(score)