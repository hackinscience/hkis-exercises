import sys
import gettext
from pathlib import Path

import correction_helper as ch

ch.exclude_file_from_traceback(__file__)
_ = gettext.translation("check", Path(__file__).parent, fallback=True).gettext


def check():
    with open("solution.py") as f:
        solution = "\n".join(
            line for line in f.read().lower().split("\n") if not line.startswith("#")
        )
    if not solution:
        ch.fail(
            _(
                """You wrote no code (in the black area, which is a code editor).

You should write a line of code which prints `Hello world!` when
executed, if you really don't know how to start, you should first read
the [tutorial](https://docs.python.org/3/tutorial/)."""
            )
        )
    if solution.strip().replace("!", "") == "hello world":
        ch.fail(
            _(
                """You need to use the
[print](https://docs.python.org/3/library/functions.html#print) function
in order to make Python print something."""
            )
        )
    if solution.strip().replace("!", "") == "print(hello world)":
        ch.fail(
            _(
                """"Hello world!" is a string, in Python strings should be enclosed
 in quotes or double quotes.
See the [strings tutorial](
https://docs.python.org/3/tutorial/introduction.html#strings)"""
            )
        )
    output = ch.run("solution.py")
    clean_output = output.lower().replace(",", "").replace("!", "")
    if "hello world" in clean_output:
        print(
            "Yep! This code prints:",
            ch.code(output),
            "You can try the next exercise by clicking the blue button below.",
            sep="\n\n",
        )
        sys.exit(0)
    if "print" not in solution and "hello" in solution:
        ch.fail(
            _(
                """You're not in an
[interactive Python interpreter](
https://docs.python.org/3/tutorial/interpreter.html#interactive-mode),
your code is tested in a file,
so there is no implicit print here.

You have to use the [print](https://docs.python.org/3/library/functions.html#print)
function."""
            )
        )
    message = _(
        'You should print "Hello World!", not something else to validate this exercise.'
    )

    if not output:
        ch.fail(message + "\n\n" + _("You printed nothing :("))
    else:
        ch.fail(message, _("You printed:"), ch.code(output))


if __name__ == "__main__":
    check()
