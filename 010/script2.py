import math

# test: 
# input: 

lines = open('input.txt', 'r').read().splitlines()
instructions = [i.split(" ") for i in lines]

cycle = 1   # pixel currenty drawn
X = 1       # position of the middle of the sprite "▓▓▓"

instr_pointer = 0
instr_in_progress = False

signal_strengths = []
display = [['.' for _ in range(40)] for _ in range(6)]

while True:
    if instr_pointer == len(instructions):
        break
    instr = instructions[instr_pointer]

    display_row_nr = math.floor((cycle - 1) / 40)
    display_row = display[display_row_nr]
    pixel_being_drawn = (cycle - 1) % 40
    sprite_positions = [X-1, X, X+1]

    if pixel_being_drawn in sprite_positions:
        display_row[pixel_being_drawn] = "▓"

    if (cycle in [20, 60, 100, 140, 180, 220]):
        signal_strengths.append(X * cycle)

    instr_name = instr[0]
    if instr_name == "noop":    
        instr_pointer += 1
        cycle += 1
        continue
    elif instr_name == "addx":
        instr_in_progress = not instr_in_progress
        cycle += 1
        if instr_in_progress == False:
            instr_value = int(instr[1])
            X += instr_value
            instr_pointer += 1
        continue

for row in display:
    print("".join(row))
