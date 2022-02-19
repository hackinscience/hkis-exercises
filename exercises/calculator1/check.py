from math import isclose
import gettext
import subprocess

import correction_helper as ch

ch.exclude_file_from_traceback(__file__)
gettext = gettext.translation(
    "check", "/opt/hkis-celery/exercises/locale/", fallback=True
).gettext


USAGE = (
    "a_number (an_operator +-*/%^) a_number",
    "usage: solution.py [-h] op_1 operator op_2",
)


def run(file, *args):
    if args:
        args = ["--"] + list(args)
    proc = subprocess.run(
        [
            "python3",
            "-m",
            "friendly",
            "--formatter",
            "correction_helper.friendly_traceback_markdown",
            file,
            *args,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    )
    return proc.stdout.strip()


def test_program(argv, expect):
    got = run("solution.py", *argv)
    if expect is None:
        if got != "input error":
            ch.fail(
                f"Got an unexpected response for `{' '.join(argv)}`, "
                "expected `input error`.",
                "Got:",
                ch.code(got) if "## " not in got else got,
            )
        return
    if expect is False:
        if all(usage not in got for usage in USAGE):
            ch.fail(
                gettext(
                    "I called your program with: `{argv}` "
                    "so I expected a usage line, but got:"
                ).format(" ".join(argv)),
                ch.code(got) if "## " not in got else got,
            )
        return
    if "## " in got:  # Traceback from friendly
        ch.fail(
            f"Got an unexpected response for `{' '.join(argv)}`:",
            got,
        )
    try:
        got = float(got)
    except Exception as err:
        ch.fail(
            f"Cannot parse your result as a number (got {err}).",
            "Given:",
            ch.code(repr(argv)),
            "your program printed:",
            ch.code(got),
        )
    if not isclose(got, expect):
        ch.fail(
            f"Got an unexpected response for `{' '.join(argv)}`, "
            f"expected `{expect!r}`.",
            "Got:",
            ch.code(got),
        )


def check():
    output = run("solution.py")
    if all(usage not in output for usage in USAGE):
        if output == "":
            ch.fail(
                gettext(
                    "With no parameter, I expected your program "
                    "to print the usage line, you printed nothing."
                ),
                gettext(
                    "(Did you forgot to call your function? I'm asking for a program, "
                    "not a function in this exercise)."
                ),
            )
        ch.fail(
            gettext(
                "With no parameter, I expected your program to print the usage "
                "line, but I got:"
            ),
            output if "## " in output else ch.code(output),
        )
    test_program(["1"], False)
    test_program(["1", "2"], False)
    test_program(["5", "+", "5"], 5 + 5)
    test_program(["5", "-", "5"], 0)
    test_program(["5", "*", "5"], 5 * 5)
    test_program(["5", "%", "5"], 5 % 5)
    got = run("solution.py", "2", "^", "32")
    if got == "34":
        ch.fail(
            "Error: got `34` for `2 ^ 32`.",
            "Beware the `^` operator is not the power operator (but `xor`).",
            "The power operator in Python is `**`",
        )

    test_program(["2", "^", "32"], 2**32)
    test_program(["1", "1", "1"], None)
    test_program(["a", "1", "1"], None)
    test_program(["5", "/", "0"], None)


if __name__ == "__main__":
    check()
