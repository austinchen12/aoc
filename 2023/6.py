data = """Time:        47     98     66     98
Distance:   400   1213   1011   1540""".split('\n')

#####
times = [int(x) for x in data[0][5:].split()]
distances = [int(x) for x in data[1][9:].split()]
sum_ = 1
for time, distance in zip(times, distances):
    count = 0
    for i in range(time + 1):
        d = i * (time - i)
        if d > distance:
            count += 1
    if count > 0:
        sum_ *= count
print(sum_)

#####
import math
time = int(''.join(data[0][5:].split()))
distance = int(''.join(data[1][9:].split()))
count = 0
for i in range(time + 1):
    d = i * (time - i)
    if d > distance:
        print(time + 1 - 2 * i)
        break
