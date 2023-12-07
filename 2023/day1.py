# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day1_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
digits = list(map(str, list(range(10))))
sum_v = 0

for d in data:
    for a in d:
        if a in digits:
            break
    for b in d[::-1]:
        if b in digits:
            break
    sum_v += int(a+b)

print(sum_v)

#part2
digits = list(map(str, list(range(10))))
names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum_v = 0

m = None
k = None

for d in data:
    m = None
    p = ""
    for a in d:
        if a in digits:
            m = a
        p += a
        for n in names:
            if n in p:
                m = str(names.index(n) + 1)
                break
        if m is not None:
            break
            
    k = None
    p = ""
    for b in d[::-1]:
        if b in digits:
            k = b
        p = b + p
        for n in names:
            if n in p:
                k = str(names.index(n) + 1)
                break
        if k is not None:
            break
    
    sum_v += int(m+k)

print(sum_v)