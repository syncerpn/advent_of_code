# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 17:56:06 2022

@author: NghiaServer
"""

with open('day5_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

state = [
["T", "V", "J", "W", "N", "R", "M", "S", ],
["V", "C", "P", "Q", "J", "D", "W", "B", ],
["P", "R", "D", "H", "F", "J", "B", ],
["D", "N", "M", "B", "P", "R", "F", ],
["B", "T", "P", "R", "V", "H", ],
["T", "P", "B", "C", ],
["L", "P", "R", "J", "B", ],
["W", "B", "Z", "T", "L", "S", "C", "N", ],
["G", "S", "L", ],
]

state = [s[::-1] for s in state]

#part1
for d in data:
    n, src, dst = list(map(int, d.split(',')))
    src -= 1
    dst -= 1
    state[dst] += state[src][-n:][::-1]
    state[src] = state[src][:-n]

top_list = [s[-1] for s in state if s]
print(''.join(top_list))

state = [
["T", "V", "J", "W", "N", "R", "M", "S", ],
["V", "C", "P", "Q", "J", "D", "W", "B", ],
["P", "R", "D", "H", "F", "J", "B", ],
["D", "N", "M", "B", "P", "R", "F", ],
["B", "T", "P", "R", "V", "H", ],
["T", "P", "B", "C", ],
["L", "P", "R", "J", "B", ],
["W", "B", "Z", "T", "L", "S", "C", "N", ],
["G", "S", "L", ],
]

state = [s[::-1] for s in state]

#part2
for d in data:
    n, src, dst = list(map(int, d.split(',')))
    src -= 1
    dst -= 1
    state[dst] += state[src][-n:]
    state[src] = state[src][:-n]

top_list = [s[-1] for s in state if s]
print(''.join(top_list))