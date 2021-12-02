from correction_helper import fail, student_code, exclude_file_from_traceback

exclude_file_from_traceback(__file__)


def main():
    with student_code():
        from solution import blah
    for a_test in ["some", "tests"]:
        with student_code():
            theirs = blah(a_test)
        if theirs is None:
            fail("You are returning `None`, you should return a string.")
        if theirs != "blah":
            fail(
                f"""Blah blah with blah `{a_test}` you failed,
expected `"blah"`, got: `{theirs!r}`"""
            )


if __name__ == "__main__":
    main()
