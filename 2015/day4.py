# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day4_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
d = data[0]
import hashlib

secret = d

i = 0
found = False
while not found:
    i += 1
    key = secret + str(i)
    md5hash = hashlib.md5(key.encode())
    if md5hash.hexdigest().startswith("00000"):
        found = True

print(i)

#part2
d = data[0]
import hashlib

secret = d

i = 0
found = False
while not found:
    i += 1
    key = secret + str(i)
    md5hash = hashlib.md5(key.encode())
    if md5hash.hexdigest().startswith("000000"):
        found = True

print(i)