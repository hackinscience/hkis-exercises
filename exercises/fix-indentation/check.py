from pathlib import Path
import gettext

import correction_helper as ch

ch.exclude_file_from_traceback(__file__)
_ = gettext.translation(
    "check", "/opt/hkis-celery/exercises/locale/", fallback=True
).gettext


EXPECTED = """Gonna knock three times:
*knock*
*knock*
*knock*
- Who's there?"""

CODE = """print("Gonna knock three times:")
for i in range(3):
print("*knock*")
print("- Who's there?")
"""


def check():
    solution = Path("solution.py").read_text(encoding="UTF-8")
    if not solution:
        ch.fail(
            _("You emptied the code area, here's what there was, just copy paste it:"),
            ch.code(
                CODE,
                "python",
            ),
        )
    output = ch.run("solution.py")
    if output != EXPECTED:
        ch.fail("The code did not printed exactly what's the exercise is asking for.")
    if solution.count("knock") > 1:
        ch.fail(
            "You modified the code, I see more than 1 `knock` in it now...",
            "You just need to fix indentation of the given code, not modify it.",
            "In case you want to copy-past it to start fresh, here it is:",
            ch.code(CODE, "python"),
        )
    print(ch.congrats())


if __name__ == "__main__":
    check()
