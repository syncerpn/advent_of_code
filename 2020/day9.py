# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 16:07:22 2021

@author: Nghia

"""
### def


### main
with open('day9_input') as f:
    data = f.readlines()

data = [int(line.strip('\n')) for line in data]

# part 1
k = 25
n = len(data)

sus_list = []

for i in range(n-k):
    found = False
    s = data[i+k]
    preamble_list = data[i:i+k]
    for p in preamble_list:
        q = s - p
        if (q != p) and (q in preamble_list):
            found = True
            break
    
    if not found:
        sus_list += [s]
        break

print(sus)
#part2
sus = sus_list[0]

go_on_list = []

for ip,p in enumerate(data):
    go_on_list = [g + p for g in go_on_list] + [p]
    if sus in go_on_list:
        break

for ig,g in enumerate(go_on_list):
    if g == sus:
        break

sus_set = data[ig:ip+1]

gmin=sus_set[0]
gmax=sus_set[0]

for g in sus_set:
    if g < gmin:
        gmin = g
    if g > gmax:
        gmax = g

print(gmin+gmax)