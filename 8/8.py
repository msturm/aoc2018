#!/usr/bin/env python3
file1 = '8.in'
# file1 = '8.test'
pc = 0
inp = []
nodes = {}

with open(file1, 'r') as f:
    for v in f:
        inp = [int(x) for x in v.strip().split(' ')]

def createNode():
    global pc
    nodecount = inp[pc]
    pc += 1
    meta_count = inp[pc]
    pc += 1
    node = {'meta': [], 'childs': []}
    for n in range(0, nodecount):
        node['childs'].append(createNode())
    for n in range(0, meta_count):
        node['meta'].append(inp[pc])
        pc += 1
    return node


def sum_meta(agg, node):
    sum_this_meta = agg + sum(node['meta'])
    for x in node['childs']:
       sum_this_meta += sum_meta(agg, x)

    return sum_this_meta

def sum_meta_p2(agg, node):
    if len(node['childs']) == 0:
        return sum(node['meta'])
    else:
        newagg = 0
        for x in node['meta']:
            if 0 < x <= len(node['childs']):
                newagg += sum_meta_p2(agg, node['childs'][x -1])
        return newagg

# while pc < len(inp):
supernode = createNode()

# print(supernode)
print("p1 {0}".format(sum_meta(0, supernode)))
print("p2 {0}".format(sum_meta_p2(0, supernode)))

