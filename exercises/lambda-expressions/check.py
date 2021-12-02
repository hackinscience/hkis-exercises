import re
from pathlib import Path

import correction_helper as checker

checker.exclude_file_from_traceback(__file__)


with checker.student_code():
    from solution import filtered


def check():
    expected = []
    expected.append(", ".join(str(i) for i in range(101) if i % 3 == 0))
    expected.append(", ".join(str(i) for i in range(101) if i % 5 == 0))
    expected.append(", ".join(str(i) for i in range(101) if i % 15 == 0))
    expected = "\n".join(expected)

    output = checker.run("./solution.py")
    solution = Path("./solution.py").read_text(encoding="UTF-8")
    if not re.search(r"def\s+filtered\s*\(", solution):
        checker.fail("You should declare a `filtered` function.")
    if "lambda " not in solution:
        checker.fail("Where are your lambda expressions?")
    for line_no, (my_line, their_line) in enumerate(
        zip(expected.split("\n"), output.split("\n"))
    ):
        if my_line != their_line:
            if "[" in their_line:
                checker.fail(
                    f"""On line {line_no + 1}, I expected numbers separated by comas,
you printed a Python list representation."""
                )
    checker.compare(expected, output)
    with checker.student_code(
        prefix=["While calling your function as `filtered([], lambda x: x)`"]
    ):
        their = filtered([], lambda x: x)
    if isinstance(their, str):
        checker.fail(
            """Your `filtered` function should not return a string.

The three prints should do the formatting, but your `filtered` function should just
return a `list`.

I tried `filtered([], lambda x: x)` and got:""",
            checker.code(repr(their)),
        )
    if their is None:
        checker.fail(
            "Your `{}` function, returned `None`, it should return an iterable.".format(
                "filtered"
            )
        )
    if list(their) != []:
        checker.fail("Filtering an empty list won't work for me")
    with checker.student_code(
        prefix=[
            "While calling your function as:",
            checker.code("filtered([1, 2, 3], lambda x: True)", "python"),
        ]
    ):
        their = filtered([1, 2, 3], lambda x: True)
    if list(their) == ["1", "2", "3"]:
        checker.fail(
            """`filtered([1, 2, 3], lambda x: True)` is expected to return 3 ints,
not 3 strings."""
        )
    with checker.student_code(
        prefix=[
            "While calling your function as:",
            checker.code("filtered([1, 2, 3], lambda x: True)", "python"),
        ]
    ):
        their = filtered([1, 2, 3], lambda x: True)
    if list(their) != [1, 2, 3]:
        checker.fail(
            "`filtered([1, 2, 3], lambda x: True)` give an unexpected result.",
            "Expected:",
            checker.code("[1, 2, 3]"),
            "Got:",
            checker.code(str(list(their))),
        )
    with checker.student_code(
        prefix=[
            "While calling your function as:",
            checker.code("filtered([1, 2, 3], lambda x: False)", "python"),
        ]
    ):
        their = filtered([1, 2, 3], lambda x: False)
    if list(their) != []:
        checker.fail("filtered([1, 2, 3], lambda x: False) won't work for me")


if __name__ == "__main__":
    check()
