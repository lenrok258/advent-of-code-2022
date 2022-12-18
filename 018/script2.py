from sys import argv
from functools import lru_cache

# test: 58
# input: 2072 (<2s)

lines = open(argv[1], 'r').read().splitlines()
cubes = [tuple([int(a) for a in l.split(",")]) for l in lines]
cube_sides = [(0,0,1), (0,1,0), (1,0,0), (0,0,-1), (0,-1,0), (-1,0,0)]
obsidian = {c:True for c in cubes}

# obsidian bounding box
cubes_xs, cubes_ys, cubes_zs = [c[0] for c in cubes], [c[1] for c in cubes], [c[2] for c in cubes]
bbox = ((min(cubes_xs), min(cubes_ys), min(cubes_zs)), (max(cubes_xs), max(cubes_ys), max(cubes_zs)))

def empty_negihbors(c, obsidian):
    result = []
    for s in cube_sides:
        candidate =(c[0] + s[0], c[1] + s[1], c[2] + s[2])
        if candidate not in obsidian:
            result.append(candidate)
    return result

# check if it is posible to move from given point to the outside of the bounding box
# if so - water and steam are able to get to this point
# Recusion would be faster executiontime-wise
@lru_cache(maxsize=None)
def available_path_beyond_bbox(coor):
    global obsidian, bbox
    queue, visited = [coor], set()
    while True:
        if not queue:
            return False
        
        c = queue.pop(0) # BFS vs DFS - does not mattter
        if c[0] < bbox[0][0] or c[1] < bbox[0][1] or c[2] < bbox[0][2] \
            or c[0] > bbox[1][0] or c[1] > bbox[1][1] or c[2] > bbox[1][2]:
            return True
        
        ens = empty_negihbors(c, obsidian)
        for en in ens:
            if en not in visited:
                queue.append(en)
                visited.add(en)

# compute exposed sides
exposed_sides = 0
for c in obsidian.keys():
    exposed_ns = [n for n in empty_negihbors(c, obsidian) if available_path_beyond_bbox(n)]
    exposed_sides += len(exposed_ns)

print(exposed_sides)