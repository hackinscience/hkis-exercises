from random import randint

from correction_helper import fail, student_code, exclude_file_from_traceback

exclude_file_from_traceback(__file__)

with student_code():
    from solution import mul


def check():
    seed = randint(100, 100_000)
    for test, expected in (
        ((10, 10), 100),
        ((0, 1, 2, 3, 4, 5), 0),
        ((1, 1), 1),
        ((100, 100), 10_000),
        ((1, seed, 1), seed),
    ):
        with student_code(
            print_prefix=f"When calling `mul({list(test)!r})` it printed:"
        ):
            their = mul(list(test))
        if their != expected:
            fail(
                f"Wrong answer for `mul({list(test)!r})`, expected your "
                f"function to `return {expected}`, but it returned `{their}`"
            )


if __name__ == "__main__":
    check()
