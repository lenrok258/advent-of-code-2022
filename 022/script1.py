from sys import argv
from tqdm import tqdm
import re

# test: 
# input: 67390

def next_coor(curr_coor, curr_dir):
    global board

    next_coor = (curr_coor[0] + curr_dir[0], curr_coor[1] + curr_dir[1]) 

    if next_coor not in board:
        tmp_dir = (curr_dir[0] * (-1), curr_dir[1] * (-1))
        tmp_nxt = curr_coor
        while True:
            tmp_nxt = (tmp_nxt[0] + tmp_dir[0], tmp_nxt[1] + tmp_dir[1]) 
            if tmp_nxt not in board:
                break
            else:
                next_coor = tmp_nxt

    return next_coor

board_raw, path_raw = open(argv[1], 'r').read().split("\n\n")

# load board
board = dict()
for y, l in enumerate(board_raw.splitlines()):
    for x, c in enumerate(l):
        if c != " ":
            board[(x, y)] = c


# find start point
start_p = (100000000000, 0)
for k in board.keys():
    if k[1] == 0 and k[0] < start_p[0]:
        start_p = k
print(f"Starting point = {start_p}")

# directions
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

# load path 
path = re.split("(\d+)([RL]+)", path_raw)
path = [p for p in path if p]
path = [int(p) if re.match("\d+", p) else p for p in path]
print(path)

# traversing path
curr_dir_i = 0
curr_dir = directions[curr_dir_i]
curr_pos = start_p
for p in path:
    print(f"\nPath action={p}, curr_pos={curr_pos}, curr_dir={curr_dir}")

    # walking
    if isinstance(p, int):
        for _ in range(p):
            nxt_pos_candidate = next_coor(curr_pos, curr_dir) 
            print(f"\tCandidate = {nxt_pos_candidate}")
            nxt_pos_can_val = board[nxt_pos_candidate]

            # blocked
            if nxt_pos_can_val == "#":
                print(f"\t\tCandidate rejected as {nxt_pos_candidate} is {nxt_pos_can_val}")
                break

            # accepted
            elif nxt_pos_can_val == ".":
                curr_pos = nxt_pos_candidate
                print(f"\t\tCandidate accepted")
                continue
    
    # turning
    else:
        if p == "L":
            curr_dir_i = (curr_dir_i - 1) % 4
        elif p == "R":
            curr_dir_i = (curr_dir_i + 1) % 4
        
        curr_dir = directions[curr_dir_i]
        print(f"\tcurr_dir changed to {curr_dir}")


print(f"\n\n Currpos={curr_pos}, currdir={curr_dir_i}")
print(f"Result = {(curr_pos[1]+1)*1000 + (curr_pos[0]+1)*4 + curr_dir_i}")