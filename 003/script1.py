# test: 
# input: 8394

lines = open('input.txt', 'r').read().splitlines()

duplicates_list = list()
for backpack in lines:
    bp_size = len(backpack)
    bp_half_i = int(bp_size/2)
    compartment_1, compartment_2 = backpack[0:bp_half_i], backpack[bp_half_i:bp_size]

    duplicate = None
    for item_1 in compartment_1:
        for item_2 in compartment_2:
            if item_1 == item_2:
                duplicate = item_1
    duplicates_list.append(duplicate)

sum = 0
for d in duplicates_list:
    if d.isupper():
        sum += ord(d) - 38
    else:
        sum += ord(d) - 96

print(sum)
