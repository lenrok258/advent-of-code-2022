from sys import argv
from tqdm import tqdm
import re
import sys

# test: code not working with test data
# input: 95291

def next_coor_and_dir(curr_coor, curr_dir):
    global board

    candidate_coor = (curr_coor[0] + curr_dir[0], curr_coor[1] + curr_dir[1])
    candidate = (candidate_coor, curr_dir)

    # in the board
    if candidate_coor in board:
        return candidate

    # not in the board (see notes.txt)
    x, y = curr_coor
    
    # A 6->1
    if x == 49 and 150 <= y <= 199 and curr_dir == (1, 0):
        return ((50 + (y - 150), 149), (0, -1))
    # A 1->6
    if 50 <= x <= 99 and y == 149 and curr_dir == (0, 1):
        return ((49, 150 + (x - 50)), (-1, 0)) 

    # B 4->2
    if 100 <= x <= 149 and y == 49 and curr_dir == (0, 1):
        return ((99, 50 + (x - 100)), (-1, 0))
    # B 2->4
    if x == 99 and 50 <= y <= 99 and curr_dir == (1, 0):
        return ((100 + (y - 50), 49), (0, -1))

    # C 5->2
    if 0 <= x <= 49 and y == 100 and curr_dir == (0, -1):
        return ((50, 50 + x), (1, 0))
    # C 2->5
    if x == 50 and 50 <= y <= 99 and curr_dir == (-1, 0):
        return (((y - 50), 100), (0, 1))

    # D 3->6
    if 50 <= x <= 99 and y == 0 and curr_dir == (0, -1):
        return ((0, 150 + (x - 50)), (1, 0))
    # D 6->3
    if x == 0 and 150 <= y <= 199 and curr_dir == (-1, 0):
        return ((50 + (y - 150), 0), (0, 1))

    # E 4->6 
    if 100 <= x <= 149 and y == 0 and curr_dir == (0, -1):
        return ((x - 100, 199), (0, -1))
    # E 6->4
    if 0 <= x <= 49 and y == 199 and curr_dir == (0, 1):
        return ((100 + x, 0), (0, 1))

    # F 4->1 
    if x == 149 and (0 <= y <= 49) and curr_dir == (1, 0):
        return ((99, 100 + (49 - y)), (-1, 0))
    # F 1->4 
    if x == 99 and (100 <= y <= 149) and curr_dir == (1, 0):
        return ((149, (149 - y)), (-1, 0))

    # G 5->3
    if x == 0 and 100 <= y <= 149 and curr_dir == (-1, 0):
        return ((50, 149 - y), (1, 0))
    # G 3->5
    if x == 50 and 0 <= y <= 49 and curr_dir == (-1, 0):
        return ((0, 100 + (49 - y)), (1, 0))

    raise Exception(f"Unhandled coordinates = {curr_coor} and direction = {curr_dir}")

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

# directions
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

# load path 
path = re.split("(\d+)([RL]+)", path_raw)
path = [p for p in path if p]
path = [int(p) if re.match("\d+", p) else p for p in path]

# traversing path
curr_dir_i = 0
curr_dir = directions[curr_dir_i]
curr_pos = start_p
for i, p in enumerate(path):
    print(f"\nPath action={p}, curr_pos={curr_pos}, curr_dir={curr_dir}, curr_dir_i={curr_dir_i}")

    # walking
    if isinstance(p, int):
        for _ in range(p):
            nxt_pos_candidate, nxt_dir_candidate = next_coor_and_dir(curr_pos, curr_dir) 
            nxt_pos_can_val = board[nxt_pos_candidate]

            print(f"\tCandidate = {nxt_pos_candidate} {nxt_dir_candidate}")

            # blocked
            if nxt_pos_can_val == "#":
                print(f"\t\tCandidate rejected as {nxt_pos_candidate} is {nxt_pos_can_val}")
                break

            # accepted
            elif nxt_pos_can_val == ".":
                curr_pos = nxt_pos_candidate
                curr_dir = nxt_dir_candidate
                curr_dir_i = directions.index(curr_dir)
                print(f"\t\tCandidate accepted")
                continue
    
    # turning
    else:
        if p == "L":
            curr_dir_i = (curr_dir_i - 1) % 4
        elif p == "R":
            curr_dir_i = (curr_dir_i + 1) % 4
        
        curr_dir = directions[curr_dir_i]

print(f"Result = {(curr_pos[1]+1)*1000 + (curr_pos[0]+1)*4 + curr_dir_i}")