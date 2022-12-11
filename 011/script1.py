from sys import argv
from collections import defaultdict

# test: 10605
# input: 54253

intput_monkeys = open(argv[1], 'r').read().split("\n\n")

monkeys = []
for input_monkey in intput_monkeys:
    monkey_chars = input_monkey.split("\n")
    m_num = int(monkey_chars[0].replace("Monkey ", "").replace(":", ""))
    m_items = list(map(int, monkey_chars[1].replace("  Starting items: ", "").split(", ")))
    m_operation = monkey_chars[2].replace("  Operation: new = ", "")
    m_test_div = int(monkey_chars[3].replace("  Test: divisible by ", ""))
    m_test_true = int(monkey_chars[4].replace("    If true: throw to monkey ", ""))
    m_test_false = int(monkey_chars[5].replace("    If false: throw to monkey ", ""))

    m = dict({
        "number":m_num, 
        "items":m_items,
        "operation": m_operation,
        "test_div": m_test_div,
        "m_test_true": m_test_true,
        "m_test_false": m_test_false
    })
    monkeys.append(m)


historam = defaultdict(lambda: 0)
for _ in range(20):
    for m in monkeys:
        for worry_level in m["items"]:
            historam[m['number']] += 1
            old = worry_level
            worry_level = eval(str(m['operation'])) // 3
            if worry_level % m["test_div"] == 0:
                target = m["m_test_true"]
            else:
                target = m["m_test_false"]
            monkeys[target]["items"].append(worry_level)
        m["items"] = []

his_sorted = sorted(list(historam.values()))
print(his_sorted[-1] * his_sorted[-2])