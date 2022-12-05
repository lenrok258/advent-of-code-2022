from collections import deque
import re

# test: 
# input: QNHWJVJZW

input_sections = open('input.txt', 'r').read().split("\n\n")

input_stacks = input_sections[0].split("\n")[0:-1]
input_nr_of_stacks = int(input_sections[0].split("\n")[-1].strip()[-1])
input_instructions = input_sections[1].split("\n")

stacks = [deque() for i in [0]*input_nr_of_stacks]
instructions = [re.split(" from | to ", i.replace("move ", "")) for i in input_instructions]

for i_s in input_stacks:
    for i in range(0, input_nr_of_stacks):
        input_idx = i * 4 + 1
        val = i_s[input_idx]
        if val != ' ': 
            stacks[i].appendleft(val)

for i in instructions:
    how_many, fromm, to = map(int, i)
    for j in range(0, how_many):
        val = stacks[fromm-1].pop()
        stacks[to-1].append(val)

result = ("".join([x.pop() for x in stacks]))
print(result)