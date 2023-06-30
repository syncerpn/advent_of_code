# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:47:54 2022

@author: Nghia
"""

def revert(n):
    s = ''
    while n != 0:
        r = n % 5
        if r > 2:
            r -= 5
        if r == -1:
            s = '-' + s
        elif r == -2:
            s = '=' + s
        else:
            s = str(r) + s
        n = n - r
        n //= 5
    
    return s

def convert(s):
    n = 0
    for c in s:
        n *= 5
        if c == '-':
            n += -1
        elif c == '=':
            n += -2
        else:
            n += int(c)
    
    return n

with open('day25_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
ss = 0

for d in data:
    print(d, convert(d))
    ss += convert(d)

print(revert(ss))

#part2