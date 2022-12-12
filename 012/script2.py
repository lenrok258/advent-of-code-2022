from sys import argv
from queue import PriorityQueue
from collections import defaultdict

# test: 29
# input: 377

lines = open(argv[1], 'r').read().splitlines()
mapp = [[c for c in l] for l in lines] 

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def find_coor_all(mapp, char_to_find):
    result = []
    for y, yv in enumerate(mapp):
        for x, xv in enumerate(yv):
            if xv == char_to_find:
                result.append((x, y))
    return result

def possible_moves(mapp, coor):
    here_x, here_y = coor
    moves = []
    for m in directions:
        new_x, new_y = here_x + m[0], here_y + m[1]

        # mapp boundries
        if new_x < 0 or new_x >= len(mapp[0]) or new_y < 0 or new_y >= len(mapp):
            continue

        # max 1 up
        if ord(mapp[new_y][new_x]) - ord(mapp[here_y][here_x]) > 1:
            continue

        moves.append((new_x, new_y))
    return moves

def dijkstra(mapp, start_coor, end_coor):
    pq = PriorityQueue()
    pq.put((0, start_coor))
    visited = set(start_coor)
    while True:
        curr_cost, curr_point = pq.get()

        if curr_point == end_coor:
            return curr_cost
        
        ns = possible_moves(mapp, curr_point)
        for n in ns:
            if n not in visited:
                n_cost = 1
                pq.put((curr_cost + n_cost, n))
                visited.add(n)
        if pq.empty():
            return 9999999999

start_coor = find_coor_all(mapp, 'S')[0]
mapp[start_coor[1]][start_coor[0]] = 'a'

end_coor = find_coor_all(mapp, 'E')[0]
mapp[end_coor[1]][end_coor[0]] = 'z'

paths = [dijkstra(mapp, s, end_coor) for s in find_coor_all(mapp, 'a')]
print(min(paths))