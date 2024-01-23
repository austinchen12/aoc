data = """addx 1
noop
addx 2
addx 11
addx -4
noop
noop
noop
noop
addx 3
addx -3
addx 10
addx 1
noop
addx 12
addx -8
addx 5
noop
noop
addx 1
addx 4
addx -12
noop
addx -25
addx 14
addx -7
noop
addx 11
noop
addx -6
addx 3
noop
addx 2
addx 22
addx -12
addx -17
addx 15
addx 2
addx 10
addx -9
noop
noop
noop
addx 5
addx 2
addx -33
noop
noop
noop
noop
addx 12
addx -9
addx 7
noop
noop
addx 3
addx -2
addx 2
addx 26
addx -31
addx 14
addx 3
noop
addx 13
addx -1
noop
addx -5
addx -13
addx 14
noop
addx -20
addx -15
noop
addx 7
noop
addx 31
noop
addx -26
noop
noop
noop
addx 5
addx 20
addx -11
addx -3
addx 9
addx -5
addx 2
noop
addx 4
noop
addx 4
noop
noop
addx -7
addx -30
noop
addx 7
noop
noop
addx -2
addx -4
addx 11
addx 14
addx -9
addx -2
noop
addx 7
noop
addx -11
addx -5
addx 19
addx 5
addx 2
addx 5
noop
noop
addx -2
addx -27
addx -6
addx 1
noop
noop
addx 4
addx 1
addx 4
addx 5
noop
noop
noop
addx 1
noop
addx 4
addx 1
noop
noop
addx 5
noop
noop
addx 4
addx 1
noop
addx 4
addx 1
noop
noop
noop
noop""".split('\n')

#####
sum_, curr, cycle = 0, 1, 0
for line in data:
    cycle += 1
    if line == "noop":
        if (cycle - 20) % 40 == 0:
            sum_ += cycle * curr
    else:
        _, value = line.split(' ')
        value = int(value)

        if (cycle - 20) % 40 == 0:
            sum_ += cycle * curr

        cycle += 1
        if (cycle - 20) % 40 == 0:
            sum_ += cycle * curr
        
        curr += value
print(sum_)

#####
output = []
def add_output(output, cycle, curr):
    if 0 <= curr and curr + 3 <= 40:
        output.append('#' if cycle % 40 in range(curr, curr + 3) else '.')
    elif curr < 0:
        output.append('#' if (cycle % 40 in range(curr % 40, 40)) or (cycle % 40 in range(0, (curr + 3) % 40)) else '.')
    elif curr + 3 > 40:
        output.append('#' if (cycle % 40 in range(curr, 40)) or (cycle % 40 in range(0, (curr + 3) % 40)) else '.')
    else:
        assert False
        

curr, cycle = 1, 0
for line in data:
    cycle += 1
    if line == "noop":
        add_output(output, cycle, curr)
    else:
        _, value = line.split(' ')
        value = int(value)
        add_output(output, cycle, curr)

        cycle += 1
        add_output(output, cycle, curr)
        curr += value
assert len(output) == 40 * 6
for i in range(len(output)):
    print(output[i], end='')
    if (i + 1) % 40 == 0:
        print()