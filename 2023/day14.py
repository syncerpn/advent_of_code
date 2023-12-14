# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day14_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
def transpose(pattern):
    tpattern = ["".join([pattern[hi][wi] for hi in range(len(pattern))]) for wi in range(len(pattern[0]))]
    return tpattern

tdata = transpose(data)
load = 0
for d in tdata:
    lb = len(tdata[0])
    for i, c in enumerate(d):
        if c == "#":
            lb = len(tdata[0])-i-1
        if c == "O":
            load += lb
            lb -= 1
    
print(load)

#part2
import numpy as np
ndata = np.array([[c for c in d] for d in data])

def roll(board):
    h, w = board.shape
    for wi in range(w):
        base = 0
        for hi in range(h):
            if board[hi, wi] == "#":
                base = hi+1
                
            elif board[hi, wi] == "O":
                board[hi, wi] = "."
                board[base, wi] = "O"
                base += 1
    
    return board
    
def rotate90(board):
    h, w = board.shape
    new_board = np.array([["" for _ in range(h)] for _ in range(w)])
    
    for hi in range(h):
        for wi in range(w):
            new_board[wi, h-1-hi] = board[hi, wi]
    
    return new_board

def load_north(board):
    h, w = board.shape
    pos = np.where(board == "O")
    load = h - pos[0]
    return np.sum(load)
    

CYCLE = 1000000000

def string_board(board):
    board_str = ["".join(list(b)) for b in board]
    return "".join(board_str)
    
states = {}
steps = {}
loop = 0
for i in range(CYCLE):
    ndata = roll(ndata)
    ndata = rotate90(ndata)
    ndata = roll(ndata)
    ndata = rotate90(ndata)
    ndata = roll(ndata)
    ndata = rotate90(ndata)
    ndata = roll(ndata)
    ndata = rotate90(ndata)
    
    bs = string_board(ndata)
    if bs in states:
        loop = i
        print("[INFO] loop found")
        break
    else:
        states[bs] = i
        steps[i] = load_north(ndata)

if loop:
    loop_base = states[bs]
    CYCLE_loop = (CYCLE - 1 - loop_base) % (loop - loop_base) + loop_base
    print(CYCLE_loop)
    print(steps[CYCLE_loop])
else:
    print(load_north(ndata))