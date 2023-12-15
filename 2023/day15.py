# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day15_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
dl = data[0].split(",")
s = 0
for d in dl:
    h = 0
    for c in d:
        h += ord(c)
        h *= 17
        h %= 256
    s += h
    
print(s)

#part2
def hash(s):
    h = 0
    for c in s:
        h = 17 * (h + ord(c)) % 256
    
    return h

dl = data[0].split(",")
box = {k: {} for k in range(256)}
box_list = {k: [] for k in range(256)}

for d in dl:
    if "=" in d:
        lbl_str, fl = d.split("=")
        box_id = hash(lbl_str)    
        fl = int(fl)
        
        if lbl_str not in box_list[box_id]:
            box_list[box_id].append(lbl_str)
        box[box_id][lbl_str] = fl
    
    elif "-" in d:
        lbl_str = d[:-1]
        box_id = hash(lbl_str)
        
        if lbl_str in box_list[box_id]:
            box_list[box_id].remove(lbl_str)

score = 0
for k in range(256):
    for li, lbl_str in enumerate(box_list[k]):
        score += (k + 1) * (li + 1) * box[k][lbl_str]

print(score)