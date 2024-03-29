import copy


data = """...#.O.#.#.O.O....#...O....#..#........OO.O#...O..O#O#.......O.O....O.....#...OO#.O....OOO..OO#..#..
.##.....#.OOO.OO#...O.......O#..O.##OO.O.......O##....O....#O..O..#.#....#OO..#...O.O#.#...#....#O.O
O...##.O.O.O.O..#.#.....#O....#..#O..O...O..OO..O...##.......OO#..OOO..#O..#.O#.O......#..#O..O..O.O
..OO....OOO....O.O..OOO.....O........#...O.O.O.O..O#.O...O..#.#O........O.....#O...##....#...#.#....
##.O.O#..O..##O.....O.#.....O.O#O.O..#...#...OO.##OOO...OO#...O...O........O.#.O.........#O.#...#.#.
.#.O.O.....#..O###..O#.#..O....O.O....#...##.O..O.OOO..O.O..O#.O..O....#.#.O..#..##O...O....#O#.....
.......O...##..O..O##..##...O....###.O.#.#.O......O...O.O......#O.....#..O..O#..##O.O#O##O....O#....
.#O..#....##.##..O#..#..#..O........OO....#..##.O.#.O.O..OO.O.O#..#O##O......OO...O...OO...#....OO..
#.....O#......O#.....#..O...#O..OO..OO.#O...O...O.........O...#O...O.....#.....#...#.....O##.O.....O
OO.O..O...O......#.O......#O....#..#.#...O.O....O.#.O#...O........O......#.#O#.O...O.........#O....O
O.O..O..#......O.O.OO...OO..##.....OO.....#.O...O.#.#...OO..OO.O.........#O..#.O...O#.#..O..OO.##O..
..#.......O....#...#....##..O.O......O....O#.O..O..#.#.O#O.O.#...#.##.....O...O.O...O.#...O...O.#...
.O...#..O.....O.O.....OO.O.O.......O..O..........#...O..O..O......O....#OOO...O#O...#.O#........O...
.OO#....#.....O...#.###..#..O..O.....#O..#..OO...OOO#.O#..O#O........#..#.O..OOO#O#..O..OO........#.
..O.....#..#..O.............#..O.O..O#.......#.O.........O.#..OO.O..#..##..O.O#O....OO.O.O.O.....O#.
........#O..O#OO...#.##O.O....O...O..........##.#O..O......O..O.#...#O.O.OO...#.#OOO.#...O#....#.O.#
.....O.O...#OO#.OO#......#..O.O..#.OO.......#...#.O.O#.O.#O.O#..#O##..OO...#......#.O....#.....O.#O.
.O#OOOO...#.#..........O#.#.#.#.O....O..O...O...OOO.O.O.O..OO..O..O#.#...#....#...#O#.OO.O..#.O#....
OO#OO..#.O.#....#..#.#..#O#.O#O#.#..O.O....#..O...OO..O..#........#.O...O#.#.....#....O.....#.O.....
.O.....#...OO...#..O..#..O..O##..OO...O....#.O.#............###.O.#..O..O.........O..#.O..O.#OO.#...
.##O.#.O.#....O..O..#..O.#.O..##O..O......OO...#...O..OO#....O..O#O.##.OO#...O#...#.......O.O#.#OO..
.OO#O#...O..##.O......O..O.O....O...OOO.O..#...O#.#.O.OOO..#...#.##..OO..................OOOOO...###
.#..##...####.O#...O........O...#O..O..O....O##O..O..OO..#.....#...O.....OO......OOO.#..O.##OO##...#
....O#........O##.O...O#..#.O#O...O...O.O........#..#.#.O......O..#.....#.O..#.#..#..#O....O##...#..
.O..OO.O##..O...O.OO....O.OOO..#O#.O##......O.O#....O#O.O......#.O..#O..#O.........#..OO....#.OO..O.
.#OO..#OO.###........#...#..#.O..#O.O#O...O.#.....O...#......O.......#.O.#.##.O..#O.O###OOOO...#..O.
##...OOO.#..........O#...O#.....OO...O#..OO.OO.#.OOO..OO....O..OOO...##O...O.........##O...#.#O.....
.#....O.....#OO.O.OO..O......#.OO..#O...O..##O.#O....#O.OO..#O.OO...O..O.#..##...O......#O##OO.#.O..
.#..O....O....#......#.O.##...OO.O.O...O.OO.O....#...#..O....O#O..#...#.#..#...OO......OOO...O..#...
#.#OO.#....O.#.OO....#........O.O.##...O.#.................OOOO....O..#......O..#.#...O....#.O#OO.#O
....O.O.......##..O.........OO#O..O.O#.#.#.O....#..OO.O..O#O....O..O.O......O.O.#..O.......O.O..O.O#
...........#OO...O....#.O.#..#O.O#.....O..O.....O#.....OO.#O...#O.#O.#.....OO.O.O....OO......O#O.O..
OOOO.OO..O....O.O...O..#.........O#.##OOO#.O..O.O.O......O..#..O..#..#.O..O....O#O.#OO..O.O...O#.##.
##.O.#O.#OO#..........OO#.OO.#..#.#......#.OO...#.O.O.......O##....O..O..#.#.#O....O..##.#OO.O..O..O
#O...OO..#.#....##.O#.#...##OO#........O#.O..O#.........O.O.#....O.#.O.......O..OOO......O#O.###.O..
....O#....#..O...#.#.....O.O#O..#O....O...O.OO#...O..O#.##.O.....O...#..#.O.....O...O#..O.#...#.#O..
O.OO......#..O...O.O....#...OO..O#.O..OO..#.##.....#....O.O#O#.O....O..#..OOO..O....O.O..#..O.O..O..
.#..#..##O..O.....O#.#.O.O..O..OO..O.O..OO.##.O...O..O#........O.............#.OO..#......O..#O#OOO.
.#..##...O.#..OO...O..#..#O#..#..##.O#.#.....#....O.O..O.........#.###...#.O##..O...#.O.OO..........
........#O.......O...O#.#....#.O#....#..O.....OO........O...#.........##.....O...O#.O...O.O..#OO.O.#
.#..#.O##..##.O#.#.......OO...OO#...#O#............#.#...#...O...#.O..#O.#.O.........O..OO.O...O.#..
#.O#OO...OO.O.#...##........#....O.#.O.....##.#.O.O.O.#..O#...O..#......#..O...###O..OO..##..OO.#OOO
.OO...#O....O##.O...O.#....O...#O.......O.....OO.O...O..#...OO.OO.O#...O##.....O..#.#...#OO......O..
..O..#...O...##..O...O..OO.O.O.O.....#.....O.....O..#OOO.....OOOO#.#.O..O..#........O.#O#.#O..O.##..
.....##.....O.....O#...##.OOO....O.O..O.#.#O........OO.....#...##...#.#......#....OO.O.....#O....#.#
..O.OO#....O..O.#O.#OO#..#.O.##.#..#.OO##....O#...#..O.#..#...#.#....OOOO.#...OOOO..O.........##O.O.
O.O.#......O#...O..#.......#O.O..OOOO..#....#.#.OO.O..#O......#.#....#...#..O....#O.OO..O.......#.#.
...O.O....O#......#.O.O....O#.#..#O.#.....#...#...#.O#.........O.OO..O###...O....O.#.O.#.....##..O..
.#.OO...O#O.....O#....O......OO...OO.OOOOOO##....#..#..#O.#.OO....O#..OO.#O........O#..O.O#.#.......
#OO#.#.....O#OOO#...O.........#......O#.......O.....O#.#O...O........#....O...O.....#.......##.OOO#.
..#.O##..#OO..#....#O....#....#..........#O...#...O.#.O.O###O..O..#...#.OO....##..O.O.O.....O..O....
....OOO#.#......#..O.O......##O.#.O.#.O.OO....#..O.......#.....#O.O...##O###.##.##..#.O.#.O#..#..O#.
......O#OO......#.#..#.O#OO#O..O#O.O##.......O...O........O......O#.....#..#....#...#.#..O...O##.#O.
#..OO..O.O.....#O.O.#.#......O......O.#....O.#OO.........#.O.O#..#..#.O..O.#..#...#...O.#..........O
..O#OOO#.#.....O.....O..##.#..OOO.O..#..O#...##O..OO...#....#..#...#...OO.....##OO#.OO...#.O....#.#.
#.#O.............#....O#.....O.....O.##O.....#.#.#.....O....O...O...##..O...#........#O..##.#.....##
.O.....O...#O.#.O#..O#........#.##...O##O..........O##.O......O..#....##....###......O##..##O..#.O#.
.#...#..#..O.O.............#....O.OO.....OO#O.....OO..OOO#O.O.O.O...#...#.........OO..O#.O...#.##..#
..O...#O#.......#OO..........OO#..#.....OO#...#OO.O#....OO....O..O..#....#OO......O#O...#......O..O.
O.......O..O..#O.....O#O.........O##.O#.#.O.O....##....O.#....O....OOO..#O#...#...O.O#.O.....O.O#.O.
O.#O....O..##....O.........##.OO###....O...O...O..O#O#...#O.O.O....#..O..#..#.O.......###..#....#..O
.........O..#O...O..OO.....#...O..#O#.....O....#O#....##...#.OOOO.O..O#...O..O.O#.#..O.O..#..#.OO...
...#.....#..OO.O.#.#.O.....O#...#..O...O..O..#...O..O.O..#...#.###..#..##O.#.#O.......O..##O.O.O#...
.##O......O....#....O....#O..#.....#.O..O.O.O..#.#O.....O#.O...#.#O.#...#.........O....O....OO..O...
.OO.O.O.O#O..O##.O...OO.....O..O....O....#..#...O.O...O....O.#.O......#O.#.O#O..O...O.O.#.O..O.#....
O#..#.#..#..#...#.O...O.###.##.OO.O.#.OOO..O..#O.#.O...OO...O.OOO....#.....#OO.O##.O.#.#O...#.#.....
.#.....#.........O.#.........#...OO..O.#.O...O##O...#..O.O.OO#....###.OO.....#..........#.#OO...O.O.
........OO..O.O.#..O.#.......#.#O.OOO...OO.O............O#O#...O...#.O.....#...........O...#..OO.O#O
..#.#.#...O....#O.......#...#...O###.O.....O.O.OO....#O...OO.O.O........O.O.#O.O....OO.....OO.....#.
#..OOO#......O.#.O#...#..#..O..O.O.O.#...O#OOO.#...O.#.OO.#O..#....#..#O....O.#.O...O...O#OO...#....
.....#.....##...O....#..O..O.....O#OO.#O#.....O...O.##.#........O..O........#.#......##......#..#..O
O..O....O.##..#.#O##.#.....OO....O.##O......#...#..OO.O.....#...#........O..O#O##.O.......#..##O..##
#.....#O....O...#OOO#..O#.O.....O..OO.#..#.#.O#..O..O#.O###....O......O.#.O..#O.....#.......##O.O..O
O.O.#..#....O....O.......#.O..O#O#.O..........#O.....#OO.O...#.OO.....#...O....OO....#...O....O.#..O
..#...OO....OO......O....#..#..........##..##..#.....##...#..#O.....#OO......#........O.....O..O...#
.OO#...O#.O....#.........OO#...O#..O.#..O.O.O.#O......##.O.......O...O...###.O......O....O...#.OO#..
..O..O#O.#..O.#O...OOO#O.#.O....O.#......O....#....###....OO......O...#...OO.#....O........O#..#..OO
#..OO..O......#...##..O#.O........O.O...##.#O...O...#O#.O.O....#.............#.O#.#..O..#..OO#.....#
#..........O...O##.O#..O..OO..O.....#O.#.O......#......O.O....##.O#OO..O.O..O.O.O..#..O....O..#....O
.O.O...O.#..O.O....#.#.O.O.##.##..O..#OOOO.###...#O...#...O.....O...#.##.OO..O.#..#.O.#.......O....#
#....#....OOOOOOO.#...OO....##O.#..#......O..#..........O......##..O..###..#.O....O.......OO......#.
.O.O..##.O.#O.#...#....O..O.....#..##......O.......O..O#.O##.#........O..#.O.#.O.O..##..###..##.#...
..OOO..O##..OOOO.O.....OO##..O..O.#....#.....OO......O.OOO#...#O.OO...O.O......O#..O.##....###...#.O
....O...O.O....#..O#.O.....O.O.#.......O##...O#..OO.O.O##...#.....O#.###....O....#O.........OO..O.O.
O#.O......##..#.#..............#......#.#.OO#......##O#OO..OOO..##.O##....#..O...#......##O.O##...OO
...#OO....OO...O#.#..##....OO.#..#O......O#....#.O.....O.#O..OO.#..OO...O#.O#....O.#.OO.O.O#..O.....
#..O.OO#O...O..O..........#..#.#..#..#O.....#O#..O....#..O...O.#.#O#.#OO.....OOO.#..#.........O...O#
....O......#..........O...#.....OOOO........#.#OO.O............O...#....O........#....#....#........
...O.......###...O.O...#O.##O.OOO.........O.###.O.......O....O.O...O.#.....#..#O..#..OO..O.O...O....
O.O#....##.O.O.....O....#............OO.#O...O..#...##.#.#O#O.#.....O......O....#.OO#.O#....#.....O.
..O####.O.........O...........OO..OO.#.....O.......#..O#.O....O#...##.......#.#....O..O..O#..##.....
.#..#......O.##.O.OOO.O.OO....O.......#......#.O...OOOO...O..#..#.O.#......O...O#.#.O.#.O....O....O.
##....O.O..O..O.#...O##.......O....#...#OOO.O..##.....#....O.......#O..#.#O..O.#.......O..#.O.O#.O##
...O....O#O.#...#......#..O.O.O.O...O.....O..O.#..#.....O#...OO...#.O.O....#..OOO...#.....OO.OO..O..
O##.O.##.O#OO...OO...OO..O....OO#O.#O..O.O....OO..........O..#.O.#O#.......O.O..#O#....#..#...#O..#.
.#.#..........#.......#..OO#....O.#.#.O.....OO.#.O..#.#.O....#..O....#..#..O.#O#O.....#.O.O.#O.O.#O.
.O.#....##O...#..OOO.#......#...#.O.......OO....#.......#..#.OOO........OO..O..###O##..O.....O##....
OO##..O#....O.##.......O...#........O.O...#O#.#.OOO....#......#.#O.O.O..O..O...#.#.O.O.OOO.O#O......
#O...#....OOO.O...#O....O...O..........O..#..O#.O..#O.....#......#.#..#.OO..#....#O#....O...O....##.
.OOOO......##.#O.#O...#......O..#..O..#.O...O.OO...............#O...O..##..#.#....O...O..O.##..O.O..""".split('\n')


