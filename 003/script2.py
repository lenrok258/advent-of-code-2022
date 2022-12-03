
# test: 
# input: 2413

def divide_array(array, chunk_size):
    for i in range(0, len(array), chunk_size):
        yield array[i:i + chunk_size]


lines = open('input.txt', 'r').read().splitlines()
triples = list(divide_array(lines, 3))

duplicates_list = list()
for triple in triples:
    duplicate = None
    for t1 in triple[0]:
        for t2 in triple[1]:
            for t3 in triple[2]:
                if t1 == t2 == t3:
                    duplicate = t1
    duplicates_list.append(duplicate)

sum = 0
for d in duplicates_list:
    if d.isupper():
        sum += ord(d) - 38
    else:
        sum += ord(d) - 96

print(sum)

