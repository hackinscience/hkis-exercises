import correction_helper as checker

checker.exclude_file_from_traceback(__file__)

EXPECTED = """222288
222303
222304
222319
222327
222331
222333
222334
222337
222338
222340
222344
222352
222367
222368"""


def check():
    output = checker.run("solution.py")
    if output == "100\n103\n104\n107\n109":
        checker.fail(
            """I'm not asking pernicious numbers in `range(100, 110)`
but in `range(222281, 222381)`."""
        )
    checker.compare(EXPECTED, output)


if __name__ == "__main__":
    check()