orig = [[x for x in line] for line in data]
def spin(data, direction): # 'N', 'E', 'S', 'W'
    if direction in 'NS':
        condition = lambda i: (i >= 0) if direction == 'N' else (i < len(data))
        for c in range(len(data[0])):
            i = (len(data) - 1) if direction == 'N' else 0
            count = 0
            while condition(i):
                if data[i][c] == 'O':
                    data[i][c] = '.'
                    count += 1
                elif data[i][c] == '#':
                    for j in range(count):
                        diff = (j + 1) if direction == 'N' else  (-j + -1)
                        data[i + diff][c] = 'O'
                    count = 0
                i += -1 if direction == 'N' else 1
            for j in range(count):
                diff = (j + 1) if direction == 'N' else  (-j + -1)
                data[i + diff][c] = 'O'
    else:
        condition = lambda i: (i >= 0) if direction == 'W' else (i < len(data[0]))
        for r in range(len(data)):
            i = (len(data[0]) - 1) if direction == 'W' else 0
            count = 0
            while condition(i):
                if data[r][i] == 'O':
                    data[r][i] = '.'
                    count += 1
                elif data[r][i] == '#':
                    for j in range(count):
                        diff = (j + 1) if direction == 'W' else  (-j + -1)
                        data[r][i + diff] = 'O'
                    count = 0
                i += -1 if direction == 'W' else 1
            for j in range(count):
                diff = (j + 1) if direction == 'W' else  (-j + -1)
                data[r][i + diff] = 'O'

#####
sum_ = 0
data = copy.deepcopy(orig)
spin(data, 'N')
for i in range(len(data)):
    r = len(data) - 1 - i
    sum_ += (i + 1) * data[r].count('O')
print(sum_)

#####
data = copy.deepcopy(orig)
DIRS = ['N', 'W', 'S', 'E']
seen, data_str = {}, ''

for i in range(1000000000):
    if data_str in seen:
        cycle_len = i - seen[data_str]
        target = (1000000000 - seen[data_str]) % cycle_len + seen[data_str]
        for key, value in seen.items():
            
            # if value == (1000000000 - i) % cycle_len:
            if value == target:
                data = key.split('\n')
                break
        break

    seen[data_str] = i
    for dir in DIRS:
        spin(data, dir)
        data_str = '\n'.join([''.join(line) for line in data])
sum_ = 0
for i in range(len(data)):
    r = len(data) - 1 - i
    sum_ += (i + 1) * data[r].count('O')
print(sum_)