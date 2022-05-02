# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 16:07:22 2021

@author: Nghia
"""

### def


### main
with open('day4_input') as f:
    data = f.readlines()

data = [line.strip('\n') for line in data]

book = [{}]
i = 0
for line in data:
    if line == '':
        i += 1
        book +=[{}]
    else:
        all_entry = line.split(' ')
        for entry in all_entry:
            pair = entry.split(':')
            book[i][pair[0]] = pair[1]

## part 1
count = len(book)
require_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for passport in book:
    for item in require_list:
        if passport.get(item) == None:
            count -= 1
            break

import re
## part 2
count = len(book)
require_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for passport in book:
    for item in require_list:
        value = passport.get(item)
        if value == None:
            count -= 1
            break
        else:
            if item == 'byr':
                value = int(value)
                if value < 1920 or value > 2002:
                    count -= 1
                    break
            if item == 'iyr':
                value = int(value)
                if value < 2010 or value > 2020:
                    count -= 1
                    break
            if item == 'eyr':
                value = int(value)
                if value < 2020 or value > 2030:
                    count -= 1
                    break
            if item == 'hgt':
                if value[-2:] == 'in':
                    if int(value[:-2]) < 59 or int(value[:-2]) > 76:
                        count -= 1
                        break
                elif value[-2:] == 'cm':
                    if int(value[:-2]) < 150 or int(value[:-2]) > 193:
                        count -= 1
                        break
                else:
                    count -= 1
                    break
            if item == 'hcl':
                pattern = r'^#[0-9a-f]{6}$'
                if not re.match(pattern, value):
                    count -= 1
                    break
            if item == 'ecl':
                if value != 'amb' and value != 'blu' and value != 'brn' and value != 'gry' and value != 'grn' and value != 'hzl' and value != 'oth':
                    count -= 1
                    break
            if item == 'pid':
                pattern = r'^[0-9]{9}$'
                if not re.match(pattern, value):
                    count -= 1
                    break
                else:
                    print(value)
                    
                
                    
                

    
