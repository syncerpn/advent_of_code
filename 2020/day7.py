# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 16:07:22 2021

@author: Nghia
"""

import re

delim = r'\sbags,\s|\sbag,\s|\sbag.|\sbags.'

### def
class bag:
    def __init__(self, look):
        self.look = look
        
    def contain(self, contents, amounts):
        self.contents = contents
        self.amounts = amounts

def count_num_bag_inside_single_target(bags, target):
    n = 0
    for bag in bags:
        if bag.look == target:
            if bag.contents:
                for i, bag_in in enumerate(bag.contents):
                    n += bag.amounts[i] * count_num_bag_inside_single_target(bags, bag_in)
            return n + 1
            

### main
with open('day7_input') as f:
    data = f.readlines()

data = [line.strip('\n') for line in data]

bags = []

for entry in data:
    look, inside = entry.split(' bags contain ')
    inside = re.split(delim, inside)
    inside = inside[0:-1]
    contents = []
    amounts = []
    for content in inside:
        if content != 'no other':
            [amount, attr_a, attr_b] = content.split(' ')
            amounts.append(int(amount))
            contents.append(' '.join([attr_a, attr_b]))
    
    new_bag = bag(look)
    new_bag.contain(contents, amounts)
    bags.append(new_bag)

#part 1
# target = ['shiny gold']
# levels = [0 for bag in bags]
# old_sum = 0
# cur_level = 1
# while (sum(levels) != old_sum) or (old_sum == 0):    
#     next_target = []
#     old_sum = sum(levels)
#     for i, bag in enumerate(bags):
#         if levels[i] == 0:
#             if set(target).intersection(set(bag.contents)):
#                 levels[i] = cur_level
#                 next_target.append(bag.look)
#     target = next_target
#     cur_level += 1
    
# count = sum([1 for i in levels if i != 0])

#part 2
count_2 = count_num_bag_inside_single_target(bags, 'shiny gold') - 1 #minus the top one