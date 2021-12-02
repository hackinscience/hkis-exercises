import gettext
import subprocess
from pathlib import Path

import correction_helper as ch

ch.exclude_file_from_traceback(__file__)
_ = gettext.translation("check", Path(__file__).parent, fallback=True).gettext


def check():
    output = subprocess.run(
        ["python3", "solution.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    if output.stdout.strip() not in (
        "usage: python3 solution.py OP1 OP2",
        "usage: python3 ./solution.py OP1 OP2",
    ):
        message = _(
            "I expect you to print the usage line when no parameters are given."
        )

        if not output.stdout:
            ch.fail(message, _("(got nothing)"))
        ch.fail(
            message,
            _("Got:"),
            ch.code(output.stdout),
            _("Expected:"),
            ch.code("usage: python3 solution.py OP1 OP2"),
        )
    for i in range(1, 25, 7):
        for j in range(0, 25, 8):
            output = ch.run("solution.py", str(i), str(j))
            if output != str(i + j):
                ch.fail(
                    f"`./solution.py {i} {j}` should give `{i+j}`",
                    _("Got:"),
                    ch.code(output),
                )


if __name__ == "__main__":
    check()
