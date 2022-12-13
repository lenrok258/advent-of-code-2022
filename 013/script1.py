from sys import argv

# test: 
# input: 6656

i_pairs = open(argv[1], 'r').read().split("\n\n")

def is_order_correct(lhs, rhs):
    # both ints
    if isinstance(lhs, int) and isinstance(rhs, int):
        if lhs != rhs:
            return lhs < rhs
        return None
    
    # one int - convert to list
    if isinstance(lhs, int) != isinstance(rhs, int):
        print("\t Jeden int, drugi tablica, konwertuję")
        if isinstance(lhs, int):
            lhs = [lhs]
        elif isinstance(rhs, int):
            rhs = [rhs]
    
    for li, lv in enumerate(lhs):
        # no more values in rhs
        if len(rhs) <= li:
            return False
        
        # compare values
        result = is_order_correct(lv, rhs[li])
        if result is None:
            continue
        else:
            return result

    # compare size
    if len(lhs) != len(rhs):
        return len(lhs) < len(rhs)

    return None


result = list()
for i, p in enumerate(i_pairs):
    lhs, rhs = [eval(v) for v in  p.split("\n")]
    if is_order_correct(lhs, rhs):
        result.append(i + 1)
print(sum(result)) 
