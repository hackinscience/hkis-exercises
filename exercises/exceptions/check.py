from pathlib import Path

from correction_helper import code, fail, run, exclude_file_from_traceback

exclude_file_from_traceback(__file__)


def main():
    out = run("solution.py")
    if out != "Not enough parameters.":
        fail(
            "Your error message seems wrong, I tried running your "
            "program without any parameter, expected:",
            code("Not enough parameters."),
            "Got:",
            code(out),
        )
    if "if " in Path("solution.py").read_text():
        fail(
            """Cheater, you tried to use an `if`?

As explicitly mentionned, any use of an `if` in this exercise is strictly prohibited.

Please stick to a simple 4 line answer with a try/except block.
"""
        )
    got = run("solution.py", "12")
    if got != "12":
        fail(
            f"""You should print the first argument when given, I called your
script with `12` as a parameter.

You printed:

{code(got)}
"""
        )
    got = run("solution.py", "12", "13")
    if got != "12":
        fail("You should ONLY print the first argument.")


if __name__ == "__main__":
    main()
