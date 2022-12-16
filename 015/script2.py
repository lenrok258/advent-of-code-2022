from sys import argv
import re

# test: 26
# input: 4724228

lines = open(argv[1], 'r').read().splitlines()
lines = [re.split("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", l) for l in lines]

def distance(fromm, to):
    return abs(fromm[0] - to[0]) + abs(fromm[1] - to[1])

sensors = [((int(l[1]), int(l[2])), (int(l[3]), int(l[4]))) for l in lines]
sensors = [(s[0], s[1], distance(s[0], s[1])) for s in sensors]

print("Sensors:")
for s in sensors:
    print(s)
print("====\n")

def not_in_distance(p_coor, sensors):
    for s in sensors:
        s_coor = s[0]
        b_coor = s[1]
        s_dist = s[2]
        p_dist = distance(s_coor, p_coor)
        
        # if s_coor == b_coor or p_coor == b_coor:
        #     return False

        if p_dist > s_dist:
            continue
        else:
            return False
    return True

# 1.  sx + sy - sd >  x + y
# 2.  sy - sx - sd >  y - x
# 3.  sx - sy - sd >  x - y
# 4.  sx + sy + sd <  x + y
b = [[] for _ in range(4)] 
for s in sensors:
    sx, sy, sd = s[0][0], s[0][1], s[2]
    b[0].append(sx + sy - sd)
    b[1].append(sy - sx - sd)
    b[2].append(sx - sy - sd)
    b[3].append(sx + sy + sd)

# test data result point: 14, 11
# print(f"1. {max(b[0])} >  x + y")
# print(f"2. {max(b[1])} >  y - x")
# print(f"3. {max(b[2])} >  x - y")
# print(f"4. {min(b[3])} <  x + y")
# print("========")

x, y = 14, 11
# print(f"{x} {y}")
# print(f"1. {max(b[0])} >  {x + y}")
# print(f"2. {max(b[1])} >  {y - x}")
# print(f"3. {max(b[2])} >  {x - y}")
# print(f"4. {min(b[3])} <  {x + y}")

# print(f"{max(b[0])} >  x + y, {max(b[1])} >  y - x, {max(b[2])} >  x - y, {min(b[3])} <  x + y, x > 0, y > 0")

equations = []
for s in sensors:
    sx, sy, sd = s[0][0], s[0][1], s[2]
    equations.append(f"|{sx} - x| + |{sy} - y| > {sd}")

# print(", ".join(equations))

boundries = [0, 4_000_000]
# candidates = set()
# for s in sensors:
#     print(f"sensor {s}")
#     sx, sy, r = s[0][0], s[0][1], s[2]+1

#     for x in range(sx + r, 0, -1):
#         for y in range(0, sy - r, -1):
#             if x >= boundries[0] and x <= boundries[1] and y >= boundries[0] and y <= boundries[1]:
#                 candidates.add((x,y))
    
#     for x in range(0 , sx - r, -1):
#         for y in range(sy - r, 0):
#             if x >= boundries[0] and x <= boundries[1] and y >= boundries[0] and y <= boundries[1]:
#                 candidates.add((x,y))
    
#     for x in range(sx - r, 0):
#         for y in range(0, sy + r):
#             if x >= boundries[0] and x <= boundries[1] and y >= boundries[0] and y <= boundries[1]:
#                 candidates.add((x,y))

#     for x in range(0, sx + r):
#         for y in range(sy + r, 0, -1):
#             if x >= boundries[0] and x <= boundries[1] and y >= boundries[0] and y <= boundries[1]:
#                 candidates.add((x,y))

# print(candidates)


candidates = set()

for s in sensors:
    print(f"sensor {s}")
    sx, sy, r = s[0][0], s[0][1], s[2]
    peaks = [(sx+r, sy), (sx, sy+r), (sx-r, sy), (sx, sy-r)]
    for p in peaks:
        for i in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x = p[0]+i[0]
            y = p[1]+i[1]
            if x >= boundries[0] and x <= boundries[1] and y >= boundries[0] and y <= boundries[1]:
                candidates.add((x, y))


for c in candidates:
    if not_in_distance(c, sensors):
        print(c)

