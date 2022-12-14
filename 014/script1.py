from collections import defaultdict
from sys import argv

# test: 
# input: 873

lines = [_.split(" -> " ) for _ in  open(argv[1], 'r').read().splitlines()]
rock_paths = [[[int(_) for _ in _.split(",")] for _ in l] for l in lines]

cave = dict()

for p in rock_paths:
    prv_r = p[0]
    for curr_r in p[1:]:
        if prv_r[0] != curr_r[0]:
            from_x, to_x = sorted([prv_r[0], curr_r[0]])
            y = prv_r[1]
            for x in range(from_x, to_x + 1):
                cave[(x, y)] = '#'
        if prv_r[1] != curr_r[1]:
            from_y, to_y = sorted([prv_r[1], curr_r[1]])
            x = prv_r[0]
            for y in range(from_y, to_y + 1):
                cave[(x, y)] = '#'
        prv_r = curr_r

rock_bottom = max([key[1] for key in cave.keys()])

def pour_sand(cave):
    grains = 0
    while True:
        s = (500, 0)
        while True:
            if s[1] > rock_bottom:
                return grains

            m_d = (s[0], s[1] + 1)
            m_l = (s[0] - 1, s[1] + 1)
            m_r = (s[0] + 1, s[1] + 1)

            if m_d not in cave:
                s = m_d
                continue
            if m_l not in cave:
                s = m_l
                continue
            if m_r not in cave:
                s = m_r
                continue

            cave[s] = "o"
            grains += 1
            break

print(pour_sand(cave))