from pathlib import Path
import gettext
import correction_helper as checker
import numpy as np

_ = gettext.translation("check", Path(__file__).parent, fallback=True).gettext
checker.exclude_file_from_traceback(__file__)

checker.run("solution.py")


def check_part_1():
    with checker.student_code():
        from solution import init_grid

    with checker.student_code():
        grid = init_grid()
    rand = set()
    for _i in range(5):
        rand.add(np.array_equal(grid, init_grid()))
    if rand == set([True]):
        checker.fail("Your `init_grid` does not looks like to place points randomly.")
    if not isinstance(grid, np.ndarray):
        checker.fail("Your `init_grid` function is required to return an `np.ndarray`.")
    if not grid.shape == (4, 4):
        checker.fail("Your `init_grid` should return an array of shape 4×4.")
    if not len(np.where(grid == 0)[0]) == 14:
        checker.fail(
            "Your `init_grid` should produce a grid with exactly two elements.",
            _("Got:"),
            checker.code(grid),
        )
    if not grid.sum().sum() == 4:
        checker.fail(
            """Your `init_grid` should place two `2`s, here's a grid your `init_grid`
gave to me:""",
            checker.code(repr(grid)),
        )


def check_part_2():
    with checker.student_code():
        from solution import add_new, init_grid

    with checker.student_code():
        grid = init_grid()
        grid = add_new(grid)
    if not len(np.where(grid == 0)[0]) == 13:
        checker.fail(
            """I tried `add_new(init_grid())`, expected to see 3 elements,
here's what I got:""",
            checker.code(repr(grid)),
        )
    sums = set()
    for _i in range(42):
        grid = init_grid()
        grid = add_new(grid)
        sums.add(grid.sum().sum())
    if not (6 in sums and 8 in sums):
        checker.fail(
            "Tried your `add_new` 20 times, and found it never added a `4`, strange..."
        )
    if not isinstance(grid, np.ndarray):
        checker.fail(
            "Your `add_new(grid)` function is required to return an `np.ndarray`."
        )


def check_part_3():
    with checker.student_code():
        from solution import rollin_row

    i_rows = [
        [0, 2, 0, 2],
        [2, 2, 4, 4],
        [0, 0, 0, 2],
        [4, 2, 0, 4],
        [4, 4, 8, 8],
        [4, 4, 8, 0],
    ]
    o_rows = [
        [4, 0, 0, 0],
        [4, 8, 0, 0],
        [2, 0, 0, 0],
        [4, 2, 4, 0],
        [8, 16, 0, 0],
        [8, 8, 0, 0],
    ]
    for row in zip(i_rows, o_rows):
        got = list(rollin_row(list(row[0])))
        if row[1] != got:
            checker.fail(
                f"`rollin_row({row[0]})` should return `{row[1]}`, got: `{got}`."
            )


def check_part_4():
    with checker.student_code():
        from solution import rollin

    grid = [[8, 0, 16, 0], [4, 0, 0, 0], [4, 0, 2, 0], [0, 32, 2, 0]]
    tests = {
        "l": np.asarray([[8, 16, 0, 0], [4, 0, 0, 0], [4, 2, 0, 0], [32, 2, 0, 0]]),
        "r": np.asarray([[0, 0, 8, 16], [0, 0, 0, 4], [0, 0, 4, 2], [0, 0, 32, 2]]),
        "u": np.asarray([[8, 32, 16, 0], [8, 0, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
        "d": np.asarray([[0, 0, 0, 0], [0, 0, 0, 0], [8, 0, 16, 0], [8, 32, 4, 0]]),
    }
    for direction, expected in tests.items():
        with checker.student_code():
            got = rollin(np.asarray(grid), direction)
        if not np.array_equal(got, expected):
            checker.fail(
                f"`rollin({np.asarray(grid)}, {direction!r})` expected to give:",
                checker.code(expected),
                "got:",
                checker.code(got),
            )


def check():
    for _ in range(10):
        check_part_1()
    check_part_2()
    check_part_3()
    check_part_4()


if __name__ == "__main__":
    check()
