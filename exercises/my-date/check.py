import gettext
from time import sleep
import re
from datetime import datetime
from itertools import zip_longest
from pathlib import Path

from correction_helper import code, exclude_file_from_traceback, fail, run

exclude_file_from_traceback(__file__)
_ = gettext.translation("check", Path(__file__).parent, fallback=True).gettext


def check():
    with open("solution.py") as solution_file:
        solution = solution_file.read()
    output = run("./solution.py")
    if not output:
        fail(_("You printed nothing!"))
    if "2015-09-17" in output:
        fail(_("You printed the example, please print the current date."))
    if "import" not in solution:
        fail(
            _(
                """A good way to import the datetime class from the datetime module is:

    from datetime import datetime
"""
            )
        )
    if "\n" in output:
        fail(_("I expect it to be in a single line, got:"), code(output))
    messages = []
    if "  " in output:
        messages.append(
            "(Beware, I see multiple consecutive spaces in your output, "
            "it may be the issue.)"
        )
    messages.append("Your function printed:")
    messages.append(code(output))
    fmt = r"^Today is [0-9-]{10} and it is [0-9:]{8}\.$"
    if re.match(fmt, output):
        now = datetime.today()
        if not now.strftime("Today is %Y-%m-%d and it is") in output:
            fail(
                _("The date seems wrong, I need the current date."),
                _("Your code prints:"),
                code(output),
                *messages,
            )
        sleep(2)
        output2 = run("./solution.py")
        if output == output2:
            fail(
                "Is this really the current time out of "
                "[datetime.now()](https://docs.python.org/3/library/datetime.html"
                "#datetime.datetime.now)?",
                "It feel... hardcoded.",
            )
        return  # Success

    if not output.startswith("Today is"):
        fail(
            _("The date format seems wrong."),
            _("Got:"),
            code(repr(output)),
            _("It should start with 'Today is'."),
            *messages,
        )

    if "and it is" not in output:
        fail(
            _("The date format seems wrong."),
            _("Got:"),
            code(repr(output)),
            _("I expected to see 'and it is' between the date and the hour."),
            *messages,
        )
    match = re.match(r"^Today is (.*) and it is [0-9:]{8}\.$", output)
    if match:
        fail(
            _("The date part is not correct."),
            _("Got:"),
            code(repr(match.group(1))),  # repr is important here, for leading spaces.
            _("Expected the format: `YYYY-MM-DD`."),
            *messages,
        )

    match = re.match(r"^Today is [0-9-]{10} and it is ([^ ]*)\.$", output)
    if match:
        # The hour part is not correct
        fail(
            _("The hour part is not correct."),
            _("Got:"),
            code(repr(match.group(1))),
            _("Expected the format: `HH:MM:SS`."),
            *messages,
        )

    def verbose(char):
        if char == " ":
            return "a space"
        if char == "[0-9]":
            return "a number"
        if char is None:
            return "the end of the string"
        if char == r"\.":
            return "a dot"
        return repr(char)

    for pos, (given_char, expected_pattern) in enumerate(
        zip_longest(output, "Today is 0000-00-00 and it is 00:00:00.")
    ):
        if expected_pattern is None:  # Too long
            message = "The format seems wrong:\n\n{}\n".format(code(output))
            message += " " * 4 + " " * pos + "^\n"
            message += " " * 4 + "Superfluous character."
            fail(message)
        if expected_pattern == "0":
            expected_pattern = "[0-9]"
        if expected_pattern == ".":
            expected_pattern = r"\."
        if given_char is None or not re.match(expected_pattern, given_char):
            message = "The format seems wrong:\n\n{}\n".format(code(output))
            message += " " * 4 + " " * pos + "^\n"
            message += " " * 4 + "Expected {} here, not {}.".format(
                verbose(expected_pattern), verbose(given_char)
            )
            fail(message)
    if len(output.split()) > 7:
        fail("The date format seems wrong, got: {!r}, looks too long.".format(output))
    if "  " in output:
        fail(
            f"""The date format seems wrong,
beware of double spaces (the print function automatically adds
 a space between each given parameters),
got:

{code(output)}
"""
        )
    fail(f"The date format seems wrong, got:\n\n{code(output)}")


if __name__ == "__main__":
    check()
