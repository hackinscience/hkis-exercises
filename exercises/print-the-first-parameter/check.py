import gettext
from pathlib import Path

import correction_helper as ch

ch.exclude_file_from_traceback(__file__)
_ = gettext.translation(
    "check", "/opt/hkis-celery/exercises/locale/", fallback=True
).gettext


def check():
    solution = Path("solution.py").read_text()
    if "len(sys.argv) >= 1:" in solution:
        ch.fail(
            """Beware, the program name is *always* given as the fist element of
sys.argv so len(sys.argv) is always greater or equal one.  (Saying so
because I see a `len(sys.argv) >= 1:` in your code...)
"""
        )
    output = ch.run("solution.py").strip()
    messages = []
    usage_is_ok = True
    first_param_is_ok = True
    if output not in (
        "usage: python3 solution.py PARAM",
        "usage: python3 ./solution.py PARAM",
    ):
        messages.extend(
            [
                "You usage line seems wrong expected:",
                ch.code("usage: python3 solution.py PARAM"),
                "got:",
                ch.code(output),
            ]
        )

        usage_is_ok = False

    for test_string in ("foo", "bar", "baz"):
        output = ch.run("solution.py", test_string)
        if output != test_string:
            messages.append(
                f"I called your program with `{test_string!r}` "
                f"(by running `python solution.py {test_string}`), "
                f"so I expected you program to print {test_string}, but it printed:"
            )
            messages.append(ch.code(output))
            first_param_is_ok = False
            break
    if usage_is_ok and not first_param_is_ok:
        ch.fail(
            "Your usage line is OK, but I get unexpected results when "
            "I give an argument to your program:",
            *messages,
        )
    if not usage_is_ok and first_param_is_ok:
        ch.fail(
            "When I give an argument to your program, it works, but with no "
            "argument I don't get the expected result:",
            *messages,
        )
    if not usage_is_ok and not first_param_is_ok:
        ch.fail(*messages)


if __name__ == "__main__":
    check()
