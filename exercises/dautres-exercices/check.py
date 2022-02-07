from pathlib import Path
import sys

from correction_helper import exclude_file_from_traceback

exclude_file_from_traceback(__file__)

print(
    """This is not really an exercise, it has no check,
#sry, there's just no way to « do » it.

But if you really want to train yourself at writing more Python,
I have one for you: contribute to open-source software, and maybe
start by contributing to HackInScience to help other learn?
"""
)


solution = Path("solution").read_text(encoding="UTF-8")

sys.exit(solution != "# Yeah, but… I'm reading the source!")
