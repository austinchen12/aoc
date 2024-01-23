data = """Sensor at x=3907621, y=2895218: closest beacon is at x=3790542, y=2949630
Sensor at x=1701067, y=3075142: closest beacon is at x=2275951, y=3717327
Sensor at x=3532369, y=884718: closest beacon is at x=2733699, y=2000000
Sensor at x=2362427, y=41763: closest beacon is at x=2999439, y=-958188
Sensor at x=398408, y=3688691: closest beacon is at x=2275951, y=3717327
Sensor at x=1727615, y=1744968: closest beacon is at x=2733699, y=2000000
Sensor at x=2778183, y=3611924: closest beacon is at x=2275951, y=3717327
Sensor at x=2452818, y=2533012: closest beacon is at x=2733699, y=2000000
Sensor at x=88162, y=2057063: closest beacon is at x=-109096, y=390805
Sensor at x=2985370, y=2315046: closest beacon is at x=2733699, y=2000000
Sensor at x=2758780, y=3000106: closest beacon is at x=3279264, y=2775610
Sensor at x=3501114, y=3193710: closest beacon is at x=3790542, y=2949630
Sensor at x=313171, y=1016326: closest beacon is at x=-109096, y=390805
Sensor at x=3997998, y=3576392: closest beacon is at x=3691556, y=3980872
Sensor at x=84142, y=102550: closest beacon is at x=-109096, y=390805
Sensor at x=3768533, y=3985372: closest beacon is at x=3691556, y=3980872
Sensor at x=2999744, y=3998031: closest beacon is at x=3691556, y=3980872
Sensor at x=3380504, y=2720962: closest beacon is at x=3279264, y=2775610
Sensor at x=3357940, y=3730208: closest beacon is at x=3691556, y=3980872
Sensor at x=1242851, y=838744: closest beacon is at x=-109096, y=390805
Sensor at x=3991401, y=2367688: closest beacon is at x=3790542, y=2949630
Sensor at x=3292286, y=2624894: closest beacon is at x=3279264, y=2775610
Sensor at x=2194423, y=3990859: closest beacon is at x=2275951, y=3717327""".split('\n')
# data = """Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3""".split('\n')

import re
regex = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')

#####
ranges, xvals = [], set()
TARGET = 2000000
for line in data:
    sx, sy, bx, by = [int(num) for num in regex.match(line).groups()]
    distance = abs(sx - bx) + abs(sy - by)
    if sy == TARGET:
        xvals.add(sx)
    if by == TARGET:
        xvals.add(bx)
    if TARGET not in range(sy - distance, sy + distance + 1):
        continue

    leftover = distance - abs(sy - TARGET)
    r = [-1 * leftover + sx, leftover + 1 + sx]
    ranges.append(r)
def merge(intervals):
    intervals = sorted(intervals, key=lambda x: x [0])
    ans = []
    for interval in intervals:
        if not ans or ans[-1][1] < interval[0]:
            ans.append(interval)
        else:
            ans[-1][1] = max(ans[-1][1], interval[1])
    
    return ans
merged_ranges = merge(sorted(ranges))
print(sum(b - a for a, b in merged_ranges) - len(xvals))

#####
S, border = set(), set()
sum_ = 0
for line in data:
    sx, sy, bx, by = [int(num) for num in regex.match(line).groups()]
    distance = abs(sx - bx) + abs(sy - by)

    S.add((sx, sy, distance))

    sum_ += (distance + 1) * 2
    for y in range(sy - (distance + 1), sy + (distance + 1) + 1):
        leftover = (distance + 1) - abs(sy - y)
        border.add((sx - leftover, y))
        border.add((sx + leftover, y))
print(sum_)
exit()
print(S)
print(border)
def get_missing_coord(border, S):
    for x, y in border:
        for sx, sy, distance in S:
            d = abs(sx - x) + abs(sy - y)
            if d <= distance:
                break
        else:
            return (x, y)
coord = get_missing_coord(border, S)
print(4000000 * coord[0] + coord[1])