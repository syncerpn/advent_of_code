# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 19:15:05 2021

@author: Syncer
"""

### def
def two_numbers_with_sum_of(s, number_list, find_all=False):
    diff_dict = {}
    result = []
    for t in number_list:
        d = s - t #the partner of t
        diff_dict[str(d)] = d
    
    for t in number_list:
        if diff_dict.get(str(t)) is not None:
            result.append([t, s-t])
            if not find_all:
                return result
    
    return result

def n_numbers_with_sum_of(n, s, number_list, find_all=False):
    result = []
    if n > 2:
        for i, t in enumerate(number_list):
            reduced_list = [a for j, a in enumerate(number_list) if j != i]
            t_result = n_numbers_with_sum_of(n-1, s-t, reduced_list, find_all)
            if t_result:
                result = [[t] + element for element in t_result]
                if not find_all:
                    return result
    else:
        result = two_numbers_with_sum_of(s, number_list, find_all)
    return result

### main
with open('day1_input') as f:
    data = f.readlines()

data = [int(d.strip('\n')) for d in data]

result_2 = two_numbers_with_sum_of(2020, data)
m_2 = 1
for a in result_2[0]:
    m_2 *= a
print(m_2)

result_3 = n_numbers_with_sum_of(3, 2020, data)
m_3 = 1
for a in result_3[0]:
    m_3 *= a
print(m_3)