from sympy.ntheory import factorint
from correction_helper import code, fail, run, exclude_file_from_traceback

exclude_file_from_traceback(__file__)


def factors(n):
    f = factorint(n, multiple=True)
    if n in f:  # I don't care to learn it can be divided by itself.
        f.remove(n)
    return f


def check():
    output = run("solution.py")
    if not output:
        fail("You printed nothing.")
    if output.endswith(","):
        fail(
            "Expected your values to be separated by a coma and a space, "
            "but I don't want a trailing coma.",
            "Your full output is:",
            code(output),
        )
    values = output.split(", ")
    for value in values:
        try:
            intvalue = int(value)
        except ValueError:
            fail(
                f"`{value}` is not an integer. Expected your values to be separated "
                "by a coma and a space, your full output is:",
                code(output),
            )
        if intvalue < 10_000 or intvalue > 10_050:
            fail(
                f"`{intvalue}` is not in the range [10000;10050]!",
                "Your full output is:",
                code(output),
            )
        for factor in factors(intvalue):
            fail(
                f"`{intvalue}` is divisible by {factor}, so it's not a prime!",
                "I need your code to only print prime numbers.",
                "Your full output is:",
                code(output),
            )


if __name__ == "__main__":
    check()
