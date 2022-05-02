# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 00:03:13 2021

@author: Syncer
"""

### main
with open('day2_input') as f:
    data = f.readlines()
    
valid = 0
for entry in data:
    [policy, char, string] = entry.split(' ')
    [min_char, max_char] = map(int, policy.split('-'))
    char = char.strip(':')
    string = string.strip('\n')
    count = 0
    for i in range(len(string)):
        if string[i] == char:
            count += 1
    if count >= min_char and count <= max_char:
        valid += 1
        
print(valid)
    
valid = 0
for entry in data:
    [policy, char, string] = entry.split(' ')
    [pos_1, pos_2] = map(int, policy.split('-'))
    char = char.strip(':')
    string = string.strip('\n')
    count = 0
    if string[pos_1-1] == char:
        count += 1
        
    if string[pos_2-1] == char:
        count += 1
        
    if count == 1:
        valid += 1
        
print(valid)