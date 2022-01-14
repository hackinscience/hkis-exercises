import sys
from pathlib import Path

import correction_helper as checker

checker.exclude_file_from_traceback(__file__)


def check():
    solution = Path("solution.py").read_text()
    if solution.count("print") > 9:
        checker.fail(
            """Don't use 10 prints to print 10 numbers, use a for loop instead.
With a for loop, the computer does the job for you,
here you're doing the job for the computer."""
        )
    theirs = checker.run("solution.py")
    mine = "0\n1\n4\n9\n16\n25\n36\n49\n64\n81"
    if theirs == mine:
        sys.exit(0)  # Success!
    if theirs.count("\n") > 100:
        checker.fail(
            "I asked for 10 squares. You printed {} lines!".format(theirs.count("\n"))
        )
    if theirs == "":
        checker.fail(
            """Your code printed nothing, did you forgot to call the
[print](https://docs.python.org/3/library/functions.html#print) function?"""
        )
    if "," in theirs:
        checker.fail(
            "Why did I see a coma? Just asked for one integer per line.",
            "Your full output is:",
            checker.code(theirs),
        )
    their_lines = theirs.split("\n")
    for line_no, line in enumerate(their_lines):
        try:
            int(line)
        except ValueError:
            checker.fail(
                f"""On line {line_no + 1} you gave: `{line}`,
which does not looks like a number.

Just print one value per line, don't print a prefix, a word, an
explanation, nothing.  Just the number.""",
            )
    their_numbers = [int(x) for x in their_lines]
    if not their_numbers:
        checker.fail("Did you forgot to print something?")

    errors = []
    if their_numbers == [x ** 2 for x in range(1, 11)]:
        errors.append("For me the first square is `0 ** 2`, not `1 ** 2`.")
    if their_numbers[:6] == [2 ** x for x in range(6)] or their_numbers[:6] == [
        2 ** x for x in range(1, 7)
    ]:
        errors.append(
            """This looks powers of two (1, 2, 4, 8, 16, 32, 64, ...),
not square numbers (0, 1, 4, 9, 16, ...).

The square of n is n², not 2ⁿ.
"""
        )
    if their_numbers[:6] == [x for x in range(6)]:
        errors.append("This looks like natural numbers, not square numbers.")
    if their_numbers[:6] == [x for x in range(1, 7)]:
        errors.append("This looks like natural numbers, not square numbers.")
    if their_numbers[:6] == [i * 2 for i in range(6)]:
        errors.append("This looks like even numbers, not squares.")
    if their_numbers[:6] == [x ** 10 for x in range(6)]:
        errors.append("This is x<sup>10</sup>, but I need x<sup>2</sup>.")
    if their_numbers[:6] == [x ** 10 for x in range(1, 7)]:
        errors.append("This is x<sup>10</sup>, but I need x<sup>2</sup>.")
    if len(their_numbers) != 10:
        if len(their_numbers) == 1:
            errors.append("I'm asking for 10 values, but you printed a single one.")
        else:
            errors.append(
                f"I'm asking for 10 values, but you printed {len(their_numbers)}"
            )
    if errors:
        checker.fail("\n".join(errors), "You printed:", checker.code(theirs))
    if their_numbers[0] != 0:
        checker.fail(
            "The first square is 0<sup>2</sup> which is 0, but you gave:",
            checker.code(their_numbers[0]),
            "Your full output is:",
            checker.code(theirs),
        )
    for line, number in enumerate(their_numbers):
        if number != line ** 2:
            if line == 0:
                checker.fail(
                    f"""On the first line, I expected {line}<sup>2</sup>, which is {line ** 2},
but you gave {number}.\nYour full output is:""",
                    checker.code(theirs),
                )
            else:
                checker.fail(
                    f"""On line {line + 1}, I expected {line}<sup>2</sup>, which is {line ** 2},
but you gave {number}.\nYour full output is:""",
                    checker.code(theirs),
                )
    if theirs == "0\n1\n4\n9\n16\n25\n36\n49\n64":
        checker.fail("Almost right! I expected 10 numbers, you gave 9.")
    if theirs == "0\n1\n4\n9\n16\n25\n36\n49\n64\n81\n100":
        checker.fail("Almost right! I expected 10 numbers, you gave 11.")
    if len(theirs.split()) < len(mine.split()):
        checker.fail(
            f"""Your answer is a bit short, got only {len(their_lines)} lines,
expected 10."""
        )
    if len(theirs.split()) < len(mine.split()):
        checker.fail(
            f"""All I can say is that it looks too long, got {len(their_lines)} lines,
expected 10."""
        )
    checker.fail(
        "That's wrong, but I don't know why, run your code and check with your eyes?"
    )


if __name__ == "__main__":
    check()
