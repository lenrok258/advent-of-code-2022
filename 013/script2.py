from sys import argv
from functools import cmp_to_key

# test: 
# input: 19716

lines = open(argv[1], 'r').read().replace("\n\n", "\n").splitlines()
lines.append("[[2]]")
lines.append("[[6]]")

exprs = [eval(v) for v in lines]

def is_order_correct(lhs, rhs):
    # both ints
    if isinstance(lhs, int) and isinstance(rhs, int):
        if lhs != rhs:
            return -1 if lhs < rhs else 1
        return None
    
    # one int - just convert to list
    if isinstance(lhs, int) != isinstance(rhs, int):
        if isinstance(lhs, int):
            lhs = [lhs]
        elif isinstance(rhs, int):
            rhs = [rhs]
    
    for li, lv in enumerate(lhs):
        # no more values in rhs
        if len(rhs) <= li:
            return 1
        
        # compare values
        result = is_order_correct(lv, rhs[li])
        if result is None:
            continue
        else:
            return result

    # compare sized
    if len(lhs) != len(rhs):
        return -1 if len(lhs) < len(rhs) else 1

    return None

comparator = cmp_to_key(is_order_correct)
exprs_sorted = sorted(exprs, key=comparator)

indices = []
for i, v in enumerate(exprs_sorted):
    if str(v) == "[[2]]" or str(v) == "[[6]]":
        indices.append(i + 1)
    print(v)

print(indices[0] * indices[1])
