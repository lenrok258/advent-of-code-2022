from sys import argv
import re
from queue import PriorityQueue
import itertools
from functools import lru_cache

# test: 
# input: 1762, 1842, 1858 too low, incorrect: 1936, candidate: 

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

print("PIPES map")
for p in pmap.items():
    print(f"\t{p}")
print("\n")

# ################################
# DISTANCES

dmap = {}
for pk_from, pv_from in pmap.items():
    for pk_to, pv_to in pmap.items():
        dist = dijkstra(lambda p:pmap[p]["tunels"], pk_from, pk_to)
        dmap[pk_from + "_" + pk_to] = dist

print("DISTANCES map")
print(f"\t{dmap}")
print("\n")

# ############################################################################################################

def where_to_go_next(curr_node, pmap, dmap, tick):
    # if curr_node == "AA": return (["DD"], 10)
    # if curr_node == "DD": return (["BB"], 10)
    # if curr_node == "BB": return (["JJ"], 10)
    # if curr_node == "JJ": return (["HH"], 10)
    # if curr_node == "HH": return (["EE"], 10)
    # if curr_node == "EE": return (["CC"], 10)

    best_value = -1000000000000
    best_ps = []

    # compute best value
    for pk, pv in pmap.items():
        if pv["open"]==True or pv["rate"] == 0:
            continue
        value = (tick - dmap[f"{curr_node}_{pk}"]) * pv["rate"]
        if value >= best_value:
            best_value = value

    # list valves with best value
    for pk, pv in pmap.items():
        if pv["open"]==True:
            continue
        value = (tick - dmap[f"{curr_node}_{pk}"]) * pv["rate"]
        if value == best_value:
            best_ps.append(pk)

    return (best_ps, best_value)

curr_node = "AA"
pmap["AA"]["open"] = True # to skip it as it's blocked
tick = 30
flow_result = 0
while True:
    if tick <= 0:
        break

    where_result = where_to_go_next(curr_node, pmap, dmap, tick)
    where_nodes, where_val = where_result
    
    if not where_nodes:
        break

    where_n = where_nodes[0] # need to decide which to choose or brute force
    pmap[where_n]["open"] = True

    tick = tick - (dmap[f"{curr_node}_{where_n}"] + 1)
    flow_n = pmap[where_n]["rate"]
    flow_result += tick*flow_n
    print(f"tick {tick}, flow {flow_n}*{tick}={flow_n*tick}")

    print(f"\t{curr_node} -> {where_nodes} {where_val}")
    curr_node = where_n

print("PIPES map")
for p in pmap.items():
    print(f"\t{p}")
print("\n")

print(flow_result)

print("==============\n\n")

# ############################################################################################################

# For input it's = 15!~10e12 permutations
# positive_ps = [pk for pk, pv in pmap.items() if pv["rate"] != 0]
# print(len(positive_ps))
# all_combinatios = list(itertools.permutations(positive_ps))
# print(len(set(all_combinatios)))

# if ("DD", "BB", "JJ", "HH", "EE", "CC") in all_combinatios:
#     print(True)

# for i, p in enumerate(itertools.permutations(positive_ps)):
#     if i%100_00_000 == 0:
#         print(i)

# ==========================


@lru_cache(maxsize=None)
def compute_value(valves, start_tick):

    # print(f"\n*** compute_value {valves}, {start_tick}\n\n")

    if len(valves) == 0:
        return 0

    if start_tick <= 0:
        return -1

    # if (valves, start_tick) in cache:
    #     return cache[(valves, start_tick)]

    # compute cost for valve[0]
    p = valves[0]
    p_rate = pmap[p]["rate"]
    p_open_penality = 0 if p_rate == 0 else 1
    value_0 = p_rate * (start_tick - p_open_penality)

    # compute cost for vales[1:] and cache it
    p_dist_penality = 0 if len(valves) == 1 else dmap[f"{p}_{valves[1]}"]
    # print(f"val:{p} p_dist_penality:{p_dist_penality}")
    new_tick = start_tick - p_open_penality - p_dist_penality
    value_rest = compute_value(valves[1:], new_tick)
    if value_rest == -1:
        return -1
    # cache[(valves[1:], new_tick)] = value_rest

    # print(f"{valves}\ttick:{start_tick}\tvalue:{value_0} + {value_rest}")
    return value_0 + value_rest

    # while True:
    #     if tick <= 0:
    #         return 0

    #     where_result = where_to_go_next(curr_node, pmap, dmap, tick)
    #     where_nodes, where_val = where_result
        
    #     if not where_nodes:
    #         break

    #     where_n = where_nodes[0] # need to decide which to choose or brute force
    #     pmap[where_n]["open"] = True

    #     tick = tick - (dmap[f"{curr_node}_{where_n}"] + 1)
    #     flow_n = pmap[where_n]["rate"]
    #     flow_result += tick*flow_n
    #     print(f"tick {tick}, flow {flow_n}*{tick}={flow_n*tick}")

    #     print(f"\t{curr_node} -> {where_nodes} {where_val}")
    #     curr_node = where_n


positive_ps = [pk for pk, pv in pmap.items() if pv["rate"] != 0]
best_val = 0
# for i, p in enumerate(itertools.permutations(positive_ps)):
#     valves = ("AA",) + p
#     val = compute_value(valves, 30)
#     print(f"{val} {valves}")
#     if val > best_val:
#         best_val = val
#         print(f"{val} {valves}")
#     if i%100_000 == 0:
#         print(i)
    

# print(compute_value(("AA", "DD", "BB", "JJ", "HH", "EE", "CC"), 30))

positive_ps_pairs = list(itertools.permutations(positive_ps, 2))

print(positive_ps_pairs)

compute1, compute2 = True, True

candidates=[(("AA","AA"),)]
for i in range(15):
    new_candidates=[]
    for c in candidates:
        used_valves = set([item for sublist in c for item in sublist])
        for tile_pair in positive_ps_pairs:

            if tile_pair[0] in used_valves:
                continue
            if tile_pair[1] in used_valves:
                continue

            temp_can = c + (tile_pair, )
            # print(temp_can)
            temp_v_1 = compute_value(tuple([v[0] for v in temp_can]), 26)
            temp_v_2 = compute_value(tuple([v[1] for v in temp_can]), 26)
            if temp_v_1 + temp_v_2 > best_val:
                best_val = temp_v_1 + temp_v_2
                print(f"{temp_v_1} + {temp_v_2} = {temp_v_1 + temp_v_2} {temp_can}")
                # print(f"{used_valves}")
            
            if temp_v_1 != -1 or temp_v_2 != -1:
            
                if temp_v_1 == -1:
                    compute1 = False
                    compute1_last_value = compute_value(tuple([v[0] for v in temp_can[:-1]]), 26)
                if temp_v_2 == -1:
                    compute2 = False
                    compute2_last_value = compute_value(tuple([v[1] for v in temp_can[:-1]]), 26)
            
                print(f"{temp_v_1} {temp_v_2}")
                new_candidates.append(temp_can)
             # print(temp_can)
    candidates = new_candidates

# print(best_val)