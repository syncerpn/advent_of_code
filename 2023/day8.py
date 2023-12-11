# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day8_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
loc = "AAA"
dest = "ZZZ"

seq = data[0]

network = {}
for d in data[2:]:
    k, branch = d.split(" = ")
    lb, rb = branch[1:-1].split(", ")
    network[k] = {}
    network[k]["L"] = lb
    network[k]["R"] = rb

i = 0
n = len(seq)
step = 0
while loc != dest:
    inst = seq[i]
    loc = network[loc][inst]
    i = (i + 1) % n
    step += 1

print(step)

#part2

def loc_end_correct(loc, dest_end_mark):
    if loc[-1] != dest_end_mark:
        return False
    
    return True

dest_end_mark = "Z"
starting_end_mark = "A"

seq = data[0]
locs = []
network = {}
for d in data[2:]:
    k, branch = d.split(" = ")
    if k[2] == starting_end_mark:
        locs.append(k)
    lb, rb = branch[1:-1].split(", ")
    network[k] = {}
    network[k]["L"] = lb
    network[k]["R"] = rb

n = len(seq)
steps = []
for loc in locs:
    step = 0
    i = 0
    while not loc_end_correct(loc, dest_end_mark):
        inst = seq[i]
        loc = network[loc][inst]
        i = (i + 1) % n
        step += 1
    steps.append(step)

import math

total_steps = 1
for step in steps:
    total_steps = total_steps * step // math.gcd(total_steps, step)

print(total_steps)

