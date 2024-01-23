data = """Monkey 0:
  Starting items: 84, 66, 62, 69, 88, 91, 91
  Operation: new = old * 11
  Test: divisible by 2
    If true: throw to monkey 4
    If false: throw to monkey 7

Monkey 1:
  Starting items: 98, 50, 76, 99
  Operation: new = old * old
  Test: divisible by 7
    If true: throw to monkey 3
    If false: throw to monkey 6

Monkey 2:
  Starting items: 72, 56, 94
  Operation: new = old + 1
  Test: divisible by 13
    If true: throw to monkey 4
    If false: throw to monkey 0

Monkey 3:
  Starting items: 55, 88, 90, 77, 60, 67
  Operation: new = old + 2
  Test: divisible by 3
    If true: throw to monkey 6
    If false: throw to monkey 5

Monkey 4:
  Starting items: 69, 72, 63, 60, 72, 52, 63, 78
  Operation: new = old * 13
  Test: divisible by 19
    If true: throw to monkey 1
    If false: throw to monkey 7

Monkey 5:
  Starting items: 89, 73
  Operation: new = old + 5
  Test: divisible by 17
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 6:
  Starting items: 78, 68, 98, 88, 66
  Operation: new = old + 6
  Test: divisible by 11
    If true: throw to monkey 2
    If false: throw to monkey 5

Monkey 7:
  Starting items: 70
  Operation: new = old + 7
  Test: divisible by 5
    If true: throw to monkey 1
    If false: throw to monkey 3""".split('\n\n')

####
monkeys, monkey_items, counts, maxes = [], [], [], [0, 0]
for chunk in data:
    lines = chunk.split('\n')
    items = [int(x) for x in lines[1][18:].split(', ')]
    operation, constant = lines[2][23:].split(' ')
    constant = 'old' if constant == 'old' else int(constant)
    test_constant = int(lines[3][21:])
    true = int(lines[4][29:])
    false = int(lines[5][30:])

    monkeys.append((operation, constant, test_constant, true, false))
    monkey_items.append(items)
    counts.append(0)
for round in range(20):
    for i in range(len(monkeys)):
        operation, constant, test_constant, true, false = monkeys[i]
        items = monkey_items[i]
        counts[i] += len(items)
        while len(items):
            item = items.pop(0)
            if operation == '+':
                new_item = item + constant
            elif operation == '*':
                new_item = item * (item if constant == 'old' else constant)
            else:
                assert False
        
            new_item = new_item // 3
            if new_item % test_constant == 0:
                monkey_items[true].append(new_item)
            else:
                monkey_items[false].append(new_item)

for count in counts:
    if count > maxes[0]:
        maxes[1] = maxes[0]
        maxes[0] = count
    elif maxes[0] > count > maxes[1]:
        maxes[1] = count
print(maxes[0] * maxes[1])

#####
monkeys, monkey_items, counts, maxes, maxn = [], [], [], [0, 0], 1
for chunk in data:
    lines = chunk.split('\n')
    items = [int(x) for x in lines[1][18:].split(', ')]
    operation, constant = lines[2][23:].split(' ')
    constant = 'old' if constant == 'old' else int(constant)
    test_constant = int(lines[3][21:])
    true = int(lines[4][29:])
    false = int(lines[5][30:])

    monkeys.append((operation, constant, test_constant, true, false))
    monkey_items.append(items)
    counts.append(0)
    maxn *= test_constant
for round in range(10000):
    for i in range(len(monkeys)):
        operation, constant, test_constant, true, false = monkeys[i]
        items = monkey_items[i]
        counts[i] += len(items)
        while len(items):
            item = items.pop(0)
            if operation == '+':
                new_item = item + constant
            elif operation == '*':
                new_item = item * (item if constant == 'old' else constant)
            else:
                assert False
        
            new_item = new_item % maxn
            if new_item % test_constant == 0:
                monkey_items[true].append(new_item)
            else:
                monkey_items[false].append(new_item)

for count in counts:
    if count > maxes[0]:
        maxes[1] = maxes[0]
        maxes[0] = count
    elif maxes[0] > count > maxes[1]:
        maxes[1] = count
print(maxes[0] * maxes[1])