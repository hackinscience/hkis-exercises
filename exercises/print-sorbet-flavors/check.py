import sys
import string
from collections import Counter
from itertools import combinations
from pathlib import Path

from correction_helper import code, exclude_file_from_traceback, fail, run

exclude_file_from_traceback(__file__)

FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]


def check():
    output = run("solution.py")
    solution = Path("solution.py").read_text()
    if output == "":
        if "def " in solution:
            fail("You printed nothing, maybe you forgot to call your function?")
        else:
            fail(
                """You printed nothing, maybe forgot to call `print()`?

You're not in an interpreter, there's no implicit print here."""
            )
    old_expected = "\n".join(i + j for i, j in combinations(string.ascii_lowercase, 2))
    expected = "\n".join(f"{i}, {j}" for i, j in combinations(FLAVORS, 2))
    if output == expected or output == old_expected:
        sys.exit(0)  # Success!
    if "," not in output:
        fail("""Please use comas between the flavors, got:""", code(output))
    if "," in output and ", " not in output:
        fail(
            """Please add a space after the coma (between the flavors),
it's more readable. You printed:""",
            code(output),
        )
    for i, line in enumerate(output.split("\n"), start=1):
        line = line.strip()
        if "," not in line:
            fail(
                f"""On line {i} (`{line}`), there's no coma, it looks wrong.
Your full output:""",
                code(output),
            )
        if ", " not in line:
            fail("You're missing a space after a coma in your output:", code(output))
        if line.count(",") > 1:
            fail(f"Found more than one coma in `{line}`, full output is:", code(output))
        if "'" in line:
            fail(
                f"""Found an quote (`'`) on line `{line}`,
I just want a coma and a space between flavors, no quotes. Full output is:""",
                code(output),
            )
        if line.count(" ") > 1:
            fail(
                f"Found more than one space in `{line}`, full output is:", code(output)
            )
        left, right = line.split(", ")
        if left not in FLAVORS:
            fail(
                f"""Beware, `{left}` is not a known flavor in this restaurant,
please stick to the given list, your full output is:""",
                code(output),
            )
        if right not in FLAVORS:
            fail(
                f"""Beware, `{right}` is not a known flavor in this restaurant,
please stick to the given list, your full output is:""",
                code(output),
            )
        if left == right:
            fail(
                f"On line {i} you're having: `{line}`.",
                "But I explicitly told to not list recipes with twice the same flavor.",
                "Your full output is:",
                code(output),
            )

    their_pairs = set(frozenset(line.split(", ")) for line in output.split("\n"))
    my_pairs = set(frozenset(line.split(", ")) for line in expected.split("\n"))
    for left, right in my_pairs - their_pairs:
        fail(
            f"""Why not proposing `{left}, {right}` (or `{right}, {left}`)?
Your full output is:""",
            code(output),
        )
    for superfluous in their_pairs - my_pairs:
        fail(
            f"Why proposing `{', '.join(superfluous)}`? You full output is:",
            code(output),
        )
    common = Counter(
        [frozenset(line.split(", ")) for line in output.split("\n")]
    ).most_common()
    for (left, right), occurrence in common:
        if occurrence > 1:
            fail(
                f"""You give the pair {left}, {right} twice
(once as `{left}, {right}` and once as `{right}, {left}`).

You should display this duo a single time (any version of it).

Your full output is:""",
                code(output),
            )


if __name__ == "__main__":
    check()
