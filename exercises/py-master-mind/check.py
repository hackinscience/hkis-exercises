"""
HackInScience - Master Mind
Author: Antoine Mazières
"""

import correction_helper as checker

checker.exclude_file_from_traceback(__file__)


COLORS = {
    4: "ABCD",
    6: "ABCDEF",
    8: "ABCDEFGH",
    26: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
}

with checker.student_code():
    # Just to check the file syntax.
    import solution  # noqa: F401


def test_gen_colors():
    for i, expected in COLORS.items():
        with checker.student_code():
            their = gen_colors(i)
        if their != expected:
            checker.fail(
                f"""`gen_colors({i})` was expected to return `{expected!r}`
but your function returned:""",
                checker.code(their),
            )


def test_gen_code():
    with checker.student_code():
        generated_code = gen_code(5, "ABCD")
    for letter in generated_code:
        if letter not in "ABCD":
            checker.fail("`gen_code` used colors not specified in parameters!")
    if len(generated_code) != 5:
        checker.fail(
            "`gen_code` output is not of the length specified in the parameters."
        )


def test_check_guess():
    with checker.student_code():
        result = check_guess("ABBD", 5, "ABCD")
    if result:
        checker.fail("`check_guess('ABBD', 5, 'ABCD')` result is wrong!")

    with checker.student_code():
        result = check_guess("ABCD", 4, "EFGH")
    if result:
        checker.fail("`check_guess('ABCD', 4, 'EFGH')` result is wrong!")

    with checker.student_code():
        result = check_guess("EFG", 3, "EFGIJ")
    if not result:
        checker.fail("`check_guess('EFG', 3, 'EFGIJ')` result is wrong!")


def test_score_guess():
    tests = [
        (("ABBC", "BCBA"), (1, 3)),
        (("AAAA", "BBBA"), (1, 0)),
        (("ABCD", "EFGH"), (0, 0)),
        (("ABCD", "ABCD"), (4, 0)),
        (("AABB", "ABBA"), (2, 2)),
        (("AAAA", "ABCD"), (1, 0)),
        (("AADA", "ABCD"), (1, 1)),
        (("ADDA", "ABCD"), (1, 1)),
        (("ADDB", "ABCD"), (1, 2)),
    ]
    for args, result in tests:
        with checker.student_code():
            their = score_guess(*args)
        if their != result:
            checker.fail(
                f"`score_guess({args!r})` result is wrong!",
                "I expected",
                checker.code(result),
                "Got:",
                checker.code(their),
            )


with checker.student_code():
    from solution import gen_colors
test_gen_colors()

with checker.student_code():
    from solution import gen_code
test_gen_code()

with checker.student_code():
    from solution import check_guess
test_check_guess()

with checker.student_code():
    from solution import score_guess
test_score_guess()
