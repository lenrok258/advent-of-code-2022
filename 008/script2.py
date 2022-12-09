from functools import reduce

# test: 
# input: 

lines = open('input.txt', 'r').read().splitlines()

forest = [[int(tree) for tree in row] for row in lines]

def visible_trees_count(forest, x, y):
    counters = [0]*4
    h = forest[x][y]
    for i in range(x-1, -2, -1):
        if i == -1:
            break
        if forest[i][y] >= h:
            counters[0] += 1
            break
        counters[0] += 1
    for i in range(x+1, len(forest)+1, 1):
        if i == len(forest):
            break
        if forest[i][y] >= h:
            counters[1] += 1
            break
        counters[1] += 1
    for i in range(y-1, -2, -1):
        if i == -1:
            break
        if forest[x][i] >= h:
            counters[2] += 1
            break
        counters[2] += 1
    for i in range(y+1, len(forest[0])+1, 1):
        if i == len(forest):
            break
        if forest[x][i] >= h:
            counters[3] += 1
            break    
        counters[3] += 1
    
    return counters

scores = []
for x in range(0, len(forest)):
    for y in range(0, len(forest[0])):
        h = forest[x][y]
        counters = visible_trees_count(forest, x, y)
        score = reduce(lambda a, b: a*b, counters, 1)
        scores.append(score)

print(max(scores))

