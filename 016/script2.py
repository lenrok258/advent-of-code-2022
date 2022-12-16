from sys import argv
import re
from queue import PriorityQueue
import itertools
from functools import lru_cache
from collections import defaultdict

# test: 
# input: 2100 (8s)

def dijkstra(next_nodes, start_node, end_node):
    pq = PriorityQueue()
    pq.put((0, start_node))
    visited = set(start_node)
    while True:
        curr_cost, curr_node = pq.get()
        if curr_node == end_node:
            return curr_cost
        ns = next_nodes(curr_node)
        for n in ns:
            if n not in visited:
                pq.put((curr_cost + 1, n))
                visited.add(n)


lines = open(argv[1], 'r').read().splitlines()
pipes = [re.split("Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)", l) for l in lines]
pipes = [(p[1], int(p[2]), p[3].split(", ")) for p in pipes]

pmap = dict()
for p in pipes:
    pmap[p[0]] = {"rate": p[1], "tunels": p[2], "open": False}

dmap = {}
for pk_from, pv_from in pmap.items():
    for pk_to, pv_to in pmap.items():
        dist = dijkstra(lambda p:pmap[p]["tunels"], pk_from, pk_to)
        dmap[pk_from + "_" + pk_to] = dist

@lru_cache(maxsize=None)
def compute_preasure(valves, start_tick):
    if len(valves) == 0:
        return 0
    if start_tick <= 0:
        return -1
    p = valves[0]
    p_rate = pmap[p]["rate"]
    p_open_penality = 0 if p_rate == 0 else 1
    value_0 = p_rate * (start_tick - p_open_penality)

    p_dist_penality = 0 if len(valves) == 1 else dmap[f"{p}_{valves[1]}"]
    new_tick = start_tick - p_open_penality - p_dist_penality
    value_rest = compute_preasure(valves[1:], new_tick)
    if value_rest == -1:
        return -1
    return value_0 + value_rest

positive_ps = [pk for pk, pv in pmap.items() if pv["rate"] != 0]
best_val = 0

results = defaultdict(lambda: 0)

candidates=[("AA",)]
for i in range(26):
    new_candidates=[]
    for c in candidates:
        for tile in positive_ps:
            if tile in c:
                continue
            temp_can = c + (tile, )
            temp_v = compute_preasure(temp_can, 26)

            if temp_v != -1:
                result_key = tuple(sorted(temp_can))
                if results[result_key] < temp_v:
                    results[result_key] = temp_v

                new_candidates.append(temp_can)
    candidates = new_candidates

positive_ps_set = set(positive_ps)
best_result = 0
for rk, rv in results.items():
    complementary_ks = positive_ps_set - set(rk)
    for i in range(1, len(complementary_ks)):
        for elephant_keys in itertools.combinations(complementary_ks, i):
            complementary_key = ("AA", ) + tuple(sorted(elephant_keys))
            if complementary_key in results:
                value = rv + results[complementary_key]
                if value > best_result:
                    best_result = value

print(best_result)