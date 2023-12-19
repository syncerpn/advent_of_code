# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:03:47 2022

@author: NghiaServer
"""

with open('day19_input') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

#part1
def check_condition(desc, cond):
    if cond is None:
        return True
    
    dn, compop, v = cond
    if compop == ">":
        if desc[dn] > v:
            return True
        return False
    
    elif compop == "<":
        if desc[dn] < v:
            return True
        return False

def process(desc, workflow):
    for cond_res in workflow:
        cond, res = cond_res
        if check_condition(desc, cond):
            return res

workflow = {}
parts = []
is_workflow = True
for d in data:
    if not d:
        is_workflow = False
        continue
    
    if is_workflow:
        name, conds = d[:-1].split("{")
        workflow[name] = []
        
        cond_res = conds.split(",")
        for cr in cond_res:
            if ":" in cr:
                c, r = cr.split(":")
                compop = ">"
                if compop not in c:
                    compop = "<"
                
                dn, v = c.split(compop)
                v = int(v)
                
                workflow[name].append(((dn, compop, v), r))
            else:
                workflow[name].append((None, cr))
    
    else:
        part_info = {}
        descs = d[1:-1].split(",")
        for desc in descs:
            k, v = desc.split("=")
            v = int(v)
            part_info[k] = v
        
        parts.append(part_info)

count = 0
for part in parts:
    wfn = "in"
    while wfn != "A" and wfn != "R":
        wfn = process(part, workflow[wfn])
    
    if wfn == "A":
        for k in part:
            count += part[k]
    
print(count)

#part2
class Node:
    nodes = {}
    
    def __init__(self, c=None, T_branch=None, F_branch=None):            
        self.p = []
        self.c = c
        self.T = T_branch
        self.F = F_branch
    
    def pass_condition(self, desc):
        if self.c is None:
            return True
        
        dn, compop, v = self.c
        if compop == ">":
            if desc[dn] > v:
                return True
            return False
        
        elif compop == "<":
            if desc[dn] < v:
                return True
            return False
    
    def move(self, desc):
        if self.pass_condition(desc):
            return self.T
        return self.F

KEYS = "xmas"

def combine_conditions(conditions, min_v, max_v):
    value_list = {k: list(range(min_v, max_v+1)) for k in KEYS}
    for cond in conditions:
        dn, compop, v = cond
        
        if compop == "<":
            value_list[dn] = [i for i in value_list[dn] if i < v]
        elif compop == ">":
            value_list[dn] = [i for i in value_list[dn] if i > v]
        elif compop == "<=":
            value_list[dn] = [i for i in value_list[dn] if i <= v]
        elif compop == ">=":
            value_list[dn] = [i for i in value_list[dn] if i >= v]
    
    return {dn: len(value_list[dn]) for dn in value_list}

Node.nodes = {}

for wfn in workflow:
    Node.nodes[wfn] = Node()

Node.nodes["A"] = Node()
Node.nodes["R"] = Node()
Node.nodes["in"].p = [None]

for wfn in workflow:
    bi_max = len(workflow[wfn]) - 2
    subnode_name = wfn
    for bi, b in enumerate(workflow[wfn]):
        cond, res = b
        
        if cond is None:
            Node.nodes[res].p += [subnode_name]
            Node.nodes[subnode_name].F = res
        else:
            if bi > 0:
                subnode_name = wfn + "_" + str(bi)
            
            subnode_next = None
            if bi < bi_max:
                subnode_next = wfn + "_" + str(bi+1)
            
            if subnode_name not in Node.nodes:
                Node.nodes[subnode_name] = Node()
            
            Node.nodes[res].p += [subnode_name]
            
            Node.nodes[subnode_name].c = cond
            Node.nodes[subnode_name].T = res
            Node.nodes[subnode_name].F = subnode_next
            
            if subnode_next:
                if subnode_next not in Node.nodes:
                    Node.nodes[subnode_next] = Node()
                Node.nodes[subnode_next].p += [subnode_name]

count = 0

dest_nodes = ["A"]

for dst in dest_nodes:
    node_cur = dst
    for nn in list(set(Node.nodes[dst].p)):
        conditions = []
        node_prev = nn
        node_cur = dst
        while node_prev:
            if node_cur == Node.nodes[node_prev].T:
                if Node.nodes[node_prev].T != Node.nodes[node_prev].F:
                    conditions.append(Node.nodes[node_prev].c)
                    
            elif node_cur == Node.nodes[node_prev].F:
                if Node.nodes[node_prev].T != Node.nodes[node_prev].F:
                    dn, compop, v = Node.nodes[node_prev].c
                    if compop == "<":
                        compop = ">="
                    else:
                        compop = "<="
                    conditions.append((dn, compop, v))
            
            node_cur = node_prev
            node_prev = Node.nodes[node_prev].p[0]
        
        print(nn, conditions)
        cc = combine_conditions(conditions, 1, 4000)
        m = 1
        for k in cc:
            m *= cc[k]
        count += m
        
    print(count)