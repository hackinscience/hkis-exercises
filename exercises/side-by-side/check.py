import gettext
from itertools import zip_longest, product
from pathlib import Path

import correction_helper as checker

_ = gettext.translation("check", Path(__file__).parent, fallback=True).gettext


checker.exclude_file_from_traceback(__file__)


TEXTS = [
    "42",
    "Hello world!",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Morbi venenatis, felis nec pretium euismod, est mauris finibus risus, "
    "consectetur laoreet sem enim sed arcu. Maecenas sit amet eleifend sem.",
]


with checker.student_code():
    from solution import sidebyside


def check(left, right, width):
    prefix = [
        "While calling your function as:",
        checker.code(f"`sidebyside({left!r}, {right!r}, width={width})`", "python"),
    ]
    with checker.student_code(prefix=prefix):
        theirs = sidebyside(left, right, width=width)
    if isinstance(theirs, zip_longest):
        checker.fail(
            "You're returning directly the result of `zip_longest`,"
            "but the exercises ask you to return a string.",
            "The result of a `zip_longest` call is not a string, "
            "but an iterable of tuples.",
        )
    if theirs is None:
        checker.fail(
            """Your function is returning `None`, maybe you printed the result
instead of returning it?"""
        )
    if not isinstance(theirs, str):
        checker.fail(
            _("Your function is expected to return a string."),
            _("Got:"),
            checker.code(theirs),
        )
    if "itertools.zip_longest" in theirs:
        checker.fail(
            "Giving a `zip_longest` object to `str()` won't retrieve the "
            "strings inside of it.",
            "You'll have to iterate over it yourself by using something like:",
            checker.code("for left, right in zip_longest(…", "python"),
        )
    expected_column_width = (width - 2 - width % 2) // 2
    their_lines = theirs.split("\n")
    for i, line in enumerate(their_lines, start=1):
        if not line:
            continue
        if line.find("|") != expected_column_width:
            if line.find("|") == -1:
                checker.fail(
                    *prefix,
                    f"On line {i} your function forgot to print the `|`, "
                    "it's mandatory on each lines.",
                    "Your function returned:",
                    checker.code(theirs),
                )
            checker.fail(
                *prefix,
                (
                    f"On line {i} your function misplaced the `|`, "
                    if i > 1
                    else "Your function misplaced the `|`, "
                )
                + f"I expected it to be the {expected_column_width+1}th character "
                "of the line, "
                f"to have two equals columns of {expected_column_width} characters. "
                f"Found it at position {1+line.find('|')}.",
                "Your function returned:",
                checker.code(theirs),
            )
    left_lines = []
    right_lines = []
    for line in their_lines:
        if not line:
            continue
        left_chunk, right_chunk = line.split("|", maxsplit=1)
        left_lines.append(left_chunk.strip())
        right_lines.append(right_chunk.strip())
    left_text = "".join(left_lines).replace(" ", "")
    right_text = "".join(right_lines).replace(" ", "")
    if left.replace(" ", "") != left_text:
        checker.fail(
            "On the left column, your function placed the text "
            "(I removed the spaces to ensure it's not a spacing issue):",
            checker.code(repr(left_text)),
            "While I gave it:",
            checker.code(repr(left.replace(" ", ""))),
            "Your function returned:",
            checker.code(theirs),
        )
    if right.replace(" ", "") != right_text:
        checker.fail(
            "On the right column, your function placed the text ",
            "(I removed the spaces to ensure it's not a spacing issue):",
            checker.code(repr(right_text)),
            "While I gave it:",
            checker.code(repr(right.replace(" ", ""))),
            "Your function returned:",
            checker.code(theirs),
        )


def main():
    for width in 10, 20, 30:
        for left, right in product(TEXTS, repeat=2):
            check(left, right, width)


if __name__ == "__main__":
    main()
