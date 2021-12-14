import string
from itertools import combinations

import correction_helper as ch

ch.exclude_file_from_traceback(__file__)


def check():
    output = ch.run("solution.py")
    if output == "":
        ch.fail(
            "You printed nothing, did you forgot to call the [print]("
            "https://docs.python.org/3/library/functions.html#print) function?"
        )
    combs = "\n".join(a + b for a, b in combinations(string.ascii_lowercase, 2))
    if output == combs:
        ch.fail(
            "I'm not asking for combinations of two letters, "
            "but every two letter pairs. I mean I want `ba` AND `ab`."
        )
    if "ab" not in output and "a b" in output:
        ch.fail("You printed 'a b' instead of 'ab'.", "You printed:", ch.code(output))
    for pair in "ab", "ac", "ad", "ba", "bc", "xy", "xz":
        if pair not in output:
            ch.fail(f"Why not printing `{pair}`?", "You printed:", ch.code(output))
    for dup in "aa", "bb", "mm", "zz", "yy":
        if dup in output:
            ch.fail(
                f"You printed the duplicate: `{dup}`, you should not.",
                "You printed:",
                ch.code(output),
            )
    if len(output.split("\n")) < (26 * 26 - 26):
        ch.fail("Your output seems a bit long.", "You printed:", ch.code(output))
    if len(output.split("\n")) > (26 * 26 - 26):
        ch.fail("Your output seems a bit short.", "You printed:", ch.code(output))


if __name__ == "__main__":
    check()
