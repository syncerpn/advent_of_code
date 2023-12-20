# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day20_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
class Node:
    nodes = {}
    queue = []
    
    def __init__(self, t=None):
        self.t = t
        self.oup = []
        self.inp = {}
        self.S = -1
    
    def send(self, s, node_name=None):
        if s:
            for nn in self.oup:
                r = Node.nodes[nn].recv(s, node_name)
                Node.queue.append((nn, r))
    
    def recv(self, s, node_name=None):
        if self.t == "%":
            if s == -1: #-1 low, 1 high
                #turn on 1 and send high 1
                self.S = -self.S
                return self.S
            
        elif self.t == "&":
            self.S = 1
            self.inp[node_name] = s
            for nn in self.inp:
                if self.inp[nn] == -1:
                    self.S = -1
            
            return -self.S
                
        else:
            if s:
                self.S = s
                return self.S
        
        return 0
    
    @staticmethod
    def status():
        stat = ""
        for k in Node.nodes:
            if Node.nodes[k].t:
                stat += "H" if Node.nodes[k].S == 1 else "L"
        
        return stat

for d in data:
    src, dsts = d.split(" -> ")
    dsts = dsts.split(", ")
    for dst in dsts:
        if dst not in Node.nodes:
            Node.nodes[dst] = Node()
        
    t = src[0]
    if t == "%" or t == "&":
        if src[1:] not in Node.nodes:
            Node.nodes[src[1:]] = Node()
        Node.nodes[src[1:]].t = t
        
        for dst in dsts:
            Node.nodes[src[1:]].oup.append(dst)
            Node.nodes[dst].inp[src[1:]] = -1
    else:
        if src not in Node.nodes:
            Node.nodes[src] = Node()
            
        for dst in dsts:
            Node.nodes[src].oup.append(dst)

N = 1000
stat_list = []
stat_dict = {}

cycle_found = False
for ni in range(N):
    # print(ni)
    stat = Node.status()
    if stat in stat_dict:
        cycle_found = True
        break
    
    Node.nodes["broadcaster"].send(-1, "broadcaster")
    
    low = 1 + len(Node.nodes["broadcaster"].oup)
    high = 0
    
    while Node.queue:
        nn, s = Node.queue.pop(0)
        if s and len(Node.nodes[nn].oup):
            # print(f"{nn} sends {s} to {' '.join(Node.nodes[nn].oup)}")
            Node.nodes[nn].send(s, nn)
            if s == -1:
                low += 1 * len(Node.nodes[nn].oup)
            elif s == 1:
                high += 1 * len(Node.nodes[nn].oup)
    
    stat_list.append(stat)
    stat_dict[stat] = (low, high)

if cycle_found:
    cycle = stat_list.index(stat)
    lows = 0
    highs = 0
    
    for i in range(cycle):
        stat = stat_dict[stat]
    
    chighs = 0
    clows = 0
    rhighs = 0
    rlows = 0
    
    n_cycles = (N - cycle) // (len(stat_list) - cycle)
    r = (N - cycle) % len(stat_list) - cycle
    
    for i in range(cycle, len(stat_list)):
        if (i - cycle) == r:
            rlows = clows
            rhighs = chighs
        
        low, high = stat_dict[stat_list[i]]
        clows += low
        chighs += high
    
    lows = rlows + clows * n_cycles
    highs = rhighs + chighs * n_cycles
    
    print(lows * highs)

else:
    lows = 0
    highs = 0
    
    for stat in stat_dict:
        low, high = stat_dict[stat]
        lows += low
        highs += high
    
    print(lows * highs)

#part2
Node.nodes = {}

for d in data:
    src, dsts = d.split(" -> ")
    dsts = dsts.split(", ")
    for dst in dsts:
        if dst not in Node.nodes:
            Node.nodes[dst] = Node()
        
    t = src[0]
    if t == "%" or t == "&":
        if src[1:] not in Node.nodes:
            Node.nodes[src[1:]] = Node()
        Node.nodes[src[1:]].t = t
        
        for dst in dsts:
            Node.nodes[src[1:]].oup.append(dst)
            Node.nodes[dst].inp[src[1:]] = -1
    else:
        if src not in Node.nodes:
            Node.nodes[src] = Node()
            
        for dst in dsts:
            Node.nodes[src].oup.append(dst)
            Node.nodes[dst].inp[src] = -1

import graphviz

dot = graphviz.Graph("part2", format="svg")
for nn in Node.nodes:
    dot.node(nn)

for nn in Node.nodes:
    for i in Node.nodes[nn].inp:
        dot.edge(i, nn, dir="forward")

dot.render("./aoc.svg")