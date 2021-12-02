import gettext
import sys
import subprocess
import re

import correction_helper as checker

checker.exclude_file_from_traceback(__file__)
_ = gettext.translation(
    "check", "/opt/hkis-celery/exercises/locale/", fallback=True
).gettext


def check():
    out = subprocess.run(
        [sys.executable, "solution.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    )
    if re.match("^[0-9.]+$", out.stdout):
        exit(0)
    if not out.stdout:
        checker.fail(
            _("Your code printed nothing. I expected to get the Github API response.")
        )
    if out.stdout[0] == "{":
        exit(0)  # There's internet connectivity (locally using pytest maybe).
    if "socket.gaierror" in out.stdout and "NewConnectionError" in out.stdout:
        checker.fail(
            "In case there's no internet connectivity I need your program to print:",
            "> No internet connectivity.",
            "But it prints:",
            checker.code(out.stdout),
        )
    checker.compare("No internet connectivity.", out.stdout.strip())


if __name__ == "__main__":
    check()
