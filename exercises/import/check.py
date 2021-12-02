import correction_helper as checker

checker.exclude_file_from_traceback(__file__)


def check():
    output = checker.run("solution.py")
    if not output:
        checker.fail(
            """Your output is empty, did you forgot to call the
[print](https://docs.python.org/3/library/functions.html#print) function?"""
        )
    if "10888869450418352160768000000" in output:
        print(
            "Wow 27! is `10888869450418352160768000000`, that's... "
            "bigger than I expected, but you're right!"
        )
        return
    try:
        int(output)
    except ValueError:
        checker.fail(
            "I expect a single number (the result of `27!`).",
            "Got:",
            checker.code(output),
        )
    checker.fail(
        "It does not look like the factorial of 27.", "Got:", checker.code(output)
    )


if __name__ == "__main__":
    check()
