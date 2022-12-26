from sys import argv
from tqdm import tqdm
from collections import defaultdict
from collections import Counter

# test: 
# input: 

lines = open(argv[1], 'r').read().splitlines()

mapp = dict()
for y, l in enumerate(lines):
    for x, c in enumerate(l):
        if c == "#":
            mapp[(x, y)] = True

def bbox(mmap):
    min_x, min_y, max_x, max_y = 100000, 100000, -100000, -100000
    for p in mmap.keys():
        min_x = p[0] if p[0] < min_x else min_x
        max_x = p[0] if p[0] > max_x else max_x
        min_y = p[1] if p[1] < min_y else min_y
        max_y = p[1] if p[1] > max_y else max_y
    return ((min_x, min_y), (max_x, max_y))


def print_mapp(mapp):
    bb = bbox(mapp)
    bb = ((-3,-2), (10, 9))
    print("3210123456789")
    for y in range(bb[0][1], bb[1][1]+1):
        line = []
        for x in range(bb[0][0], bb[1][0]+1):
            line.append("#" if (x, y) in mapp else ".")
        print("".join(line))
    print()


directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
diagonals = {
        (0, -1) :[(-1, -1), (1, -1)],
        (0,  1) :[(-1, 1), (1, 1)],
        (-1, 0) :[(-1, -1), (-1, 1)],
        (1,  0) :[(1, 1), (1, -1)],
}
around = []
around.extend(directions)
around.extend(diagonals[(1, 0)])
around.extend(diagonals[(-1, 0)])

curr_dir_i = 0

def around_coor(elf):
    return [(elf[0] + a[0], elf[1] + a[1]) for a in around]


def round(mapp, curr_dir_i):
    global directions

    proposals = {}
    destination_counter = Counter()

    # proposals
    for elf in mapp:
        
        # empty around
        if all([a not in mapp for a in  around_coor(elf)]):
            continue

        # looking around + proposals
        for d in range(curr_dir_i, curr_dir_i + 4):
            d = d%4
            mods = [directions[d]] + diagonals[directions[d]]
            pts = [(elf[0] + m[0], elf[1] + m[1]) for m in mods]
            if all([p not in mapp for p in pts]):
                destination = (elf[0] + directions[d][0], elf[1] + directions[d][1])
                proposals[elf] = destination
                destination_counter[destination] += 1
                break
                
    # movements
    new_mapp = dict()
    for elf in mapp:
        if elf not in proposals:
            new_mapp[elf] = True
            continue
        elif elf in proposals:
            prop_dest = proposals[elf]
            if destination_counter[prop_dest] == 1:
                new_mapp[prop_dest] = True
                continue
            else:
                new_mapp[elf] = True
            
    return new_mapp


print_mapp(mapp)
for _ in range(10):
    print(f"Round {_+1}")
    mapp = round(mapp, curr_dir_i)
    curr_dir_i = (curr_dir_i + 1) % 4
    print_mapp(mapp)


bbb = bbox(mapp)
a = 0
for y in range(bbb[0][1], bbb[1][1]+1):
    for x in range(bbb[0][0], bbb[1][0]+1):
        if (x,y) not in mapp:
            a += 1

print(a)