import numpy as np
from correction_helper import (
    code,
    fail,
    student_code,
    congrats,
    exclude_file_from_traceback,
)

exclude_file_from_traceback(__file__)

CHECKS = {
    (5, 2): np.array(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    ),
    (5, 4): np.array(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    ),
    (5, 5): np.array(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    ),
    (5, 8): np.array(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 2, 0, 2, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    ),
    (9, 1): np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    ),
    (9, 4): np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    ),
    (9, 32): np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 3, 1, 0, 0, 0],
            [0, 0, 1, 2, 1, 2, 1, 0, 0],
            [0, 0, 3, 1, 0, 1, 3, 0, 0],
            [0, 0, 1, 2, 1, 2, 1, 0, 0],
            [0, 0, 0, 1, 3, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    ),
}


def main():
    with student_code():
        from solution import apply_gravity
    for (width, height), expected in CHECKS.items():
        sand = np.zeros((width, width))
        sand[width // 2, width // 2] = height
        with student_code(
            prefix=["While calling your function with:", code(sand), ":"]
        ):
            theirs = apply_gravity(sand)
        if theirs is not None:
            fail(
                f"Your function returned `{theirs!r}` "
                "while you're asked to return `None`."
            )
        if not np.array_equal(sand, expected):
            fail(
                f"In a square of width `{width}`, "
                f"with a single pile of `{height}` grains of sand in the middle, "
                "my output is:",
                code(expected),
                "while yours is:",
                code(sand),
            )
    print(congrats())


if __name__ == "__main__":
    main()
