import sys

import correction_helper as checker

checker.exclude_file_from_traceback(__file__)


def check():
    output = checker.run("solution.py")
    if not output:
        checker.fail(
            """Your code printed nothing, did you forgot to call the
[print](https://docs.python.org/3/library/functions.html#print) function?

As a reminder: to display for example the result of `60 × 60` the syntax is:

```python
print(60 * 60)
```
"""
        )
    output_lines = output.split("\n")
    output_line = output_lines[0]
    if output_line.replace(" ", "") == "60*60*24*365":
        checker.fail(
            f"You're printing `{output_line}`, while I expect you to "
            "print the result of this.",
            "I bet you used quotes, which are used to buid strings, "
            "where you should have not, to let Python interpret the values:",
            "`print(2 * 2)` prints `4`.",
            '`print("2 * 2")` prints `2 * 2`.',
        )
    if str(60 * 60 * 24 * 365) in output:
        print(
            f"Looks good to me! {60 * 60 * 24 * 365} seconds per year, that's a lot!!"
        )
        sys.exit(0)
    if len(output_lines) > 1:
        checker.fail(
            f"Expected a single line (the result), got {len(output_lines)}"
            "lines, you printed:",
            checker.code(output),
        )
    try:
        output_int = int(output_line)
    except ValueError:
        try:
            output_int = int(float(output_line))
        except ValueError:
            checker.fail(
                "Expected your program to display a number "
                f"(that Python can read as a number), got `{output_line}`."
            )
    if output_int == 60 * 60 * 24:
        checker.fail(
            f"You printed {60 * 60 * 24} (60 × 60 × 24), this is the number of "
            "seconds in a day. I need the number of seconds in a year of **365** days."
        )
    if output_line.startswith(" "):
        checker.fail(
            "Why do your output starts with a space?",
            "You printed:",
            checker.code(output),
        )
    message = ["This is not the correct answer. You printed:", checker.code(output)]
    if output_int > 60 * 60 * 24:
        days, rest = divmod(output_int, 60 * 60 * 24)
        if rest:
            message.append("It's roughly equivalent to {} days.".format(days))
        else:
            message.append("It's {} days (I want `365` days).".format(days))
    checker.fail(*message)


if __name__ == "__main__":
    check()
