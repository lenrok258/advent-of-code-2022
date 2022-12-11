# test: 
# input: 

intput_monkeys = open('input_test.txt', 'r').read().split("\n\n")
monkeys = []
for input_monkey in intput_monkeys:
    monkey_chars = input_monkey.split("\n")
    m_num = int(monkey_chars[0].replace("Monkey ", "").replace(":", ""))
    m_items = monkey_chars[1].replace("  Starting items: ", "").split(", ")
    m_operation = monkey_chars[2].replace("  Operation: ", "")
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

for m in monkeys:
    print(m)




