# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day2_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
limit = {
    "red": 12,
    "green": 13,
    "blue": 14,
         }

sum_id = 0
for d in data:
    game_id, content = d.split(": ")
    gid = int(game_id.split(" ")[1])
    
    packs = content.split("; ")
    invalid = False
    for pack in packs:
        cubes = pack.split(", ")
        for cube in cubes:
            num, color = cube.split(" ")
            num = int(num)
            if num > limit[color]:
                invalid = True
                break
        if invalid:
            break
    
    if invalid:
        continue
    sum_id += gid

print(sum_id)
            

#part2
cube_dict = {}
sum_id = 0
for d in data:
    _, content = d.split(": ")
    cube_dict["red"] = 0
    cube_dict["green"] = 0
    cube_dict["blue"] = 0
    
    packs = content.split("; ")
    
    for pack in packs:
        cubes = pack.split(", ")
        for cube in cubes:
            num, color = cube.split(" ")
            num = int(num)
            if num > cube_dict[color]:
                cube_dict[color] = num
    
    sum_id += cube_dict["red"] * cube_dict["green"] * cube_dict["blue"]

print(sum_id)