from random import randint
from unicodedata import name
import correction_helper as checker

checker.exclude_file_from_traceback(__file__)

with checker.student_code():
    from solution import list_pretty_print


def check_result_contains(prefix, stdout, a_list):
    for value in a_list:
        if str(value) not in stdout:
            checker.fail(
                *prefix,
                f"I expected to see at least {value} in the output, "
                "bit I don't see it, your function printed:",
                checker.code(stdout),
            )


def check_number_of_comas(prefix, stdout, a_list):
    for lineno, line in enumerate(stdout.split("\n"), start=1):
        if line.count(",") > 4:
            checker.fail(
                *prefix,
                f"With at most 5 values per line, I expect at most 4 comas per line."
                f"Found {line.count(',')} comas on line {lineno}:",
                checker.code(stdout),
            )


def check_used_characters(prefix, stdout, a_list):
    for char in stdout:
        if char not in "0123456789 ,\r\n":
            checker.fail(
                *prefix,
                f"You used a `{char}` ({name(char)}), "
                "I just need the numbers, some comas, and some newlines.",
                "Here's your full output:",
                checker.code(stdout),
            )


def check_spaces_at_end_of_line(prefix, stdout):
    for lineno, line in enumerate(stdout.split("\n"), start=1):
        if line.endswith(" "):
            checker.fail(
                *prefix,
                f"At the end of line {lineno}, your function prints a space.",
                "It look like this:",
                checker.code(repr(line)),
                "(And no, I don't like spaces at end of lines...)",
                "Here's what your function printed:",
                checker.code(stdout),
            )


def check_round_trip(prefix, stdout, a_list):
    items = stdout.replace(",", " ").split()
    items = [int(item) for item in items]
    if len(items) < len(a_list):
        checker.fail(
            *prefix,
            "I expected to find **all** my values, "
            "looks like your code forgot some ☹.",
            "Here's what your function printed:",
            checker.code(stdout),
        )
    if len(items) > len(a_list):
        checker.fail(
            *prefix,
            "I expected to find the values from the given parameter, "
            "looks like your code added some??",
            "Here's what your function printed:",
            checker.code(stdout),
        )
    if items != a_list:
        checker.fail(
            *prefix,
            "I expected to find my values in the same order and all, "
            "looks like you messed-up something.",
            "Here's what your function printed:",
            checker.code(stdout),
        )


def main():
    for width in range(50):
        test_list = [randint(0, 100_000) for _ in range(width)]
        prefix = [
            "While calling your function as",
            checker.code(f"list_pretty_print({test_list!r})", "python"),
        ]
        with checker.student_code(
            prefix=prefix,
            print_allowed=None,  # Capture
        ) as call:
            list_pretty_print(test_list.copy())

        check_used_characters(prefix, call.out, test_list)
        check_result_contains(prefix, call.out, test_list)
        check_number_of_comas(prefix, call.out, test_list)
        check_spaces_at_end_of_line(prefix, call.out)
        check_round_trip(prefix, call.out, test_list)


if __name__ == "__main__":
    main()
