# test: 
# input: 534

lines = open('input.txt', 'r').read().splitlines()

counter = 0
for l in lines:
    sections = list(map(lambda a: a.split("-"), l.split(",")))
    e1_1, e1_2, e2_1, e2_2 = int(sections[0][0]), int(sections[0][1]), int(sections[1][0]), int(sections[1][1])

    if (e1_1 >= e2_1 and e1_2 <= e2_2) or (e1_1 <= e2_1 and e1_2 >= e2_2):
        counter += 1

print(counter)