# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day1_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
sum_max = 0
sum_c = 0
sum_i = 0
i = 0
for d in data:
    if d:
        sum_c += int(d)
    
    else:
        if sum_max < sum_c:
            sum_max = sum_c
            sum_i = i
        
        sum_c = 0
        i += 1

print(sum_max)

#part2
sum_list = []

sum_c = 0
for d in data:
    if d:
        sum_c += int(d)
    
    else:
        sum_list.append(sum_c)
        sum_c = 0

sum_list.sort()
print(sum(sum_list[-3:]))