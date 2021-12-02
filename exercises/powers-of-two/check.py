from pathlib import Path
import sys

import correction_helper as ch

ch.exclude_file_from_traceback(__file__)


def check():
    solution = Path("solution.py").read_text()
    if solution.count("print") > 9:
        return """Don't use 10 prints to print 10 numbers, use a for loop instead.
With a for loop, the computer does the job for you,
here you're doing the job for the computer."""
    theirs = ch.run("solution.py")
    mine = "1\n2\n4\n8\n16\n32\n64\n128\n256\n512"
    if theirs == mine:
        print(ch.congrats())
        sys.exit(0)
    if theirs.count("\n") > 100:
        ch.fail(
            "I asked for 10 powers of two. You printed {} lines!".format(
                theirs.count("\n")
            )
        )
    if theirs == "":
        ch.fail(
            """Your code printed nothing, did you forgot to call the
[print](https://docs.python.org/3/library/functions.html#print) function?"""
        )
    if "," in theirs:
        ch.fail(
            "Why did I see a coma? Just asked for one integer per line.",
            "Your full output is:",
            ch.code(theirs),
        )
    their_lines = theirs.split("\n")
    for line_no, line in enumerate(their_lines):
        try:
            int(line)
        except ValueError:
            ch.fail(
                f"""On line {line_no + 1} you gave: `{line}`,
which does not looks like a number.

Just print one value per line, don't print a prefix, a word, an
explanation, nothing.  Just the number.""",
            )
    their_numbers = [int(x) for x in their_lines]
    if not their_numbers:
        ch.fail("Did you forgot to print something?")

    errors = []
    if their_numbers == [2 ** x for x in range(1, 11)]:
        errors.append("For me the first power of two is `2 ** 0`, not `2 ** 1`.")
    if their_numbers[:6] == [x ** 2 for x in range(6)] or their_numbers[:6] == [
        x ** 2 for x in range(1, 7)
    ]:
        errors.append(
            """This looks like square numbers (0, 1, 4, 9, 16, ...),
not powers of two (1, 2, 4, 8, 16, 32, 64, ...).

The square of n is n², but I need two to the power of n, which is 2ⁿ.
"""
        )
    if their_numbers[:6] == [x for x in range(6)]:
        errors.append("This looks like natural numbers, not powers of two.")
    if their_numbers[:6] == [x for x in range(1, 7)]:
        errors.append("This looks like natural numbers, not powers of two.")
    if their_numbers[:6] == [i * 2 for i in range(6)]:
        errors.append("This looks like even numbers, not powers of two.")
    if their_numbers[:6] == [x ** 10 for x in range(6)]:
        errors.append("This is x<sup>10</sup>, but I need 2<sup>x</sup>.")
    if their_numbers[:6] == [x ** 10 for x in range(1, 7)]:
        errors.append("This is x<sup>10</sup>, but I need 2<sup>x</sup>.")
    if len(their_numbers) != 10:
        if len(their_numbers) == 1:
            errors.append("I'm asking for 10 values, but you printed a single one.")
        else:
            errors.append(
                f"I'm asking for 10 values, but you printed {len(their_numbers)}"
            )
    if errors:
        ch.fail("\n".join(errors), "You printed:", ch.code(theirs))
    if their_numbers[0] != 1:
        ch.fail(
            "The first power of two is 2<sup>0</sup> which is 1, but you gave:",
            ch.code(their_numbers[0]),
            "Your full output is:",
            ch.code(theirs),
        )
    for line, number in enumerate(their_numbers):
        if number != 2 ** line:
            if line == 0:
                ch.fail(
                    f"On the first line, I expected 2<sup>{line}</sup>, "
                    f"which is {2 ** line}, "
                    f"but you gave {number}.",
                    "Your full output is:",
                    ch.code(theirs),
                )
            else:
                ch.fail(
                    f"On line {line + 1}, I expected 2<sup>{line}</sup>, "
                    f"which is {2 ** line}, "
                    f"but you gave {number}.",
                    "Your full output is:",
                    ch.code(theirs),
                )
    if theirs == "1\n2\n4\n8\n16\n32\n64\n128\n256":
        ch.fail("Almost right! I expected 10 numbers, you gave 9.")
    if theirs == "1\n2\n4\n8\n16\n32\n64\n128\n256\n512\n1024":
        ch.fail("Almost right! I expected 10 numbers, you gave 11.")
    if len(theirs.split()) < len(mine.split()):
        ch.fail(
            f"""Your answer is a bit short, got only {len(their_lines)} lines,
expected 10."""
        )
    if len(theirs.split()) < len(mine.split()):
        ch.fail(
            f"""All I can say is that it looks too long, got {len(their_lines)} lines,
expected 10."""
        )
    ch.fail(
        "That's wrong, but I don't know why, run your code and check with your eyes?"
    )


if __name__ == "__main__":
    check()
