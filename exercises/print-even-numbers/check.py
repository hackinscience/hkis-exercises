import sys
import gettext
import re

import correction_helper as checker

checker.exclude_file_from_traceback(__file__)
_ = gettext.translation(
    "check", "/opt/hkis-celery/exercises/locale/", fallback=True
).gettext

with checker.student_code(prefix="While importing your solution:"):
    from solution import print_even_numbers


def check_in_range(start, stop):
    with checker.student_code(print_allowed=None) as run:
        print_even_numbers(start, stop)
    if run.out == "\n".join(str(i) for i in range(start, stop) if i % 2 == 0):
        return  # OK
    message = (
        _("I tried `print_even_numbers({start}, {stop})`").format(
            start=start, stop=stop
        ),
        _("Got:"),
        checker.code(run.out),
    )
    if run.out == "\n".join(str(i) for i in range(start, stop) if i % 2 == 1):
        checker.fail(_("You printed odd numbers, I need even numbers."), *message)
    if run.out == "\n".join(str(i) for i in range(start, stop + 1) if i % 2 == 0):
        checker.fail(
            _(
                "Looks like you included the end bound, but I need your "
                "function to exclude it, exactly like Python's range "
                "function does."
            ),
            *message,
        )
    if run.out == "":
        checker.fail(
            _(
                """I tried `print_even_numbers({start}, {stop})` and it printed nothing,
did you forgot to call the
[print](https://docs.python.org/3/library/functions.html#print) function?"""
            ).format(start=start, stop=stop)
        )
    for line_no, value in enumerate(run.out.split("\n"), start=1):
        try:
            intvalue = int(value)
        except ValueError:
            if line_no == 1:
                if re.match("[0-9]*", value) and " " in value:
                    checker.fail(
                        _("Can't parse the first line as an integer."),
                        _("You need to put a single number per line."),
                        *message,
                    )
            checker.fail(
                _(
                    "One line {line}, you gave something I can't parse as an integer:"
                ).format(line=line_no),
                *message,
            )
        else:
            if intvalue % 2 == 1:
                checker.fail(
                    _(
                        "One line {line}, you gave an **odd** number, "
                        "I need **even** numbers:"
                    ).format(line=line_no),
                    *message,
                )

    if run.out == "\n".join(str(i) for i in range(start + 1, stop)):
        checker.fail(
            _(
                """You displayed all numbers but one,
but I need only [even](https://en.wikipedia.org/wiki/Parity_(mathematics)) numbers!"""
            ),
            *message,
        )
    if run.out == "\n".join(str(i) for i in range(start, stop)):
        checker.fail(
            _(
                """You displayed all numbers (in the right range),
but I need only even numbers."""
            ),
            *message,
        )
    if run.out == "\n".join(str(i) for i in range(start, stop - 1)):
        checker.fail(
            _(
                """You displayed all numbers, but I need only even numbers
(and Python's range is half-open: start is included, stop is excluded!)"""
            ),
            *message,
        )
    if run.out == "\n".join(str(i) for i in range(start, stop - 1) if i % 2 == 0):
        checker.fail(
            _("Python's range is half-open (start included, stop excluded)."), *message
        )
    if run.out == "\n".join(str(i) for i in range(start - 1, stop - 1) if i % 2 == 0):
        checker.fail(
            _("Python's range is half-open (start included, stop excluded)."), *message
        )
    if run.out == "\n".join(str(i) for i in range(start - 1, stop) if i % 2 == 0):
        checker.fail(
            _(
                "You started at {s1} when I called your function with `start={s2}`."
            ).format(s1=start - 1, s2=start),
            *message,
        )
    if run.out.count(" ") > 10 and run.out.count("\n") < 10:
        checker.fail(_("I need one number per line"), *message)
    checker.compare(
        "\n".join(str(i) for i in range(start, stop) if i % 2 == 0),
        run.out,
        preamble=_("I tried to call `print_even_numbers{args!r}`:").format(
            args=(start, stop)
        ),
    )


def check():
    if not callable(print_even_numbers):
        checker.fail(
            "I need you to implement a function called `print_even_numbers`.",
            "Currently, in your code, `print_even_numbers` "
            f"is a {type(print_even_numbers)}.",
        )
    with checker.student_code(print_allowed=None) as run0to10:
        out1 = print_even_numbers(0, 10)
    with checker.student_code(print_allowed=None) as run10to20:
        out2 = print_even_numbers(10, 20)
    outputs = []
    for start in range(0, 10, 2):
        for stop in range(40, 60, 2):
            with checker.student_code(print_allowed=None) as run:
                print_even_numbers(start, stop)
            outputs.append(run.out)
    more = []
    if out1 is not None:
        more.append(
            "Beware: when I called `print_even_numbers(0, 10)` your "
            f"function returned `{out1!r}`, which is unexpected."
            "I just need you to `print` the numbers, not return them."
        )
    if len(set(outputs)) == 1 and out1 == out2:
        checker.fail(
            _(
                "Looks like your function is ignoring the given `start` and `stop` "
                "arguments."
            ),
            _("For example, when I call `print_even_numbers(0, 10)` I get:"),
            checker.code(run0to10.out),
            _("And, when I call `print_even_numbers(10, 20)` I get:"),
            checker.code(run10to20.out),
            *more,
        )
    for start in range(0, 10):
        for stop in range(45, 50):
            check_in_range(start, stop)
    print(_("Nicely done! I love even numbers!"))
    sys.exit(0)


if __name__ == "__main__":
    check()
