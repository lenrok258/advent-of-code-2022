# test: 
# input: 6642

lines = open('input.txt', 'r').read().splitlines()

instructions = [line.split(" ") for line in lines]
moves_def = {"R":(1,0), "L":(-1, 0), "U":(0, 1), "D":(0, -1)}

coor_head, coor_tail = [0, 0], [0, 0]
tail_visited_coor = set([(0,0)])

magic_trans = {0:0, -2:-1, 2:1}
magic_trans2 = {-2:-1, 2:1, -1:-1, 1:1}

def follow_head(coor_head, coor_tail):
    delta_x = coor_head[0] - coor_tail[0]
    delta_y = coor_head[1] - coor_tail[1]

    new_coor_tail_x, new_coor_tail_y = coor_tail
    if (abs(delta_x) == 2 or abs(delta_y) == 2):
        if (delta_x == 0 or delta_y == 0):
            new_coor_tail_x += magic_trans[delta_x]
            new_coor_tail_y += magic_trans[delta_y]
        elif (abs(delta_x) + abs(delta_y) >= 3):
            new_coor_tail_x += magic_trans2[delta_x]
            new_coor_tail_y += magic_trans2[delta_y]
    return [new_coor_tail_x, new_coor_tail_y]


for instr in instructions:
    move_direction, move_steps = instr[0], int(instr[1])
    for step in range(0, move_steps):
        move_def =  moves_def[move_direction]
        coor_head[0] += move_def[0]
        coor_head[1] += move_def[1]

        coor_tail = follow_head(coor_head, coor_tail.copy())
        tail_visited_coor.add((coor_tail[0], coor_tail[1]))

print(len(tail_visited_coor))