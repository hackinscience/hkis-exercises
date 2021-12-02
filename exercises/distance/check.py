from itertools import permutations

import correction_helper as checker
from math import isclose

checker.exclude_file_from_traceback(__file__)

with checker.student_code():
    from solution import dist


def check(test):
    with checker.student_code(
        prefix=[
            "While calling your function as:",
            checker.code(f"dist({test})", "python"),
        ]
    ):
        their = dist(test.copy())

    if their is None:
        checker.fail(
            f"Your function, called as `dist({test!r})` returns `None`.",
            "It is asked to return "
            "the distance between the two furthest apart values.",
        )
    try:
        if not isclose(their, max(test) - min(test)):
            tail = ""
            if len(test) == 1:
                tail = """(There's a single point, so from the point to itself,
    the distance is zero.)"""
            checker.fail(
                f"Biggest distance in `{test!r}` is not the `{type(their)}` `{their}` "
                f"but `{max(test) - min(test)}`",
                tail,
            )
    except TypeError:
        checker.fail(
            "Called `dist({!r})`, expected a number, got:".format(test),
            checker.code(repr(their)),
        )


def main():
    seed = [1, 2, 12.5, 22, 0.01, -9]
    for i in range(2, 6):
        for test in permutations(seed, i):
            check(list(test))
    check([-1, -2, -3])


if __name__ == "__main__":
    main()
