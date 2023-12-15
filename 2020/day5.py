# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 16:07:22 2021

@author: Nghia
"""

### def


### main
with open('day5_input') as f:
    data = f.readlines()

data = [line.strip('\n') for line in data]

#part1
bdata = []
max_seat_id = 0
min_seat_id = 1000000
occupied = {}
for entry in data:
    seat_id = 0
    for e in entry:
        seat_id *= 2
        if e == 'B' or e == 'R':
            seat_id += 1
    
    if seat_id > max_seat_id:
        max_seat_id = seat_id
        
    if seat_id < min_seat_id:
        min_seat_id = seat_id
    
    occupied[str(seat_id)] = 1

print(max_seat_id)

#part2
for i in range(min_seat_id, max_seat_id+1):
    if occupied.get(str(i)) == None:
        print(i)
        break