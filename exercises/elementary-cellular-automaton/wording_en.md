Build a program taking an integer as single parameter, .

This integer is a rule number in the [Wolfram
code](https://en.wikipedia.org/wiki/Wolfram_code).

Your program will display a 79×40 table filled with `#` for ones (`1`s) and `.`
for zeroes (`0`s), as a result of running an [elementary
automata](https://en.wikipedia.org/wiki/Elementary_cellular_automaton) for 
the given rule number (the `int` parameter).

The first line will always be filled with zeroes except for a single
cell with a 1 right in the middle.

The "board" is a cylinder: on the left of the leftmost column is the rightmost
column, and vice-versa.

Here is an example, so you can check your implementation visually:

```
julien@prof$ python solution.py 90
.......................................#.......................................
......................................#.#......................................
.....................................#...#.....................................
....................................#.#.#.#....................................
...................................#.......#...................................
..................................#.#.....#.#..................................
.................................#...#...#...#.................................
................................#.#.#.#.#.#.#.#................................
...............................#...............#...............................
..............................#.#.............#.#..............................
.............................#...#...........#...#.............................
............................#.#.#.#.........#.#.#.#............................
...........................#.......#.......#.......#...........................
..........................#.#.....#.#.....#.#.....#.#..........................
.........................#...#...#...#...#...#...#...#.........................
........................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#........................
.......................#...............................#.......................
......................#.#.............................#.#......................
.....................#...#...........................#...#.....................
....................#.#.#.#.........................#.#.#.#....................
...................#.......#.......................#.......#...................
..................#.#.....#.#.....................#.#.....#.#..................
.................#...#...#...#...................#...#...#...#.................
................#.#.#.#.#.#.#.#.................#.#.#.#.#.#.#.#................
...............#...............#...............#...............#...............
..............#.#.............#.#.............#.#.............#.#..............
.............#...#...........#...#...........#...#...........#...#.............
............#.#.#.#.........#.#.#.#.........#.#.#.#.........#.#.#.#............
...........#.......#.......#.......#.......#.......#.......#.......#...........
..........#.#.....#.#.....#.#.....#.#.....#.#.....#.#.....#.#.....#.#..........
.........#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#.........
........#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#........
.......#...............................................................#.......
......#.#.............................................................#.#......
.....#...#...........................................................#...#.....
....#.#.#.#.........................................................#.#.#.#....
...#.......#.......................................................#.......#...
..#.#.....#.#.....................................................#.#.....#.#..
.#...#...#...#...................................................#...#...#...#.
#.#.#.#.#.#.#.#.................................................#.#.#.#.#.#.#.#
```

Don't forget to print something friendly if the human forgot to give
the rule number as a parameter of your program.
