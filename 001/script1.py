# test: 
# input: 

lines = open('input.txt', 'r').read().splitlines()

current_elf_kcal = 0
max_cal = 0
for l in lines:
    if not l:
        if current_elf_kcal > max_cal:
            max_cal = current_elf_kcal
        current_elf_kcal = 0
    else:
        current_elf_kcal += int(l)

print(max_cal)
