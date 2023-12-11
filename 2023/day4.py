# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day4_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]
#part1
score = 0
for d in data:
    card_id, content = d.split(": ")
    winning_list, having_list = content.split(" | ")
    winning_list = [n for n in winning_list.split(" ") if n]
    having_list = [n for n in having_list.split(" ") if n]
    
    common = set(winning_list).intersection(set(having_list))
    if len(common) > 0:
        score += 2 ** (len(common) - 1)

print(score)

#part2
score = 0
n = len(data)
copies = {i: 1 for i in range(n)}
for di, d in enumerate(data):
    card_id, content = d.split(": ")
    winning_list, having_list = content.split(" | ")
    winning_list = [n for n in winning_list.split(" ") if n]
    having_list = [n for n in having_list.split(" ") if n]
    
    common = set(winning_list).intersection(set(having_list))
    for ci in range(len(common)):
        if di + ci + 1 < n:
            copies[di + ci + 1] += copies[di]

for i in copies:
    score += copies[i]

print(score)