# test: 
# input: 

lines = open('input.txt', 'r').read().splitlines()
instructions = [i.split(" ") for i in lines]

cycle, X = 1

instr_pointer = 0
instr_in_progress = False

signal_strengths = []

while True:
    if instr_pointer == len(instructions):
        break
    instr = instructions[instr_pointer]

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

print(sum(signal_strengths))