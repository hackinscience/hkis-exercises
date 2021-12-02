from random import choices
from string import ascii_letters
from dataclasses import dataclass
import correction_helper as checker

checker.exclude_file_from_traceback(__file__)


@dataclass(frozen=True)
class Frame:
    top: str = "-"
    left: str = "|"
    bottom: str = "-"
    right: str = "|"
    top_left: str = "+"
    top_right: str = "+"
    bottom_left: str = "+"
    bottom_right: str = "+"


FANCY_FRAME = Frame("─", "│", "─", "│", "╭", "╮", "╰", "╯")
DOT_FRAME = Frame(".", ".", ".", ".", ".", ".", ".", ".")

FIR = """      *
     ***
    *****
   *******
    *****
   *******
  *********
 ***********
*************
     |||
     |||"""


CHECKS = {
    (
        "It is 11:11:23",
        Frame(),
    ): """
+--------------+
|It is 11:11:23|
+--------------+""".strip(),
    (
        "It is 11:11:23",
        FANCY_FRAME,
    ): """
╭──────────────╮
│It is 11:11:23│
╰──────────────╯""".strip(),
    (
        "It is 11:11:23",
        DOT_FRAME,
    ): """
................
.It is 11:11:23.
................""".strip(),
    (
        FIR,
        Frame(),
    ): """
+-------------+
|      *      |
|     ***     |
|    *****    |
|   *******   |
|    *****    |
|   *******   |
|  *********  |
| *********** |
|*************|
|     |||     |
|     |||     |
+-------------+""".strip(),
    (
        FIR,
        FANCY_FRAME,
    ): """
╭─────────────╮
│      *      │
│     ***     │
│    *****    │
│   *******   │
│    *****    │
│   *******   │
│  *********  │
│ *********** │
│*************│
│     |||     │
│     |||     │
╰─────────────╯""".strip(),
    (
        FIR,
        DOT_FRAME,
    ): """
...............
.      *      .
.     ***     .
.    *****    .
.   *******   .
.    *****    .
.   *******   .
.  *********  .
. *********** .
.*************.
.     |||     .
.     |||     .
...............""".strip(),
}


with checker.student_code():
    from solution import frame_text


def check_return():
    with checker.student_code(
        prefix=[
            "While calling your `frame_text` function as:",
            checker.code("""frame_text("Lorem ipsum", Frame())""", "python"),
        ]
    ):
        their = frame_text("Lorem ipsum", Frame())
    if not isinstance(their, str):
        checker.fail(
            "I expected your `frame_text` function to return a `str`. "
            f"I called `frame_text('Lorem ipsum', Frame())` and got `{their!r}`."
        )


def check_from_dict():
    for (text, frame), expected in CHECKS.items():
        with checker.student_code(
            prefix=[
                "Testing your `frame_text` function as:",
                checker.code(f"frame_text({text!r}, {frame!r})", "python"),
            ]
        ):
            their = frame_text(text, frame)
        checker.compare(
            expected,
            their,
            preamble="\n\n".join(
                [
                    "I called your function with the text:",
                    checker.code(repr(text)),
                    "and the frame:",
                    checker.code(repr(frame)),
                ]
            ),
        )


def check_from_random():
    for text in ["".join(choices(ascii_letters, k=10)) for _ in range(10)]:
        with checker.student_code(
            prefix=[
                "Testing your `frame_text` function as:",
                checker.code(f"frame_text({text!r}, Frame())", "python"),
            ]
        ):
            their = frame_text(text, Frame())
        if text not in their:
            checker.fail(
                f"Calling `frame_text({text!r}, Frame()) "
                "I expected to find the text in your output, but got:",
                checker.code(their),
            )


check_return()
check_from_dict()
check_from_random()
print("Yeah !!! Look how fancy it is:\n")
print(
    checker.code(
        f'''fir = """
      *
     ***
    *****
   *******
    *****
   *******
  *********
 ***********
*************
     |||
     |||"""
frame = {FANCY_FRAME!r}
frame_text(fir, frame)''',
        "python",
    )
)
print("gives:\n")
print(checker.code(frame_text(FIR, FANCY_FRAME)))
