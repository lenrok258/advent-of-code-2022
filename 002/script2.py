import re

# test: 
# input: 16098

lines = open('input.txt', 'r').read().splitlines()


def loose(oponent):
    if oponent == 1: return 3
    if oponent == 2: return 1
    if oponent == 3: return 2


def win(oponent):
    if oponent == 1: return 2
    if oponent == 2: return 3
    if oponent == 3: return 1


score = 0
for l in lines:
    l = re.sub("X|A", '1', l) # rock, loose
    l = re.sub("Y|B", '2', l) # paper, tie
    l = re.sub("Z|C", '3', l) # scissors, win

    oponent, result = map(int, l.split(' '))

    # loose
    if result == 1:
        score += loose(oponent)
    # tie
    if result == 2:
        score += (3 + oponent)
    # win
    if result == 3:
        score += (6 + win(oponent))
    

print(score)
