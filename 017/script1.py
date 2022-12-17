from sys import argv
from collections import defaultdict

# test: 
# input: 3065

lines = open(argv[1], 'r').read().splitlines()
hot_gas = [int(i.replace("<", "-1").replace(">", "1")) for i in [c for c in lines[0]]]


def print_cave(cave, floor_y):
    for y in range(floor_y, 0, -1):
        line_vals = []
        line_vals.append("|")
        for x in range(1, 8):
            line_vals.append(cave[(x, y)])
        line_vals.append(f"| {y} {'--- !!!' if all([cave[(x, y)] == '#' for x in range(1, 8)]) else ''}")
        print("".join(line_vals))
    print("+" + "-"*7 + "+")
            

def next_rock(floor_y, rock_i):
    rocks_ascii = ["-", "+", "_|", "|", "o"]
    y = floor_y + 4
    # ----
    if rock_i == 0:
        return [(3, y), (4, y), (5, y), (6, y)]
    # +
    elif rock_i == 1:
        return [(4, y), (3, y+1), (4, y+1), (5, y+1), (4, y+2)]
    # _|
    elif rock_i == 2:
        return [(3, y), (4, y), (5, y), (5, y+1), (5, y+2)]
    # |
    elif rock_i == 3:
        return [(3, y), (3, y+1), (3, y+2), (3, y+3)]
    # o
    elif rock_i == 4:
        return [(3, y), (4, y), (3, y+1), (4, y+1)]        


def colision_detected(cave, rock):
    for (x, y) in rock:
        if x < 1 or x > 7:
            return True
        if y < 1:
            return True
        if cave[(x, y)] == "#":
            return True
    return False

def park_rock(cave, rock): 
    global hot_gas, gas_i

    while True:
        # hot gas 
        gas_x = hot_gas[gas_i]
        gas_i = (gas_i + 1) % len(hot_gas)
        rock_candidate = [(x + gas_x, y) for (x, y) in rock]
        if not colision_detected(cave, rock_candidate):
            rock = rock_candidate
        
        # gravitation
        rock_candidate = [(x, y - 1) for (x, y) in rock]
        if not colision_detected(cave, rock_candidate):
            rock = rock_candidate
            continue
        else:
            return rock
        

def add_rock(cave, rock):
    for r in rock:
        cave[r] = "#"


cave = defaultdict(lambda: '.')
floor_y = 0
rock_i = 0
gas_i = 0

for _ in range(2022):
    rock = next_rock(floor_y, rock_i)
    parked_rock = park_rock(cave, rock)
    floor_y = max(floor_y, max([c[1] for c in parked_rock]))
    add_rock(cave, parked_rock)
    rock_i = (rock_i + 1) % 5

print_cave(cave, floor_y+3)
print(floor_y)