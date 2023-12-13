# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day12_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
def count_ones(n):
    index = []
    c = 0
    
    while n:
        if n % 2:
            index.append(c)
        c += 1
        n = n >> 1
    return index

def pairing_replace(base_str, windex, rindex):
    base_str_i = [c for c in base_str]
    for i, wi in enumerate(windex):
        if i in rindex:
            base_str_i[wi] = "#"
        else:
            base_str_i[wi] = "."
    
    return "".join(base_str_i)

counts = []
for di, d in enumerate(data):
    print(di)
    record, info = d.split(" ")
    parts = [i for i in record.split(".") if i]
    groups = list(map(int, info.split(",")))
    
    wc_ids = [i for i, ltr in enumerate(record) if ltr == "?"]
    nwc = len(wc_ids)
    n_hash = sum(groups) - record.count("#")
    n_dot = nwc - n_hash
    
    count = 0
    for i in range(2 ** nwc):
        hash_index = count_ones(i)
        # hash_index = [ci for ci, c in enumerate(str(bin(i))[-1:1:-1]) if c == "1"]
        if len(hash_index) == n_hash:
            base_str_i = pairing_replace(record, wc_ids, hash_index)
        
            if [len(g) for g in base_str_i.split(".") if g] == groups:
                count += 1
    
    counts.append(count)

print(sum(counts))
#part2

counts = []
for di, d in enumerate(data):
    print(di)
    record, info = d.split(" ")
    parts = [i for i in record.split(".") if i]
    groups = list(map(int, info.split(",")))
    
    record = (record + "?") * 1 + record
    groups = groups * 2
    
    wc_ids = [i for i, ltr in enumerate(record) if ltr == "?"]
    nwc = len(wc_ids)
    n_hash = sum(groups) - record.count("#")
    n_dot = nwc - n_hash
    
    count = 0
    for i in range(2 ** nwc):
        hash_index = [ci for ci, c in enumerate(str(bin(i))[2:]) if c == "1"]
        if len(hash_index) == n_hash:
            base_str_i = pairing_replace(record, wc_ids, hash_index)
        
            if [len(g) for g in base_str_i.split(".") if g] == groups:
                count += 1
    
    counts.append(count)

print(sum(counts))
