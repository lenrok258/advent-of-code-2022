# test: 
# input: 

lines = open('input.txt', 'r').read().splitlines()

forest = [[int(tree) for tree in row] for row in lines]

def is_visible(forest, x, y):
    h = forest[x][y]
    for i in range(x-1, -2, -1):
        if i == -1:
            return True 
        if forest[i][y] >= h:
            break
    for i in range(x+1, len(forest)+1, 1):
        if i == len(forest):
            return True 
        if forest[i][y] >= h:
            break
    for i in range(y-1, -2, -1):
        if i == -1:
            return True 
        if forest[x][i] >= h:
            break
    for i in range(y+1, len(forest[0])+1, 1):
        if i == len(forest):
            return True 
        if forest[x][i] >= h:
            break       
    return False


count = 0
for x in range(0, len(forest)):
    for y in range(0, len(forest[0])):
        h = forest[x][y]
        visible = is_visible(forest, x, y)
        if visible: count += 1

print(count)

