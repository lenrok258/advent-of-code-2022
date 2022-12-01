# test: 
# input: 

lines = open('input.txt', 'r').read().splitlines()

current_elf_kcal = 0
elfs_cals = list()
for l in lines:
    if not l:
        elfs_cals.append(current_elf_kcal)
        current_elf_kcal = 0
    else:
        current_elf_kcal += int(l)

elfs_cals = sorted(elfs_cals)

print(elfs_cals[-1] + elfs_cals[-2] + elfs_cals[-3])
