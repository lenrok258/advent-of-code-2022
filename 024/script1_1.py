from queue import PriorityQueue
from sys import argv
from tqdm import tqdm
from collections import defaultdict
import math

# test: 
# input: 205 too low

lines = open(argv[1], 'r').read().splitlines()

board = defaultdict(list)
board_w, board_h = None, None

directions = ((1, 0), (-1, 0), (0, -1), (0, 1)) # R, L, U, D

# load board
for y, l in enumerate(lines[1:]):
    for x, c in enumerate(l[1:-1]):
        c = c.replace(">", "0").replace("<", "1").replace("^", "2").replace("v", "3")
        if c == "." or c == '#':
            continue
        board[(x, y)].append(c)
        board_w = x + 1
    board_h = y


def print_board(board):
    for y in range(0, board_h):
        line = []
        for x in range(0, board_w):
            v = board[(x, y)]
            if len(v) == 1:
                v = v[0].replace("0", ">").replace("1", "<").replace("2", "^").replace("3", "v")
            v = "." if len(v) == 0 else v
            v = "2" if len(v) == 2 else v
            v = "3" if len(v) == 3 else v
            v = "4" if len(v) == 4 else v
            line.append(v)
        print(f"#{''.join(line)}#")
    print("")


def tick(board):
    new_board = defaultdict(list)
    for coor, plys in board.items():
        for p in plys:
            if p in ["0", "1", "2" , "3"]:
                dir = directions[int(p)]
                new_coor = ((coor[0] + dir[0]) % board_w, (coor[1] + dir[1]) % board_h)
                new_board[new_coor].append(p)                
    return new_board


# find a period
period = math.lcm(board_w, board_h)
print(f"Period = {period}")

# generate all possible board states
states = dict()
for i in range(period):
    print(f"Generating state {i}")
    states[i] = board
    board = tick(board)

start_point, end_point = (0, -1), (board_w - 1, board_h)

def next_nodes(board, coor):

    global end_point

    next_nodes = [] 
    if len(board[coor]) == 0:
        next_nodes.append(coor)
    for d in directions:
        new_coor = (coor[0] + d[0], coor[1] + d[1])
        if new_coor[0] < 0 or new_coor[0] >= board_w:
            continue
        if (new_coor[1] < 0 or new_coor[1] >= board_h) and new_coor != end_point:
            continue
        if len(board[new_coor]) != 0:
            continue
        next_nodes.append(new_coor)
    return next_nodes

# BFS
def bfs(start_coor, end_coor, states):

    global period

    curr_state = 0

    queue = []
    visited = set()

    queue.append((start_coor, 0))
    visited.add((start_coor, 0))

    while True:
        c_coor, c_state = queue.pop(0)
        next_state = (c_state + 1)

        if c_coor == end_coor:
            print(f"{c_coor}")
            return c_state

        c_kids = next_nodes(states[next_state % period], c_coor)
        for c_k_coor in c_kids:
            c_k_node = (c_k_coor, next_state)
            
            if (c_k_coor, next_state % period) in visited:
                continue

            queue.append(c_k_node)
            visited.add(c_k_node)


t = bfs(start_point, end_point, states)
print(t)

# board = tick(board)
# board = tick(board)
# p = (0,0)
# print_board(board)
# print(board[p])
# print(next_nodes(board, p))

