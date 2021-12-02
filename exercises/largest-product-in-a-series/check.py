import correction_helper as checker

checker.exclude_file_from_traceback(__file__)


def check():
    output = checker.run("solution.py")
    try:
        output = int(output)
    except ValueError:
        checker.fail("Expected you to print an integer.")
    if output > 23514624000:
        checker.fail(
            "Where did your get this number? " "It's bigger that the one I found!"
        )
    if output == 568995840:
        checker.fail(
            """Looks like you only analyzed the 50 first digit of the
it has 1000 digits."""
        )
    if output == 1512:
        checker.fail(
            """That's the answer for the first 50 digits of the 1000 digits number,
and using only 4 digits in a row, not 13."""
        )
    if output < 1000:
        checker.fail(f"I found a WAY BIGGER one (like {output} is the biggest?).")
    if output < 235146240:
        checker.fail("I found a way bigger one.")
    if output < 23514624000:
        checker.fail("I found a bigger one.")


if __name__ == "__main__":
    check()
