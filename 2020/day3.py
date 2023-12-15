# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 16:07:22 2021

@author: Nghia
"""

### def


### main
with open('day3_input') as f:
    data = f.readlines()

data = [line.strip('\n') for line in data]

## part 1
l = len(data[0])
n = len(data)
x = 0
y = 0
count = 0

while y < n:
    if data[y][x] == '#':
        count += 1
    y += 1
    x += 3
    x = x % l
print(count)
## part 2
l = len(data[0])
n = len(data)

mul = 1
x = 0
y = 0
count = 0

while y < n:
    if data[y][x] == '#':
        count += 1
    y += 1
    x += 1
    x = x % l

mul *= count
x = 0
y = 0
count = 0

while y < n:
    if data[y][x] == '#':
        count += 1
    y += 1
    x += 3
    x = x % l

mul *= count
x = 0
y = 0
count = 0

while y < n:
    if data[y][x] == '#':
        count += 1
    y += 1
    x += 5
    x = x % l

mul *= count
x = 0
y = 0
count = 0

while y < n:
    if data[y][x] == '#':
        count += 1
    y += 1
    x += 7
    x = x % l

mul *= count
x = 0
y = 0
count = 0

while y < n:
    if data[y][x] == '#':
        count += 1
    y += 2
    x += 1
    x = x % l

mul *= count
print(mul)