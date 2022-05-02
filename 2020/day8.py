# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 16:07:22 2021

@author: Nghia

"""
### def
def execute(code):
    acc = 0
    i = 0
    executed = [0 for i in range(len(code))]
    while (i < len(code)):
        if executed[i] == 1:
            return 0, acc, executed
        
        executed[i] = 1
        inst, val = code[i].split(' ')
        
        if inst == 'nop':
            i += 1
        elif inst == 'acc':
            i += 1
            acc += int(val)
        elif inst == 'jmp':
            i += int(val)

    return 1, acc, executed

### main
with open('day8_input') as f:
    data = f.readlines()

data = [line.strip('\n') for line in data]

# part 1
sc, acc, exed = execute(data)
print(acc)

# part 2

for i in range(len(exed)):
    if exed[i] == 1:
        tmp_data = data.copy()
        inst, val = tmp_data[i].split(' ')
        if inst == 'nop':
            tmp_data[i] = ' '.join(['jmp', val])
        elif inst == 'jmp':
            tmp_data[i] = ' '.join(['nop', val])
        else:
            continue
        sc, acc, _ = execute(tmp_data)
        if sc:
            print(acc)
            break