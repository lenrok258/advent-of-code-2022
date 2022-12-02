# test: 
# input: 15572

lines = open('input.txt', 'r').read().splitlines()

score = 0
for l in lines:
    oponent, me = l.split(' ')
    print(f"{oponent}, {me}")
    if me == 'X': 
        score += 1
        if oponent == 'C':
            score += 6
        if oponent == 'A':
            score += 3
    if me == 'Y': 
        score += 2
        if oponent == 'A':
            score += 6
        if oponent == 'B':
            score += 3
    if me == 'Z': 
        score += 3
        if oponent == 'B':
            score += 6
        if oponent == 'C':
            score += 3
    
print(score)
