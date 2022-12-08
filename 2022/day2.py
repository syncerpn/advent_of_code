# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:07:26 2022

@author: NghiaServer
"""

with open('day2_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

opponent = []
you = []
rule_score = {'A': 1, 'B': 2, 'C': 3}
win = {'A': 'B', 'B': 'C', 'C': 'A'}
lose = {'A': 'C', 'B': 'A', 'C': 'B'}
draw = {'A': 'A', 'B': 'B', 'C': 'C'}

#part1
score = 0

for d in data:
    i, j = d.split(' ')
    j = chr(ord(j) - 23)
    opponent.append(i)
    you.append(j)
    
    score += rule_score[j]
    
    if j == win[i]:
        score += 6
    elif j == i:
        score += 3
    
print(score)

#part2
score = 0
rule2 = {'X': lose, 'Y': draw, 'Z': win}
rule2_score = {'X': 0, 'Y': 3, 'Z': 6}

for d in data:
    i, j = d.split(' ')
    
    score += rule2_score[j] + rule_score[rule2[j][i]]
    
print(score)