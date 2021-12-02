import gettext
from math import pi, tau, isclose
from pathlib import Path

import correction_helper as checker

checker.exclude_file_from_traceback(__file__)
_ = gettext.translation(
    "check", "/opt/hkis-celery/exercises/locale/", fallback=True
).gettext


def check_if_they_obey_parameter(circle_perimeter):
    outputs = set()
    for i in range(10):
        i = float(i)
        with checker.student_code(
            prefix=[
                "While calling your function as",
                checker.code(f"circle_perimeter({i})", "python"),
            ]
        ):
            result = circle_perimeter(i)
        outputs.add(result)
    if len(outputs) == 1:
        what_they_compute = outputs.pop() / tau
        checker.fail(
            f"""Looks like your function is ignoring the parameter I give.

Yes, I try your function many times with many many different circles.

And your function always returns the perimeter of a circle with
r ~= {what_they_compute:.2f}."""
        )


def check_result(param, their, partial=False):
    if their is None:
        checker.fail(
            """Your function is returning `None`. You may have printed the result
instead of returning it. Use a `return` statement."""
        )
    if not isinstance(their, float):
        checker.fail(
            "Your function is returning a `{type}`. I expected a `float`.".format(
                type=type(their)
            )
        )
    if isclose(their, pi * param ** 2):
        checker.fail("I'm asking for the perimeter, not the area.")
    if isclose(their, 2 * pi * param ** 2):
        checker.fail(
            "I'm asking for the perimeter, you're mixing the formula of the "
            "and the area."
        )
    if partial:
        return
    if not isclose(their, tau * param):
        checker.fail(
            f"""You gave `{their}` for `circle_perimeter({param})`
            but I expected `{tau * param}`."""
        )


def check():
    solution = Path("solution.py").read_text()
    example = checker.code(
        """def circle_perimeter(r):
    # you code goes here
""",
        "python",
    )

    if "import solution" in solution or "from solution import" in solution:
        checker.fail(
            _("You should declare the `circle_perimeter` function, not import it."),
            _("Use the following syntax to declare the function:"),
            example,
            _("I will import it myself, to test it."),
        )

    if (
        "def " not in solution and "lambda " not in solution
    ) or "circle_perimeter" not in solution:
        checker.fail(
            _("You should declare the `circle_perimeter` function."),
            _("Use the following syntax to declare the function:"),
            example,
        )

    with checker.student_code(
        print_prefix="When I imported your solution, it printed:"
    ):
        from solution import circle_perimeter

    for i in range(10, 100, 7):
        with checker.student_code(
            prefix=[
                "While calling your function as:",
                checker.code(f"circle_perimeter({float(i)!r})"),
            ]
        ):
            their = circle_perimeter(float(i))
        check_result(i, their, partial=True)
    check_if_they_obey_parameter(circle_perimeter)
    for i in range(100, 200, 7):
        with checker.student_code(
            prefix=[
                "While calling your function as:",
                checker.code(f"circle_perimeter({float(i)!r})"),
            ]
        ):
            their = circle_perimeter(float(i))
        check_result(i, their)
    print(_("I tested your function thouroughly and it works like a charm!"))


if __name__ == "__main__":
    check()
