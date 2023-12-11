# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day6_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
times = [d for d in data[0].split(" ") if d]
times = list(map(int, times[1:]))
distances = [d for d in data[1].split(" ") if d]
distances = list(map(int, distances[1:]))

score = 1

for t, d in zip(times, distances):
    for i in range(t):
        if i * (t - i) >= d:
            print(i, abs(2*i - t) + 1)
            score *= abs(2*i - t) + 1
            break

print(score)

#part2
times = [d for d in data[0].split(" ") if d]
t = int("".join(times[1:]))
distances = [d for d in data[1].split(" ") if d]
d = int("".join(distances[1:]))

score = 1

for i in range(t):
    if i * (t - i) >= d:
        print(i, abs(2*i - t) + 1)
        score *= abs(2*i - t) + 1
        break

print(score)

#part2b: or use binary search
l = 0
r = t
i = t // 2

i_best = i

while (l + r) // 2 != l:
    if i * (t - i) >= d:
        r = i
        i_best = i
    else:
        l = i
    
    i = (l + r) // 2

score = abs(2*i_best - t) + 1

print(score)