import os
from pathlib import Path

from correction_helper import code, fail, run, exclude_file_from_traceback

exclude_file_from_traceback(__file__)


def check(check_string):
    Path("words.txt").write_text(check_string)
    output = run("solution.py")
    if Path("words.txt").read_text() != check_string:
        fail("Have you modified my file? Please don't write to it, just read.")
    try:
        output = int(output)
    except ValueError:
        fail("I expect your output to be an integer, got:", code(output))
    expected = sum(1 if char == "e" else 0 for char in check_string)
    if output != expected:
        fail(
            "I don't get the same count...",
            "In my `words.txt` file I had:",
            code(check_string),
            "In it you found {} `e`s.".format(output),
            "But I think there is {}".format(expected),
        )


if __name__ == "__main__":
    try:
        for check_string in (
            "The interpreter’s line-editing features include " "interactive editing",
            "Return the absolute value of a number.",
            "Return True if any element of the iterable is true. "
            "If the iterable is empty, return False.",
            "As repr(), return a string containing a printable "
            "representation of an object, but escape the non-ASCII "
            "characters in the string returned by repr() using "
            "\\x, \\u or \\U escapes.",
        ):
            check(check_string)
    finally:
        try:
            os.unlink("words.txt")
        except Exception:
            pass
