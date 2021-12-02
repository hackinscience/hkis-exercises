import sys
from pathlib import Path

from correction_helper import code, exclude_file_from_traceback, fail, run

exclude_file_from_traceback(__file__)


def check():
    output = run("solution.py")
    if output == "42":
        print("""`42` is the answer. Well done!""")
        sys.exit(0)
    if output.lower() == "hello world":
        fail(
            """Almost done! You're printing `{out!r}`,
but in this challenge I need you to print `42`.""".format(
                out=output
            )
        )
    solution = Path("solution.py").read_text()
    if any(quote in solution for quote in ('"', "'")) and output == "42":
        fail(
            """Almost done! But I'd prefer you just print the integer `42`
not the string `"42"`.

If you're using quotes, it's not an integer, it's a string.

Visually, for me, once printed, it make no difference, OK, but semantically
it's not the same thing.""",
            "Your code printed:",
            code(output),
        )
    if "print" not in solution and "42" in solution:
        fail(
            """You're not in Python interpreter,
there is no implicit print here,
you have to call the `print` function."""
        )
    if not output:
        fail(
            """Your code printed nothing, did you forgot to call the
[print](https://docs.python.org/3/library/functions.html#print) function?"""
        )
    if "42" in output:
        more = ""
        if output.startswith(" "):
            more = "(Beware, your output starts with a space, remove it.)"
        if output.endswith(" "):
            more = "(Beware, your output ends with a space, remove it.)"
        fail(
            """Almost there! I just need a 42, nothing more, nothing before,
nothing after, only 42.""",
            "Your code printed:",
            code(output),
            more,
        )
    fail(
        """Drzzzt: wrong, I need your code to
[print](https://docs.python.org/3/library/functions.html#print) `42`!""",
        "Your code printed:",
        code(output),
    )


if __name__ == "__main__":
    check()
