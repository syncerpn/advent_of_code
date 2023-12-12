# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day12_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1

DMG_PATTERN = "[#?]"
SEP_PATTERN = "(?!#)[?.]+?"

import re
for d in data:
    d = "?###???????? 3,2,1"
    record, info = d.split(" ")
    parts = [i for i in record.split(".") if i]
    groups = list(map(int, info.split(",")))
    
    pattern = ""
    for i, g in enumerate(groups):
        pattern += f"({DMG_PATTERN}{{{g}}})"
        if i < len(groups) - 1:
            pattern += f"{SEP_PATTERN}"
    
    pattern = f"(?={pattern})"
    pattern = "(?=(?=([#?]{3})(?!#)[?.]+?([#?]{2})(?!#)[?.]+?)([#?]{1}))"
    for m in re.finditer(pattern, record):
        for i in range(len(groups)):
            print(m.start(i+1), m.end(i+1), m.group(i+1))
    
    assert 0

#part2