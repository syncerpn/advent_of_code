# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 16:07:22 2021

@author: Nghia
"""

### def


### main
with open('day6_input') as f:
    data = f.readlines()

data = [line.strip('\n') for line in data]
data.append('')
#part 1
count = 0
group = []
for i in data:
    if i != '':
        group.append(i)
    else:
        count += len(set(''.join(group)))
        group = []

print(count)
#part 2        
count = 0
group = {}
first = True
for i in data:
    if i != '':
        if first:
            group = set(i)
            first = False
        else:
            group = group.intersection(set(i))
    else:
        first = True
        count += len(group)
        group = {}

print(count)