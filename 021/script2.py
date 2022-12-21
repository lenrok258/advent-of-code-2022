from sys import argv
from tqdm import tqdm
import re

# test: 
# input: 

lines = open(argv[1], 'r').read().splitlines()

m_raw = [re.split("(\w*): (\w*|\d*) ?(.)? ?(\w*)?", m) for m in lines]
monekys = [(m[1], int(m[2]), None, None) for m in m_raw if not m[3]]
monekys.extend([(m[1], m[2], m[3], m[4]) for m in m_raw if m[3]])

# name => (0:digit/name, 1:operator, 2:name)
mmap = {m[0]:(m[1], m[2], m[3]) for m in monekys}

mmap["humn"] = ("x", None, None, None)

# for m in mmap.items():
#     print(m)


def resolve(mmap, node_name):

    node = mmap[node_name]

    # digit node
    if not node[1]:
        return node[0]
    
    # equation node
    lhs = resolve(mmap, node[0])
    operator = node[1]
    rhs = resolve(mmap, node[2])

    if isinstance(lhs, int) and isinstance(rhs, int):
        return int(eval(f"{lhs} {operator} {rhs}"))
    else:
        return f"({lhs}{operator}{rhs})"


root_lhs = mmap["root"][0]
root_rhs = mmap["root"][2]

r1 = resolve(mmap, root_lhs)
r2 = resolve(mmap, root_rhs)
print(f"equasion: {r1} = {r2}")