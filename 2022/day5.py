# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 17:56:06 2022

@author: NghiaServer
"""

with open('day5_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

state = [
        ['M','F','C','W','T','D','L','B'],
        ['L','B','N'],
        ['V','L','T','H','C','J'],
        ['W','J','P','S'],
        ['R','L','T','F','C','S','Z'],
        ['Z','N','H','B','G','D','W'],
        ['N','C','G','V','P','S','M','F'],
        ['Z','C','V','F','J','R','Q','W'],
        ['H','L','M','P','R'],
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
        ['M','F','C','W','T','D','L','B'],
        ['L','B','N'],
        ['V','L','T','H','C','J'],
        ['W','J','P','S'],
        ['R','L','T','F','C','S','Z'],
        ['Z','N','H','B','G','D','W'],
        ['N','C','G','V','P','S','M','F'],
        ['Z','C','V','F','J','R','Q','W'],
        ['H','L','M','P','R'],
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