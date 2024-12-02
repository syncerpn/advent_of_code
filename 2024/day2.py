# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day2_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
ans = 0

for d in data:
    nums = list(map(int, d.split(" ")))
    p = nums[0]
    q = 0
    for n in nums[1:]:
        if n != p:
            if q == 0:
                if n - p > 3 or n - p < -3:
                    break
                q = 1 if n > p else -1
            elif q == 1 and (n < p or n - p > 3):
                break
            elif q == -1 and (n > p or p - n > 3):
                break
        else:
            break
        p = n
    else:
        print(nums)
        ans += 1

print(ans)

#part2
ans = 0

for d in data:
    nums_ori = list(map(int, d.split(" ")))
    for i in range(len(nums_ori)):
        nums = nums_ori[:i] + nums_ori[i+1:]
        p = nums[0]
        q = 0
        for n in nums[1:]:
            if n != p:
                if q == 0:
                    if n - p > 3 or n - p < -3:
                        break
                    q = 1 if n > p else -1
                elif q == 1 and (n < p or n - p > 3):
                    break
                elif q == -1 and (n > p or p - n > 3):
                    break
            else:
                break
            p = n
        else:
            print(nums)
            ans += 1
            break

print(ans)