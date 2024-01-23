data = """.........................#.........#..................#..............#.......#.....#........................#............#.....#...........#
.............................................#.....................................................#........................................
.......#............#..........#............................................................................................................
.#................................................#........#.............................................#..............................#...
................#.....................#.............................................................................#.......................
........................................................................#....................#................#...........#.................
...........................................#........................................#.......................................................
..................................#......................#.......#...........#..............................................................
..........#.................................................................................................................................
..............................................#..........................................#.....................................#............
..........................................................................#.................................................................
...#................#...........#.......#............................#...............................#......................................
.........................................................................................................................#..................
.............................................................................#........#.............................#....................#..
..........#.....#...............................#..............................................................#...................#........
.........................................................#..................................................................................
.....................#......#.......................#.......................................................................................
.....................................#.....#.......................#.........................#...........#..............#..................#
...................................................................................................#........................................
...............#........................................................#.........................................#............#............
#........................................................................................#..................................................
...............................................................................#............................................................
....................................................#......#.........#..........................#...........................................
...............................................#.....................................................#...........................#..........
.....#............#........................................................................................................................#
...........................................#.................................................................#......#.......................
............#....................#...............................#..........#...............................................................
............................................................#......................................#........................#...............
...........................#.......................................................#..........#......................................#......
...................#..............................................................................................#.........................
....................................................................#......................................................................#
.............#................................#.............................................................................................
........#.........................#..........................................#..................#...........................................
...........................................................................................................#...............#................
........................................#.........#.......#.....................................................#...........................
..#................................................................................#.................................#.............#........
.....................#......#.......................................................................#.......................................
........................................................................................................................................#...
..........#.....#........................................................#............#......................................#..............
.....................................................#.......#..............................................................................
.............................................................................................................#.........#....................
...#.............................................................#........................................................................#.
.............................#.........#.................#.......................#.................#........................................
..............................................#.........................#...................#...............................................
............#............#..........................#.......................................................................................
....................................................................................................................#.......................
...................#...............................................#........................................................................
...................................#............#..........................................................#..............#.....#......#....
.......................#......#...........................................#..............#.........#........................................
............................................................................................................................................
..#............................................................#.....#...............................................#......................
.......#......................................#.........#.....................................................#..........................#..
.........................#...............................................................................#..................................
.............#...............................................................................#..............................................
#........................................#..................#.............#.........#.................................................#.....
............................................................................................................................................
..................................................#........................................................................................#
........#.............#............#...........................................................................#............................
..............#.....................................................................................#.......................................
...................................................................................................................#........................
..................#...........#............#................#...................................#..............................#............
......................................................................#.................#....................#.......................#......
.................................................................................#.........................................#................
............#....................................#......#...................................................................................
......................#.........................................#...........................................................................
.......#....................#.........#....................................................#.......................#............#...........
.............................................................................#......................#.......................................
...#.............#..........................#........#...............#...................................#................#.................
............................................................................................................................................
.................................................................................................#..........................................
.........................#.....#..................................................#...........................................#.......#.....
............................................................................................................................................
............#.....................................................#...............................................................#.........
...#........................#.................#.........................................................#...........#.....................#.
................#....................................#......................................#...............................................
............................................................................................................................................
............................................................................................................................................
...................................#.................................................#.................................#....................
.............#..............................#....................................................#..............#.......................#...
...................................................#.........#..........#..................#................................................
#......#.............#.......#...........................................................................#..................................
.................................................................................#..................#...............#.......................
..........................................................#.................................................................................
.......................................................................................................................................#....
...........#....................................................#......................#...................#................................
.......................................#................................#...................................................................
...................#............................................................................................#........#..........#.......
............................................#....................................................#......#.....................#.............
........#........................#................#...............#.........................................................................
.............#.............#............................................................#............................#......................
...........................................................#................................................................................
........................................#......#.............................#...............................#..............................
................#...........................................................................................................................
.................................................................#................#.................#.......................................
......#.............#...........#.....................................................................................................#.....
.#.......................#...........#......#.............................................#.................................................
........................................................#.................#.................................................................
....................................................................................#.......................................................
...............#..................#.............................#............................#..............#...............#...............
.........................................#.......................................................................#..........................
..#........#........#..............................#........................................................................................
............................................................#.....................#.........................................................
....................................#........................................#...........#......#......#....................................
.......................#.......................#..................................................................................#.........
........#......#.........................................................................................................................#..
..........................................................#..............................................................#..................
...#........................#........................#................#......................#......................#.......................
................................................................#..........#...........#......................................#.............
..............................................#.....................................................#.................................#.....
......................................#.....................................................................................................
..........#......#...............................................................................................#..........................
...........................................#.................#...................#........................................#.................
........................................................................................#......#...........................................#
....................................................................#.......................................................................
.#.......................#................................#..............#.............................................#....................
................................................#...............................................................#...........................
.......................................#.............#.....................................................#...............#................
.............#................#...................................................................#................................#........
.............................................#..........................................#.................................................#.
.................#................................................................#.........................................................
.#..........................................................................................................................................
........................................................................................................................#...................
...........#..........#...........#..............#.......................................................#.......#....................#.....
....#................................................................#......................................................................
...........................................#.................#...............................................#..................#...........
.....................................#....................................#..........#..........#...........................................
.........................................................................................................................#..............#...
.................................................................................#.........#............#...................................
................#......#.............................#.............#........................................................................
#.......#....................#.........#....................................................................................................
.............................................#..............................#.....................................................#.........
...................#.................................................................#......................................................
....................................#................................................................#..............#.......................
...................................................#...........#................................#...........#..............................#
.........................................................................#.....#............................................................
..#.....................#......................#.................................................................#...........#..............
.........................................................................................#.........#........................................
.........#.......................................................................................................................#......#...
.............................#.....#............................#.....#..............#...............................#......................
.............#.............................................#.............................................#.................#................""".split('\n')

stars, empty_cols, empty_rows = [], set(), set()
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '#':
            stars.append((i, j))
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] != '.':
            break
        if j == (len(data[i]) - 1):
            empty_rows.add(i)
for j in range(len(data[0])):
    for i in range(len(data)):
        if data[i][j] != '.':
            break
        if i == len(data) - 1:
            empty_cols.add(j)
def func(DUPE):
    sum_ = 0
    for ai in range(len(stars)):
        for bi in range(ai, len(stars)):
            if stars[ai] == stars[bi]:
                continue
            ar, ac = stars[ai]
            br, bc = stars[bi]
            steps = max(ar, br) - min(ar, br) + max(ac, bc) - min(ac, bc)
            for i in range(min(ar, br), max(ar, br) + 1):
                if i in empty_rows:
                    steps += DUPE - 1
            for i in range(min(ac, bc), max(ac, bc) + 1):
                if i in empty_cols:
                    steps += DUPE - 1
            sum_ += steps
    print(sum_)


#####
func(2)

#####
func(1000000)