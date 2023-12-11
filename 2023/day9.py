# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day9_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
import numpy as np
seqs = [list(map(int, d.split(" "))) for d in data]

score = 0
for seq in seqs:
    array_end = 0
    while np.sum(np.absolute(np.array(seq))) != 0:
        array_end += seq[-1]
        seq = [seq[i+1] - seq[i] for i in range(len(seq) - 1)]        
    
    score += array_end

print(score)

#part2
import numpy as np
seqs = [list(map(int, d.split(" "))) for d in data]

score = 0
for seq in seqs:
    array_end = 0
    sign = 1
    while np.sum(np.absolute(np.array(seq))) != 0:
        array_end += sign * seq[0]
        sign = -sign
        seq = [seq[i+1] - seq[i] for i in range(len(seq) - 1)]
    
    score += array_end

print(score)