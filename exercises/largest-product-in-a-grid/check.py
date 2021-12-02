from pathlib import Path

import correction_helper as checker

checker.exclude_file_from_traceback(__file__)


def check():
    output = checker.run("solution.py")
    solution = Path("solution.py").read_text()
    if output == "":
        checker.fail(
            "Your code printed nothing, I need it to print the integer result."
        )
    if "70600674" in solution:
        checker.fail("Are you trying to cheat? Remove this hardcoded value.")
    try:
        output = int(output)
    except ValueError:
        checker.fail(
            "I expect your output to be an integer.", "Got:", checker.code(output)
        )
    if output > 706_006_740:
        checker.fail("It's WAY less, you gave:", checker.code(output))
    if output > 70_600_674:
        checker.fail("It's less, you gave:", checker.code(output))
    if output < 7_060_067:
        checker.fail("It's WAY more, you gave:", checker.code(output))
    if output < 70_600_674:
        checker.fail("It's more, you gave:", checker.code(output))


if __name__ == "__main__":
    check()
