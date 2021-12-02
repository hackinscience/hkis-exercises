from pathlib import Path

import correction_helper as ch

ch.exclude_file_from_traceback(__file__)


def check():
    output = ch.run("solution.py")
    try:
        output = int(output)
    except ValueError:
        ch.fail("Expected an integer, got:", ch.code(output))
    if output > 100000007:
        ch.fail("It's less.")
    if output < 10000099:
        ch.fail("It's way more, like 10× more.")
    if output < 100000007:
        ch.fail("It's more.")
    their_code = Path("solution.py").read_text()
    if "100000007" in their_code and len(their_code) < 25:
        ch.fail("I see what you did here.")
    print(ch.congrats())


if __name__ == "__main__":
    check()
