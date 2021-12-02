import re
import sys
from pathlib import Path

from correction_helper import code, exclude_file_from_traceback, fail, run

exclude_file_from_traceback(__file__)


def check():
    output = run("solution.py")
    solution = Path("solution.py").read_text()
    if re.match("[^#]*__file__", solution, re.M):
        fail("You don't need __file__, you need sys.argv.")
    if output.endswith("solution.py"):
        sys.exit(0)  # OK :)
    if "[" in output and "]" in output:
        fail(
            "Looks like you printed a list, I just need the program name. Got:",
            code(output),
        )
    fail("Expected to see the program name, got:", code(output))


if __name__ == "__main__":
    check()
