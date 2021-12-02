import os
from pathlib import Path

import correction_helper as helper

helper.exclude_file_from_traceback(__file__)


TESTS = (
    ("a", {"a": 1}, 1),
    ("ab", {"a": 1, "b": 1}, 2),
    ("aab", {"a": 2, "b": 1}, 3),
    ("abc", {"a": 1, "b": 1, "c": 1}, 3),
    ("abcdef", {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1}, 6),
    ("ooooooooooooooooooooooooooooooooooo", {"o": 35}, 35),
    ("ooboboooboboboooboboooboooobobobo", {"o": 22, "b": 11}, 33),
    (
        "ababcdlslsoowhlasdfjowjowjoooooooooooo",
        {
            "a": 3,
            "b": 2,
            "c": 1,
            "d": 2,
            "l": 3,
            "s": 3,
            "o": 16,
            "w": 3,
            "h": 1,
            "f": 1,
            "j": 3,
        },
        38,
    ),
)


def main():
    for check_string, freq, total in TESTS:
        Path("words.txt").write_text(check_string, encoding="UTF-8")
        output = helper.run("solution.py")
        for char, count in freq.items():
            should_find = f"{char}: {count/total:.2f}"
            if should_find not in output:
                helper.fail(
                    "Dzzzrrr, wrong!",
                    f"frequency for letter `{char}` in `{repr(check_string)}` "
                    f"is `{should_find}`.",
                    "FYI you gave:",
                    helper.code(output),
                    "(Beware about the format, I really want two decimal digits, "
                    "even if the last one is zero.)",
                )


if __name__ == "__main__":
    try:
        main()
    finally:
        try:
            os.unlink("words.txt")
        except Exception:
            pass
