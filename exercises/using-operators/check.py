import math
import sys

import correction_helper as checker

checker.exclude_file_from_traceback(__file__)


def check():
    output = checker.run("solution.py")
    if "3.1415926535897" in output:
        # OK the result is here, let's be cool, it's OK.
        print("Looks good to me! (This is a good `pi` approximation!)")
        sys.exit(0)
    if output == """3.141592653589793\n1.61803398875""":
        print(
            "This was the answer for an old version of this exercise, "
            "let's say it's OK ☺."
        )
        sys.exit(0)
    if not output:
        checker.fail(
            "Your code printed nothing, did you forgot to call the "
            "[print](https://docs.python.org/3/library/functions.html#print) function?",
            "As a reminder: to display the result of `1 / 2` the syntax is:",
            checker.code("print(1 / 2)", "python"),
        )
    output_lines = output.split("\n")
    if len(output_lines) > 1:
        checker.fail(
            f"Expected a single line (the result), got {len(output_lines)} "
            "lines, you printed:",
            checker.code(output),
        )
    output_line = output_lines[0]
    if output_line.replace(" ", "") == "8958937768937/2851718461558":
        checker.fail(
            f"You're printing `{output_line}`, while I expect you to "
            "print the result of this.",
            "I bet you used quotes, which are used to buid strings, "
            "where you should have not, to let Python interpret the values:",
            "`print(2 * 2)` prints `4`.",
            '`print("2 * 2")` prints `2 * 2`.',
        )
    try:
        output_float = float(output_line)
    except ValueError:
        checker.fail(f"Expected a number, got `{output_line}`.")
    if math.isclose(math.pi, output_float):
        print("Looks good to me! (This is a good `pi` approximation!)")
        sys.exit(0)
    if not math.isclose(output_float, 245850922 / 78256779) and not math.isclose(
        output_float, 8958937768937 / 2851718461558
    ):
        checker.fail(
            f"""This is not the right number, got `{output_line}`.""",
            "(You should copy-paste the numbers to avoid errors in them, they're big.)",
        )
    if output_line.startswith(" "):
        checker.fail(
            "Why do your output starts with a space?",
            "You printed:",
            checker.code(output),
        )
    checker.fail("This is not the correct answer. You printed:", checker.code(output))


if __name__ == "__main__":
    check()
