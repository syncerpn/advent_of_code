# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 19:43:44 2022

@author: NghiaServer
"""

with open('day7_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

tree = {}

for d in data:
    d = d.split(' ')
    if d[0] == '$':
        break