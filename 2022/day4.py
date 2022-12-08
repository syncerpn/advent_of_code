# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 17:34:51 2022

@author: NghiaServer
"""

with open('day4_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part 1
count = 0
for d in data:
    x,y = d.split(',')
    xs, xe = list(map(int,x.split('-')))
    ys, ye = list(map(int,y.split('-')))
    if (xs <= ys) and (xe >= ye):
        count += 1
    elif (ys <= xs) and (ye >= xe):
        count += 1
print(count)

#part 2
count = 0
for d in data:
    x,y = d.split(',')
    xs, xe = list(map(int,x.split('-')))
    ys, ye = list(map(int,y.split('-')))
    
    ms = max(xs,ys)
    me = min(xe,ye)
    
    if ms <= me:
        print(d)
        count += 1
print(count)