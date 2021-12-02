from correction_helper import (
    exclude_file_from_traceback,
    fail,
    student_code,
    code,
    congrats,
)

exclude_file_from_traceback(__file__)


with student_code():
    from solution import perfect_shuffle


CHECKS = (
    ([], []),
    ([1, 2], [1, 2]),
    ([0, 1], [0, 1]),
    ([1, 2, 3, 4], [1, 3, 2, 4]),
    ([0, 1, 2, 3], [0, 2, 1, 3]),
    ([1, 2, 3, 4, 5, 6], [1, 4, 2, 5, 3, 6]),
    ([0, 1, 2, 3, 4, 5], [0, 3, 1, 4, 2, 5]),
    ([1, 2, 3, 4, 5, 6, 7, 8], [1, 5, 2, 6, 3, 7, 4, 8]),
    ([0, 1, 2, 3, 4, 5, 6, 7], [0, 4, 1, 5, 2, 6, 3, 7]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 6, 2, 7, 3, 8, 4, 9, 5, 10]),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 5, 1, 6, 2, 7, 3, 8, 4, 9]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 7, 2, 8, 3, 9, 4, 10, 5, 11, 6, 12]),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 6, 1, 7, 2, 8, 3, 9, 4, 10, 5, 11]),
    (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        [1, 8, 2, 9, 3, 10, 4, 11, 5, 12, 6, 13, 7, 14],
    ),
    (
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        [0, 7, 1, 8, 2, 9, 3, 10, 4, 11, 5, 12, 6, 13],
    ),
    (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
        [1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15, 8, 16],
    ),
    (
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [0, 8, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15],
    ),
    (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        [1, 10, 2, 11, 3, 12, 4, 13, 5, 14, 6, 15, 7, 16, 8, 17, 9, 18],
    ),
    (
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
        [0, 9, 1, 10, 2, 11, 3, 12, 4, 13, 5, 14, 6, 15, 7, 16, 8, 17],
    ),
)


def test(deck, expected):
    with student_code(
        prefix=[
            "While calling your function as:",
            code(f"perfect_shuffle({deck!r})", "python"),
        ]
    ):
        shuffeled = perfect_shuffle(deck)
    if expected != shuffeled:
        fail(
            "Expected `perfect_shuffle({})` to return `{}`, got `{}`".format(
                deck, expected, shuffeled
            )
        )
    if deck and shuffeled is deck:
        fail(
            f"""You modified the `{deck!r}` deck inplace, you should not,
just return a new one."""
        )


def check():
    for deck, expected in CHECKS:
        test(deck, expected)
    print(congrats())


if __name__ == "__main__":
    check()
