import gettext
from time import perf_counter
from pathlib import Path

import correction_helper as checker

checker.exclude_file_from_traceback(__file__)
_ = gettext.translation("check", Path(__file__).parent, fallback=True).gettext


def too_slow(start, tested):
    checker.fail(
        """Your program is a bit slow, it takes in average {s:.2f}s on each run,
I won't be able to test it thouroughly.

You can do better.""".format(
            s=(perf_counter() - start) / tested
        )
    )


EXPECTED = {
    24: (
        ".......................................#.......................................\n"  # noqa: E501
        "........................................#......................................\n"  # noqa: E501
        ".........................................#.....................................\n"  # noqa: E501
        "..........................................#....................................\n"  # noqa: E501
        "...........................................#...................................\n"  # noqa: E501
        "............................................#..................................\n"  # noqa: E501
        ".............................................#.................................\n"  # noqa: E501
        "..............................................#................................\n"  # noqa: E501
        "...............................................#...............................\n"  # noqa: E501
        "................................................#..............................\n"  # noqa: E501
        ".................................................#.............................\n"  # noqa: E501
        "..................................................#............................\n"  # noqa: E501
        "...................................................#...........................\n"  # noqa: E501
        "....................................................#..........................\n"  # noqa: E501
        ".....................................................#.........................\n"  # noqa: E501
        "......................................................#........................\n"  # noqa: E501
        ".......................................................#.......................\n"  # noqa: E501
        "........................................................#......................\n"  # noqa: E501
        ".........................................................#.....................\n"  # noqa: E501
        "..........................................................#....................\n"  # noqa: E501
        "...........................................................#...................\n"  # noqa: E501
        "............................................................#..................\n"  # noqa: E501
        ".............................................................#.................\n"  # noqa: E501
        "..............................................................#................\n"  # noqa: E501
        "...............................................................#...............\n"  # noqa: E501
        "................................................................#..............\n"  # noqa: E501
        ".................................................................#.............\n"  # noqa: E501
        "..................................................................#............\n"  # noqa: E501
        "...................................................................#...........\n"  # noqa: E501
        "....................................................................#..........\n"  # noqa: E501
        ".....................................................................#.........\n"  # noqa: E501
        "......................................................................#........\n"  # noqa: E501
        ".......................................................................#.......\n"  # noqa: E501
        "........................................................................#......\n"  # noqa: E501
        ".........................................................................#.....\n"  # noqa: E501
        "..........................................................................#....\n"  # noqa: E501
        "...........................................................................#...\n"  # noqa: E501
        "............................................................................#..\n"  # noqa: E501
        ".............................................................................#.\n"  # noqa: E501
        "..............................................................................#"  # noqa: E501
    ),  # noqa: E501
    26: (  # noqa: E501
        ".......................................#.......................................\n"  # noqa: E501
        "......................................#.#......................................\n"  # noqa: E501
        ".....................................#...#.....................................\n"  # noqa: E501
        "....................................#.#.#.#....................................\n"  # noqa: E501
        "...................................#.......#...................................\n"  # noqa: E501
        "..................................#.#.....#.#..................................\n"  # noqa: E501
        ".................................#...#...#...#.................................\n"  # noqa: E501
        "................................#.#.#.#.#.#.#.#................................\n"  # noqa: E501
        "...............................#...............#...............................\n"  # noqa: E501
        "..............................#.#.............#.#..............................\n"  # noqa: E501
        ".............................#...#...........#...#.............................\n"  # noqa: E501
        "............................#.#.#.#.........#.#.#.#............................\n"  # noqa: E501
        "...........................#.......#.......#.......#...........................\n"  # noqa: E501
        "..........................#.#.....#.#.....#.#.....#.#..........................\n"  # noqa: E501
        ".........................#...#...#...#...#...#...#...#.........................\n"  # noqa: E501
        "........................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#........................\n"  # noqa: E501
        ".......................#...............................#.......................\n"  # noqa: E501
        "......................#.#.............................#.#......................\n"  # noqa: E501
        ".....................#...#...........................#...#.....................\n"  # noqa: E501
        "....................#.#.#.#.........................#.#.#.#....................\n"  # noqa: E501
        "...................#.......#.......................#.......#...................\n"  # noqa: E501
        "..................#.#.....#.#.....................#.#.....#.#..................\n"  # noqa: E501
        ".................#...#...#...#...................#...#...#...#.................\n"  # noqa: E501
        "................#.#.#.#.#.#.#.#.................#.#.#.#.#.#.#.#................\n"  # noqa: E501
        "...............#...............#...............#...............#...............\n"  # noqa: E501
        "..............#.#.............#.#.............#.#.............#.#..............\n"  # noqa: E501
        ".............#...#...........#...#...........#...#...........#...#.............\n"  # noqa: E501
        "............#.#.#.#.........#.#.#.#.........#.#.#.#.........#.#.#.#............\n"  # noqa: E501
        "...........#.......#.......#.......#.......#.......#.......#.......#...........\n"  # noqa: E501
        "..........#.#.....#.#.....#.#.....#.#.....#.#.....#.#.....#.#.....#.#..........\n"  # noqa: E501
        ".........#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#.........\n"  # noqa: E501
        "........#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#........\n"  # noqa: E501
        ".......#...............................................................#.......\n"  # noqa: E501
        "......#.#.............................................................#.#......\n"  # noqa: E501
        ".....#...#...........................................................#...#.....\n"  # noqa: E501
        "....#.#.#.#.........................................................#.#.#.#....\n"  # noqa: E501
        "...#.......#.......................................................#.......#...\n"  # noqa: E501
        "..#.#.....#.#.....................................................#.#.....#.#..\n"  # noqa: E501
        ".#...#...#...#...................................................#...#...#...#.\n"  # noqa: E501
        "#.#.#.#.#.#.#.#.................................................#.#.#.#.#.#.#.#"  # noqa: E501
    ),  # noqa: E501
    28: (  # noqa: E501
        ".......................................#.......................................\n"  # noqa: E501
        ".......................................##......................................\n"  # noqa: E501
        ".......................................#.#.....................................\n"  # noqa: E501
        ".......................................#.##....................................\n"  # noqa: E501
        ".......................................#.#.#...................................\n"  # noqa: E501
        ".......................................#.#.##..................................\n"  # noqa: E501
        ".......................................#.#.#.#.................................\n"  # noqa: E501
        ".......................................#.#.#.##................................\n"  # noqa: E501
        ".......................................#.#.#.#.#...............................\n"  # noqa: E501
        ".......................................#.#.#.#.##..............................\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.............................\n"  # noqa: E501
        ".......................................#.#.#.#.#.##............................\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#...........................\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.##..........................\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.........................\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.##........................\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.......................\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.##......................\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.....................\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.##....................\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#...................\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.##..................\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#.#.................\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#.##................\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#.#.#...............\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#.#.##..............\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.............\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#.#.#.##............\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#...........\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.##..........\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.........\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.##........\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.......\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.##......\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.....\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.##....\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#...\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.##..\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.##"  # noqa: E501
    ),  # noqa: E501
    30: (  # noqa: E501
        ".......................................#.......................................\n"  # noqa: E501
        "......................................###......................................\n"  # noqa: E501
        ".....................................##..#.....................................\n"  # noqa: E501
        "....................................##.####....................................\n"  # noqa: E501
        "...................................##..#...#...................................\n"  # noqa: E501
        "..................................##.####.###..................................\n"  # noqa: E501
        ".................................##..#....#..#.................................\n"  # noqa: E501
        "................................##.####..######................................\n"  # noqa: E501
        "...............................##..#...###.....#...............................\n"  # noqa: E501
        "..............................##.####.##..#...###..............................\n"  # noqa: E501
        ".............................##..#....#.####.##..#.............................\n"  # noqa: E501
        "............................##.####..##.#....#.####............................\n"  # noqa: E501
        "...........................##..#...###..##..##.#...#...........................\n"  # noqa: E501
        "..........................##.####.##..###.###..##.###..........................\n"  # noqa: E501
        ".........................##..#....#.###...#..###..#..#.........................\n"  # noqa: E501
        "........................##.####..##.#..#.#####..#######........................\n"  # noqa: E501
        ".......................##..#...###..####.#....###......#.......................\n"  # noqa: E501
        "......................##.####.##..###....##..##..#....###......................\n"  # noqa: E501
        ".....................##..#....#.###..#..##.###.####..##..#.....................\n"  # noqa: E501
        "....................##.####..##.#..######..#...#...###.####....................\n"  # noqa: E501
        "...................##..#...###..####.....####.###.##...#...#...................\n"  # noqa: E501
        "..................##.####.##..###...#...##....#...#.#.###.###..................\n"  # noqa: E501
        ".................##..#....#.###..#.###.##.#..###.##.#.#...#..#.................\n"  # noqa: E501
        "................##.####..##.#..###.#...#..####...#..#.##.######................\n"  # noqa: E501
        "...............##..#...###..####...##.#####...#.#####.#..#.....#...............\n"  # noqa: E501
        "..............##.####.##..###...#.##..#....#.##.#.....#####...###..............\n"  # noqa: E501
        ".............##..#....#.###..#.##.#.####..##.#..##...##....#.##..#.............\n"  # noqa: E501
        "............##.####..##.#..###.#..#.#...###..####.#.##.#..##.#.####............\n"  # noqa: E501
        "...........##..#...###..####...####.##.##..###....#.#..####..#.#...#...........\n"  # noqa: E501
        "..........##.####.##..###...#.##....#..#.###..#..##.####...###.##.###..........\n"  # noqa: E501
        ".........##..#....#.###..#.##.#.#..#####.#..######..#...#.##...#..#..#.........\n"  # noqa: E501
        "........##.####..##.#..###.#..#.####.....####.....####.##.#.#.#########........\n"  # noqa: E501
        ".......##..#...###..####...####.#...#...##...#...##....#..#.#.#........#.......\n"  # noqa: E501
        "......##.####.##..###...#.##....##.###.##.#.###.##.#..#####.#.##......###......\n"  # noqa: E501
        ".....##..#....#.###..#.##.#.#..##..#...#..#.#...#..####.....#.#.#....##..#.....\n"  # noqa: E501
        "....##.####..##.#..###.#..#.####.####.#####.##.#####...#...##.#.##..##.####....\n"  # noqa: E501
        "...##..#...###..####...####.#....#....#.....#..#....#.###.##..#.#.###..#...#...\n"  # noqa: E501
        "..##.####.##..###...#.##....##..###..###...######..##.#...#.###.#.#..####.###..\n"  # noqa: E501
        ".##..#....#.###..#.##.#.#..##.###..###..#.##.....###..##.##.#...#.####....#..#.\n"  # noqa: E501
        "##.####..##.#..###.#..#.####..#..###..###.#.#...##..###..#..##.##.#...#..######"  # noqa: E501
    ),  # noqa: E501
    60: (  # noqa: E501
        ".......................................#.......................................\n"  # noqa: E501
        ".......................................##......................................\n"  # noqa: E501
        ".......................................#.#.....................................\n"  # noqa: E501
        ".......................................####....................................\n"  # noqa: E501
        ".......................................#...#...................................\n"  # noqa: E501
        ".......................................##..##..................................\n"  # noqa: E501
        ".......................................#.#.#.#.................................\n"  # noqa: E501
        ".......................................########................................\n"  # noqa: E501
        ".......................................#.......#...............................\n"  # noqa: E501
        ".......................................##......##..............................\n"  # noqa: E501
        ".......................................#.#.....#.#.............................\n"  # noqa: E501
        ".......................................####....####............................\n"  # noqa: E501
        ".......................................#...#...#...#...........................\n"  # noqa: E501
        ".......................................##..##..##..##..........................\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.........................\n"  # noqa: E501
        ".......................................################........................\n"  # noqa: E501
        ".......................................#...............#.......................\n"  # noqa: E501
        ".......................................##..............##......................\n"  # noqa: E501
        ".......................................#.#.............#.#.....................\n"  # noqa: E501
        ".......................................####............####....................\n"  # noqa: E501
        ".......................................#...#...........#...#...................\n"  # noqa: E501
        ".......................................##..##..........##..##..................\n"  # noqa: E501
        ".......................................#.#.#.#.........#.#.#.#.................\n"  # noqa: E501
        ".......................................########........########................\n"  # noqa: E501
        ".......................................#.......#.......#.......#...............\n"  # noqa: E501
        ".......................................##......##......##......##..............\n"  # noqa: E501
        ".......................................#.#.....#.#.....#.#.....#.#.............\n"  # noqa: E501
        ".......................................####....####....####....####............\n"  # noqa: E501
        ".......................................#...#...#...#...#...#...#...#...........\n"  # noqa: E501
        ".......................................##..##..##..##..##..##..##..##..........\n"  # noqa: E501
        ".......................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.........\n"  # noqa: E501
        ".......................................################################........\n"  # noqa: E501
        ".......................................#...............................#.......\n"  # noqa: E501
        ".......................................##..............................##......\n"  # noqa: E501
        ".......................................#.#.............................#.#.....\n"  # noqa: E501
        ".......................................####............................####....\n"  # noqa: E501
        ".......................................#...#...........................#...#...\n"  # noqa: E501
        ".......................................##..##..........................##..##..\n"  # noqa: E501
        ".......................................#.#.#.#.........................#.#.#.#.\n"  # noqa: E501
        ".......................................########........................########"  # noqa: E501
    ),  # noqa: E501
    90: (  # noqa: E501
        ".......................................#.......................................\n"  # noqa: E501
        "......................................#.#......................................\n"  # noqa: E501
        ".....................................#...#.....................................\n"  # noqa: E501
        "....................................#.#.#.#....................................\n"  # noqa: E501
        "...................................#.......#...................................\n"  # noqa: E501
        "..................................#.#.....#.#..................................\n"  # noqa: E501
        ".................................#...#...#...#.................................\n"  # noqa: E501
        "................................#.#.#.#.#.#.#.#................................\n"  # noqa: E501
        "...............................#...............#...............................\n"  # noqa: E501
        "..............................#.#.............#.#..............................\n"  # noqa: E501
        ".............................#...#...........#...#.............................\n"  # noqa: E501
        "............................#.#.#.#.........#.#.#.#............................\n"  # noqa: E501
        "...........................#.......#.......#.......#...........................\n"  # noqa: E501
        "..........................#.#.....#.#.....#.#.....#.#..........................\n"  # noqa: E501
        ".........................#...#...#...#...#...#...#...#.........................\n"  # noqa: E501
        "........................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#........................\n"  # noqa: E501
        ".......................#...............................#.......................\n"  # noqa: E501
        "......................#.#.............................#.#......................\n"  # noqa: E501
        ".....................#...#...........................#...#.....................\n"  # noqa: E501
        "....................#.#.#.#.........................#.#.#.#....................\n"  # noqa: E501
        "...................#.......#.......................#.......#...................\n"  # noqa: E501
        "..................#.#.....#.#.....................#.#.....#.#..................\n"  # noqa: E501
        ".................#...#...#...#...................#...#...#...#.................\n"  # noqa: E501
        "................#.#.#.#.#.#.#.#.................#.#.#.#.#.#.#.#................\n"  # noqa: E501
        "...............#...............#...............#...............#...............\n"  # noqa: E501
        "..............#.#.............#.#.............#.#.............#.#..............\n"  # noqa: E501
        ".............#...#...........#...#...........#...#...........#...#.............\n"  # noqa: E501
        "............#.#.#.#.........#.#.#.#.........#.#.#.#.........#.#.#.#............\n"  # noqa: E501
        "...........#.......#.......#.......#.......#.......#.......#.......#...........\n"  # noqa: E501
        "..........#.#.....#.#.....#.#.....#.#.....#.#.....#.#.....#.#.....#.#..........\n"  # noqa: E501
        ".........#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#.........\n"  # noqa: E501
        "........#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#........\n"  # noqa: E501
        ".......#...............................................................#.......\n"  # noqa: E501
        "......#.#.............................................................#.#......\n"  # noqa: E501
        ".....#...#...........................................................#...#.....\n"  # noqa: E501
        "....#.#.#.#.........................................................#.#.#.#....\n"  # noqa: E501
        "...#.......#.......................................................#.......#...\n"  # noqa: E501
        "..#.#.....#.#.....................................................#.#.....#.#..\n"  # noqa: E501
        ".#...#...#...#...................................................#...#...#...#.\n"  # noqa: E501
        "#.#.#.#.#.#.#.#.................................................#.#.#.#.#.#.#.#"  # noqa: E501
    ),  # noqa: E501
    91: (  # noqa: E501
        ".......................................#.......................................\n"  # noqa: E501
        "#######################################.#######################################\n"  # noqa: E501
        "......................................#.#......................................\n"  # noqa: E501
        "######################################...######################################\n"  # noqa: E501
        ".....................................#####.....................................\n"  # noqa: E501
        "######################################...######################################\n"  # noqa: E501
        ".....................................#####.....................................\n"  # noqa: E501
        "######################################...######################################\n"  # noqa: E501
        ".....................................#####.....................................\n"  # noqa: E501
        "######################################...######################################\n"  # noqa: E501
        ".....................................#####.....................................\n"  # noqa: E501
        "######################################...######################################\n"  # noqa: E501
        ".....................................#####.....................................\n"  # noqa: E501
        "######################################...######################################\n"  # noqa: E501
        ".....................................#####.....................................\n"  # noqa: E501
        "######################################...######################################\n"  # noqa: E501
        ".....................................#####.....................................\n"  # noqa: E501
        "######################################...######################################\n"  # noqa: E501
        ".....................................#####.....................................\n"  # noqa: E501
        "######################################...######################################\n"  # noqa: E501
        ".....................................#####.....................................\n"  # noqa: E501
        "######################################...######################################\n"  # noqa: E501
        ".....................................#####.....................................\n"  # noqa: E501
        "######################################...######################################\n"  # noqa: E501
        ".....................................#####.....................................\n"  # noqa: E501
        "######################################...######################################\n"  # noqa: E501
        ".....................................#####.....................................\n"  # noqa: E501
        "######################################...######################################\n"  # noqa: E501
        ".....................................#####.....................................\n"  # noqa: E501
        "######################################...######################################\n"  # noqa: E501
        ".....................................#####.....................................\n"  # noqa: E501
        "######################################...######################################\n"  # noqa: E501
        ".....................................#####.....................................\n"  # noqa: E501
        "######################################...######################################\n"  # noqa: E501
        ".....................................#####.....................................\n"  # noqa: E501
        "######################################...######################################\n"  # noqa: E501
        ".....................................#####.....................................\n"  # noqa: E501
        "######################################...######################################\n"  # noqa: E501
        ".....................................#####.....................................\n"  # noqa: E501
        "######################################...######################################"  # noqa: E501
    ),  # noqa: E501
    93: (  # noqa: E501
        ".......................................#.......................................\n"  # noqa: E501
        "######################################.########################################\n"  # noqa: E501
        ".....................................#.#.......................................\n"  # noqa: E501
        "####################################.#.########################################\n"  # noqa: E501
        "...................................#.#.#.......................................\n"  # noqa: E501
        "##################################.#.#.########################################\n"  # noqa: E501
        ".................................#.#.#.#.......................................\n"  # noqa: E501
        "################################.#.#.#.########################################\n"  # noqa: E501
        "...............................#.#.#.#.#.......................................\n"  # noqa: E501
        "##############################.#.#.#.#.########################################\n"  # noqa: E501
        ".............................#.#.#.#.#.#.......................................\n"  # noqa: E501
        "############################.#.#.#.#.#.########################################\n"  # noqa: E501
        "...........................#.#.#.#.#.#.#.......................................\n"  # noqa: E501
        "##########################.#.#.#.#.#.#.########################################\n"  # noqa: E501
        ".........................#.#.#.#.#.#.#.#.......................................\n"  # noqa: E501
        "########################.#.#.#.#.#.#.#.########################################\n"  # noqa: E501
        ".......................#.#.#.#.#.#.#.#.#.......................................\n"  # noqa: E501
        "######################.#.#.#.#.#.#.#.#.########################################\n"  # noqa: E501
        ".....................#.#.#.#.#.#.#.#.#.#.......................................\n"  # noqa: E501
        "####################.#.#.#.#.#.#.#.#.#.########################################\n"  # noqa: E501
        "...................#.#.#.#.#.#.#.#.#.#.#.......................................\n"  # noqa: E501
        "##################.#.#.#.#.#.#.#.#.#.#.########################################\n"  # noqa: E501
        ".................#.#.#.#.#.#.#.#.#.#.#.#.......................................\n"  # noqa: E501
        "################.#.#.#.#.#.#.#.#.#.#.#.########################################\n"  # noqa: E501
        "...............#.#.#.#.#.#.#.#.#.#.#.#.#.......................................\n"  # noqa: E501
        "##############.#.#.#.#.#.#.#.#.#.#.#.#.########################################\n"  # noqa: E501
        ".............#.#.#.#.#.#.#.#.#.#.#.#.#.#.......................................\n"  # noqa: E501
        "############.#.#.#.#.#.#.#.#.#.#.#.#.#.########################################\n"  # noqa: E501
        "...........#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.......................................\n"  # noqa: E501
        "##########.#.#.#.#.#.#.#.#.#.#.#.#.#.#.########################################\n"  # noqa: E501
        ".........#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.......................................\n"  # noqa: E501
        "########.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.########################################\n"  # noqa: E501
        ".......#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.......................................\n"  # noqa: E501
        "######.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.########################################\n"  # noqa: E501
        ".....#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.......................................\n"  # noqa: E501
        "####.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.########################################\n"  # noqa: E501
        "...#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.......................................\n"  # noqa: E501
        "##.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.########################################\n"  # noqa: E501
        ".#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.......................................\n"  # noqa: E501
        ".#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.########################################"  # noqa: E501
    ),
}


def check():
    start = perf_counter()
    deadline = start + 15
    tested = 0
    for rule, expected in EXPECTED.items():
        got = checker.run("solution.py", str(rule))
        tested += 1
        if perf_counter() > deadline:
            too_slow(start, tested)
        if expected != got:
            checker.compare(
                expected,
                got,
                preamble="I checked rule {} by running:".format(rule)
                + "\n\n"
                + checker.code("python3 solution.py {}".format(rule)),
            )

    print(
        "Isn't that nice? Take a close look at "
        "[rule 30](https://wouterkoolen.info/Cellular/Wolfram30.gif), "
        "chaos fighting regularity, how come, with such simple rules?"
    )


if __name__ == "__main__":
    check()
