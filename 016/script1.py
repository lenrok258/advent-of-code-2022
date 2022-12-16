from sys import argv
import re

# test: 
# input: 

lines = open(argv[1], 'r').read().splitlines()
pipes = [re.search("Valve (\w+)", l) for l in lines]
 
for p in pipes:
    print(p)