from sys import argv
from tqdm import tqdm
import re
from collections import defaultdict
from functools import lru_cache

# test: 1*9, 2*12 = 33
# input: 1294

lines = open(argv[1], 'r').read().splitlines()

blueprints = [re.split("Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.", l) for l in lines]
blueprints = [( (int(b[2]),), (int(b[3]),), (int(b[4]), int(b[5]),), (int(b[6]), int(b[7]),) ) for b in blueprints]

# BLUEPRINTS and ROBOTS indices:
# 0 (ore robot): (ore,)
# 1 (clay robot): (ore,)
# 2 (obsidian robot): (ore, clay,)
# 3 (geode robot): (ore, obsidian,)

# RESOURCES indices:
# 0-ore, 1-clay, 2-obsidian, 3-geode

# actions = {
#     0: "nothing", 
#     1: "create_ore_robo", 
#     2: "create_clay_robo", 
#     3: "create_obsidian_robo", 
#     4: "create_geode_robo"
# }

def valid_actions(bprint_nr, res, robos, minute):
    # test = [0,0,2,0,2,0,2,0,0,0,3,2,0,0,3,0,0,4,0,0,4,0,0,0]
    # return [test[minute]]

    global max_robos_needed

    actions = [0, ]
    bp = blueprints[bprint_nr]

    # if you have enought res to produce geo robo every turn, do not build any other robots
    if bp[3][0] <= robos[0] and bp[3][1] <= robos[2]:
        if bp[3][0] <= res[0] and bp[3][1] <= res[2]:
            return [4]
        else:
            return [0]

    # probably not true - if able to build geode robot - always do
    if bp[3][0] <= res[0] and bp[3][1] <= res[2]:
        return [4]

    # in 23 minute, even if we create a roto it will not produce anything 
    if minute == 23:
        return [0]

    # in 22 minute, only building geode robo makes sense
    if minute == 22:
        if bp[3][0] <= res[0] and bp[3][1] <= res[2]:
            actions.append(4)
        return actions

    if bp[0][0] <= res[0]:
        if robos[0] < max_robos_needed[0]:
            actions.append(1)
    if bp[1][0] <= res[0]:  
        if robos[1] < max_robos_needed[1]:    
            actions.append(2)
    if bp[2][0] <= res[0] and bp[2][1] <= res[1]:
        if robos[2] < max_robos_needed[2]:    
            actions.append(3)
    if bp[3][0] <= res[0] and bp[3][1] <= res[2]:
        actions.append(4)
    return actions

# iii = 0
# actions_histogram = [0,0,0,0,0,0]
# def search(bp_nr, start_minute, start_robos, start_res):

#     geode_max = 0
#     queue = [(start_minute, start_robos, start_res)]
#     bp = blueprints[bp_nr]

#     max_ore_robo_needed = max(bp[0][0], bp[1][0], bp[2][0], bp[3][0])
#     max_clay_robo_needed = bp[2][1]
#     max_obsidian_robo_needed = bp[3][1]
#     max_robos_needed = (max_ore_robo_needed, max_clay_robo_needed, max_obsidian_robo_needed)
#     print(max_robos_needed)

#     # visited = set()
    
#     print(f"Blueprint {bp_nr}, {bp}")

#     while True:

#         # DEBUG STATS
#         global iii
#         iii += 1
#         if iii % 1_000_000 == 0:
#             actions_sum = sum(actions_histogram)
#             print(f"{iii}: geomax={geode_max}, actions histo={[int(i/actions_sum*100) for i in actions_histogram]})")
        

#         # if iii > 100:
#             # break

#         if not queue:
#             print("\tTime's up")
#             return geode_max

#         state = queue.pop()
#         minute, robos, res = state

#         if minute >= 24:
#             continue

#         actions = valid_actions(bp_nr, res, robos, minute, max_robos_needed)

#         # print(f"{bp_nr} clockmins={minute} robos={robos} res={res}")

#         # time flies by
#         minute += 1

#         # robots produce resources here
#         for i in range(4):
#             res[i] += robos[i]

#         if res[3] > geode_max:
#             geode_max = res[3]

#         for a in actions:
#             actions_histogram[len(actions)] += 1

