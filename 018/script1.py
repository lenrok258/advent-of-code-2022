from sys import argv

# test: 64
# input: 3586

lines = open(argv[1], 'r').read().splitlines()
cubes = [tuple([int(a) for a in l.split(",")]) for l in lines]
cube_sides = [(0,0,1), (0,1,0), (1,0,0), (0,0,-1), (0,-1,0), (-1,0,0)]
obsidian = {c:True for c in cubes}

exposed_sides = 0
for c in obsidian.keys():
    for s in cube_sides:
        neighbor_candidate = (c[0] + s[0], c[1] + s[1], c[2] + s[2]) 
        if neighbor_candidate not in obsidian:
            exposed_sides += 1

print(exposed_sides)
