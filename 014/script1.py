from sys import argv
import re

# test: 26
# input: 200 too low

lines = open(argv[1], 'r').read().splitlines()
lines = [re.split("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", l) for l in lines]

def distance(fromm, to):
    return abs(fromm[0] - to[0]) + abs(fromm[1] - to[1])

sensors = [((int(l[1]), int(l[2])), (int(l[3]), int(l[4]))) for l in lines]
sensors = [(s[0], s[1], distance(s[0], s[1])) for s in sensors]

for s in sensors:
    print(s)

def in_distance_of_any(p_coor, sensors):
    for s in sensors:
        s_coor = s[0]
        b_coor = s[1]
        s_dist = s[2]
        p_dist = distance(s_coor, p_coor)
        
        if p_coor == b_coor:
            return False

        if p_dist <= s_dist:
            return True
    return False

print(sensors)

x_from = min([s[0][0] - s[2] for s in sensors])
x_to = max([s[0][0] + s[2] for s in sensors])
print(f"from {x_from}, to {x_to}")

in_dist_count = 0
for x in range(x_from, x_to):
    if x % 100_000 == 0:
        print(x)
    if in_distance_of_any((x, 10), sensors):
        in_dist_count += 1
print(in_dist_count)