#             robos_copy = robos.copy()
#             res_copy = res.copy()
#             if a == 0:
#                 queue.append((minute, robos_copy, res_copy))
#             elif a == 1:
#                 robos_copy[0] += 1
#                 ore_robo_cost_ore = bp[0][0]
#                 res_copy[0] -= ore_robo_cost_ore
#                 queue.append((minute, robos_copy, res_copy))
#             elif a == 2:
#                 robos_copy[1] += 1
#                 clay_robo_cost_ore = bp[1][0]
#                 res_copy[0] -= clay_robo_cost_ore
#                 queue.append((minute, robos_copy, res_copy))
#             elif a == 3:
#                 robos_copy[2] += 1
#                 obsidian_robo_cost_ore = bp[2][0]
#                 obsidian_robo_cost_clay = bp[2][1]
#                 res_copy[0] -= obsidian_robo_cost_ore
#                 res_copy[1] -= obsidian_robo_cost_clay
#                 queue.append((minute, robos_copy, res_copy))
#             elif a == 4:
#                 robos_copy[3] += 1
#                 geode_robo_cost_ore = bp[3][0]
#                 geode_robo_cost_obsidian = bp[3][1]
#                 res_copy[0] -= geode_robo_cost_ore
#                 res_copy[2] -= geode_robo_cost_obsidian
#                 queue.append((minute, robos_copy, res_copy))

#             # if res_copy[0] < 0 or res_copy[1] < 0 or res_copy[2] < 0 or res_copy[3] < 0:
#             #     print("error 1")
#             #     return -1

iii = 0
actions_histogram = [0,0,0,0,0,0]
geode_max = 0

@lru_cache(maxsize=None)
def search_recursive(bp_nr, minute, robos, res):

    # DEBUG STATS
    global iii 
    global geode_max
    iii += 1
    # if iii % 1_000_000 == 0:
        # actions_sum = sum(actions_histogram)
        # print(f"{iii}: geomax = {geode_max} actions histo={[int(i/actions_sum*100) for i in actions_histogram]})")

    # print(f"{bp_nr} clockmins={minute} robos={robos} res={res}")

    mins_left = (24 - minute)
    geo_potential = res[3] + (mins_left * robos[3]) + ((mins_left/2)*(mins_left-1))
    if geo_potential < geode_max:
        return res[3]

    if minute == 24:
        if geode_max < res[3]:
            geode_max = res[3]
            print(geode_max)
        return res[3]

    bp = blueprints[bp_nr]

    robos_2 = list(robos)
    res_2 = list(res)

    actions = valid_actions(bp_nr, res, robos, minute)

    # robots produce resources here
    for i in range(4):
        res_2[i] += robos_2[i]

    sub_results = []
    for a in actions:
        # actions_histogram[len(actions)] += 1

        robos_copy = list(robos_2)
        res_copy = list(res_2)
        if a == 0:
            pass
        elif a == 1:
            robos_copy[0] += 1
            ore_robo_cost_ore = bp[0][0]
            res_copy[0] -= ore_robo_cost_ore
        elif a == 2:
            robos_copy[1] += 1
            clay_robo_cost_ore = bp[1][0]
            res_copy[0] -= clay_robo_cost_ore
        elif a == 3:
            robos_copy[2] += 1
            obsidian_robo_cost_ore = bp[2][0]
            obsidian_robo_cost_clay = bp[2][1]
            res_copy[0] -= obsidian_robo_cost_ore
            res_copy[1] -= obsidian_robo_cost_clay
        elif a == 4:
            robos_copy[3] += 1
            geode_robo_cost_ore = bp[3][0]
            geode_robo_cost_obsidian = bp[3][1]
            res_copy[0] -= geode_robo_cost_ore
            res_copy[2] -= geode_robo_cost_obsidian
        
        sub_r = search_recursive(bp_nr, minute+1, tuple(robos_copy), tuple(res_copy))
        sub_results.append(sub_r)
    return max(sub_results)

geo_max_all = []
for i, b in enumerate(blueprints):

    print(f"Blueprint {i+1}, {b}")
    iii = 0

    bp = blueprints[i]
    max_ore_robo_needed = max(bp[0][0], bp[1][0], bp[2][0], bp[3][0])
    max_clay_robo_needed = bp[2][1]
    max_obsidian_robo_needed = bp[3][1]
    max_robos_needed = (max_ore_robo_needed, max_clay_robo_needed, max_obsidian_robo_needed)

    print(f"max_robos_needed={max_robos_needed}")
    result = search_recursive(i, 0, (1,0,0,0), (0,0,0,0))
    print(f"blueprint {i} {result}")
    geo_max_all.append(result)

    geode_max = 0

    print(f"Numer of search_recursive calls = {iii}")
    
    print(f"Cache stats {search_recursive.cache_info()}")
    search_recursive.cache_clear() 

print(sum([(i+1)*g for i, g in enumerate(geo_max_all)]))