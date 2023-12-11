# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day5_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

debug = -1

#part1
class RangeMapper:
    def __init__(self, range_list_str):
        self.range_list = []
        for range_str in range_list_str:
            range_i = list(map(int, range_str.split(" ")))
            self.range_list.append(range_i)
    
    def get_dest(self, n):
        for ri in self.range_list:
            dst_s, src_s, l = ri
            if n >= src_s and n < src_s + l:
                return dst_s + n - src_s
        
        return n

def chain_map(range_mapper_list, n):
    for range_mapper in range_mapper_list:
        n = range_mapper.get_dest(n)
    
    return n

score = None
all_seeds = []
di = 0
range_mapper_list = []
count = 0
while di < len(data):
    d = data[di]
    if d[0:6] == "seeds:":
        all_seeds = list(map(int, d[7:].split(" ")))
        di += 2
    else:
        range_mapper_info = []
        while di < len(data):
            if data[di]:
                range_mapper_info.append(data[di])
            else:
                break
            di += 1
        
        range_mapper_list.append(RangeMapper(range_mapper_info))
        count += 1
        if count == debug:
            break
        di += 1
    
    di += 1

for seed in all_seeds:
    if score is None:
        score = chain_map(range_mapper_list, seed)
    else:
        score = min(score, chain_map(range_mapper_list, seed))

print(score)

#part2

class RangeMapperAcc:
    @staticmethod
    def _get_mapped_range(x, l, mapper):
        ys = []
        keys = sorted(mapper.keys())
        if not keys:
            return [(x, x, l)]
        
        ki = 0
        
        ke = keys[ki]
        if x < ke:
            n = min(ke - x, l)
            ys.append((x, x, n))
            l = l - n
            x = ke
        
        while ki < len(keys) - 1 and l > 0:
            ks = keys[ki]
            ke = keys[ki+1]
            if ks <= x and ke > x:
                n = min(ke - x, l)
                ys.append((mapper[ks] + x - ks, x, n))
                l = l - n
                x = ke
            
            ki += 1
            
        if l > 0:
            ks = keys[ki]
            ys.append(mapper[ks] + x - ks, x, l)
    
        return ys
            
    def __init__(self):
        self.xy = {}
        self.yx = {}
    
    def add_layer(self, range_list_str):
        for range_str in range_list_str:
            range_i = list(map(int, range_str.split(" ")))
            dst, src, l = range_i
            
            srcs_origin = self.get_src(src, l)
            
            for segment in srcs_origin:
                src_origin, dst_origin, l_seg = segment
                self.xy[src_origin] = dst
                if src_origin + l_seg not in self.xy:
                    self.xy[src_origin + l_seg] = dst_origin + l_seg
                    
                dst += l_seg

        self.yx = {}
        for k, v in self.xy.items():
            self.yx[v] = k
        
    def get_dst(self, x, l):
        return RangeMapperAcc._get_mapped_range(x, l, self.xy)
    
    def get_src(self, y, l):
        return RangeMapperAcc._get_mapped_range(y, l, self.yx)

score = None
all_seeds = []
di = 0
count = 0
range_mapper_acc = RangeMapperAcc()
while di < len(data):
    d = data[di]
    if d[0:6] == "seeds:":
        all_seeds = list(map(int, d[7:].split(" ")))
        di += 2
    else:
        range_mapper_info = []
        while di < len(data):
            if data[di]:
                range_mapper_info.append(data[di])
            else:
                break
            di += 1
        
        range_mapper_acc.add_layer(range_mapper_info)
        count += 1
        if count == debug:
            break
        di += 1
    
    di += 1

for i in range(len(all_seeds) // 2):
    seed_start = all_seeds[2 * i]
    num_seed = all_seeds[2 * i + 1]
    
    locs = range_mapper_acc.get_dst(seed_start, num_seed)
    for loc in locs:
        s, _, _ = loc
        if score is None:
            score = s
        else:
            score = min(score, s)

print(score)











