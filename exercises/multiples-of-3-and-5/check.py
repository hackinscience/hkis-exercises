from pathlib import Path

import correction_helper as checker

checker.exclude_file_from_traceback(__file__)


def check():
    source = Path("solution.py").read_text()
    if "233168" in source:
        checker.fail("Are you cheating? Remove this hardcoded value.")
    output = checker.run("solution.py")
    if not output:
        checker.fail(
            "You're printing nothing. Did you forgot to call the `print` function?"
        )
    try:
        output = int(output)
    except ValueError:
        try:
            output = float(output)
        except ValueError:
            checker.fail(
                """I expect your output to be the **sum** of all natural numbers
below 1000 (<1000) that are multiples of 3 or 5.

(in other words: A single integer)""",
                "Got:",
                checker.code(output),
            )
        else:
            checker.fail(
                """I expect your output to be a sum of natural numbers,
it has to be an integer. You gave a `float`.""",
                "Got:",
                checker.code(output),
            )
    trees = sum(range(0, 1000, 3))
    fives = sum(range(0, 1000, 5))

    expected = sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)
    if output == expected:
        return  # OK
    if output == sum(i for i in range(100) if i % 3 == 0 or i % 5 == 0):
        checker.fail("Those are multiples of 3 or 5 below 100.")
    if output == sum(i for i in range(1000) if i % 3 == 0 and i % 5 == 0):
        checker.fail(
            """This is the sum of numbers multiple of tree and five (15, 30, 45, ...)
I need multiples of three and multiples of five (3, 5, 6, 9, 10, 12, 15, 18, ...)."""
        )
    if output == sum(range(0, 102, 2)):
        checker.fail(
            "Did you just summed even numbers <= 100 instead of multiples of 3 or 5?"
        )
    if output == 166833 and "&" in source:
        checker.fail(
            """Looks like you used & instead of and, but they has different meanings
(`&` works on bits, use `and` in this case)."""
        )
    if output in (66, 67):
        checker.fail(
            f"""It's more (you gave {output}, which looks like the **count**
of multiples of **15** in the given range)."""
        )
    if output == sum(i for i in range(1001) if i % 3 == 0 or i % 5 == 0):
        checker.fail("Beware, I asked for `1000 excluded` not `1000 included`.")
    if output == trees + fives:
        checker.fail("You counted 15 twice (and many others)")
    if output > expected:
        checker.fail("It's less")
    if output < expected:
        checker.fail(f"It's more (you gave {output})")


if __name__ == "__main__":
    check()
