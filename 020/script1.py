from __future__ import annotations

from sys import argv
from tqdm import tqdm
from dataclasses import dataclass

# test: 
# input: 645 too low, 22539 to high

lines = open(argv[1], 'r').read().splitlines()

enc_file = [int(n) for n in lines]

def print_ll(ll_first_node):
    l = []
    node = ll_first_node
    for _ in enc_file:
        l.append(f"{node.val :>3}")
        node = node.nxt
    print(" ".join(l))

@dataclass
class Node:
    val: int
    prv: Node
    nxt: Node

    def __str__(self):
        prv_val = self.prv.val if self.prv else None
        nxt_val = self.nxt.val if self.nxt else None
        return f"{prv_val} [{self.val}] {nxt_val}"

ll_first, ll_last = None, None
ll_map = dict()
zero_node = None

prv_node = None
for i, e_val in enumerate(enc_file):
    curr_node = Node(e_val, prv_node, None)

    if e_val == 0:
        zero_node = curr_node

    ll_map[i] = curr_node

    if i == 0:
        ll_first = curr_node
    if i == len(enc_file) - 1:
        ll_last = curr_node

    if prv_node:
        prv_node.nxt = curr_node

    prv_node = curr_node

ll_first.prv = ll_last
ll_last.nxt = ll_first

for e_i, e_val in enumerate(enc_file):
    e_node = ll_map[e_i]

    if e_val == 0:
        continue

    # cut it out 
    e_prv = e_node.prv
    e_nxt = e_node.nxt
    e_prv.nxt = e_nxt
    e_nxt.prv = e_prv

    # put it in new location
    ne_node = e_node

    if e_val > 0:
        for i in range(abs(e_val)):
            ne_node = ne_node.nxt
        nne_node = ne_node.nxt
        ne_node.nxt = e_node
        nne_node.prv = e_node
        e_node.prv = ne_node
        e_node.nxt = nne_node
    elif e_val < 0:
        for i in range(abs(e_val)):
            ne_node = ne_node.prv
        nne_node = ne_node.prv
        ne_node.prv = e_node
        nne_node.nxt = e_node
        e_node.nxt = ne_node
        e_node.prv = nne_node

print_ll(ll_first)

r = []
n = zero_node
for i in range(1, 3001):
    n = n.nxt
    if i in (1000, 2000, 3000):
        # print(n.val)
        r.append(n.val)

print(f"r={sum(r)}")