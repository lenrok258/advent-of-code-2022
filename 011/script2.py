from sys import argv
from functools import reduce
from collections import defaultdict

# test: 2713310158
# input: 13119526120

intput_chunks = open(argv[1], 'r').read().split("\n\n")
monkeys = []
for chunk in intput_chunks:
    chunk_lines = chunk.split("\n")
    m_num = int(chunk_lines[0].replace("Monkey ", "").replace(":", ""))
    m_items = list(map(int, chunk_lines[1].replace("  Starting items: ", "").split(", ")))
    m_operation = chunk_lines[2].replace("  Operation: new = ", "")
    m_test_div = int(chunk_lines[3].replace("  Test: divisible by ", ""))
    test_true = int(chunk_lines[4].replace("    If true: throw to monkey ", ""))
    test_false = int(chunk_lines[5].replace("    If false: throw to monkey ", ""))

    m = dict({
        "number":m_num, 
        "items":m_items,
        "operation": m_operation,
        "test_div": m_test_div,
        "test_true": test_true,
        "test_false": test_false
    })
    monkeys.append(m)

historam = defaultdict(lambda: 0)
prime_product = reduce(lambda a,b: a*b, [m["test_div"] for m in monkeys])

for _ in range(10_000):
    for m in monkeys:
        for worry_level in m["items"]:
            historam[m['number']] += 1
            worry_level = worry_level % prime_product if worry_level > prime_product else worry_level
            old = int(worry_level)
            worry_level = eval(m['operation'])
            if worry_level % m["test_div"] == 0:
                target = m["test_true"]
            else:
                target = m["test_false"]
            monkeys[target]["items"].append(worry_level)
        m["items"] = []


his_sorted = sorted(list(historam.values()))
print(his_sorted[-1] * his_sorted[-2])    