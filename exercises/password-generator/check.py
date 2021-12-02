import math
from statistics import mean
from string import ascii_lowercase, ascii_uppercase, digits

import correction_helper as checker

checker.exclude_file_from_traceback(__file__)

with checker.student_code():
    from solution import pwgen


def check_password(ntry, password, length, with_digits, with_uppercase):
    if not isinstance(password, str):
        checker.fail(
            "Your function should return strings, it returned a {type}:".format(
                type=type(password)
            ),
            checker.code(password),
        )
    if len(password) != length:
        checker.fail(
            "Asked for a password of length {}, got {}".format(length, password)
        )
    if not with_digits and any(c in password for c in digits):
        checker.fail(
            (
                "Found a digit in a 'without digits' password ({})"
                " (after generating {} passwords)."
            ).format(password, ntry)
        )
    if not with_uppercase and any(c in ascii_uppercase for c in password):
        checker.fail(
            "Found an uppercased letter in a 'without uppercase' "
            "password ({}) (after generating {} passwords).".format(password, ntry)
        )
    if not any(c in ascii_lowercase for c in password):
        checker.fail(
            "Found no lowercase letter in a password"
            " ({}) (after generating {} passwords).".format(password, ntry)
        )
    if with_digits and not any(c in digits for c in password):
        checker.fail(
            "I asked for a password with digits (`with_digits=True`) "
            "and your function gave me one without digits: "
            "`{}`. (After generating {} passwords).".format(password, ntry)
        )
    if with_uppercase and not any(c in ascii_uppercase for c in password):
        checker.fail(
            "Found no uppercased letters in a 'with uppercase' password "
            "({}) after generating {} passwords)".format(password, ntry)
        )


def entropy(password, alphabet):
    return math.ceil(math.log2(len(set(alphabet))) * len(password))


def check():
    from collections import defaultdict

    default_length = 10
    args_set = [
        (default_length, False, False),
        (default_length, True, False),
        (default_length, False, True),
        (default_length, True, True),
    ]
    all_passwords = defaultdict(list)
    entropies = {}
    for args in args_set:
        for ntry in range(500):
            with checker.student_code(
                too_slow_message=f"Called `pwgen{args!r}`, and had to "
                "cancel your function: it looks like it entered in an infinite loop."
            ):
                password = pwgen(*args)
            if password is None:
                checker.fail(
                    f"Your function, called as `pwgen{args!r}` returned `None`.",
                    "Maybe you forgot the `return` statement?",
                )
            check_password(ntry, password, *args)
            all_passwords[args].append(password)
        alphabet = set("".join(all_passwords[args]))
        entropies[args] = mean([entropy(p, alphabet) for p in all_passwords[args]])
    if not 47 <= entropies[10, False, False] <= 48:
        checker.fail(
            (
                "I expect the entropy of a lower cased alphabet to be of "
                "like 4.7 bits per char, got {} bits of entropy "
                "for a password of {} characters"
            ).format(entropies[default_length, False, False], default_length)
        )
    if not 57 <= entropies[default_length, False, True] <= 58:
        checker.fail(
            (
                "I expect the entropy of a case sensitive alphabet to be of "
                "like 5.7 bits per char, got {} bits of entropy "
                "for a password of {} characters"
            ).format(entropies[default_length, False, True], default_length)
        )
    if not 51 <= entropies[default_length, True, False] <= 52:
        checker.fail(
            (
                "I expect the entropy of a case insensitive alphanumeric "
                "alphabet to be of like 5.17 bits per char, got {} bits of "
                "entropy for a password of {} characters"
            ).format(entropies[default_length, True, False], default_length)
        )
    if not 59 <= entropies[default_length, True, True] <= 60:
        checker.fail(
            (
                "I expect the entropy of a case sentivve alphanumeric alphabet "
                " to be of like 5.954 bits per char, got {} bits of entropy "
                "for a password of {} characters"
            ).format(entropies[default_length, True, True], default_length)
        )


if __name__ == "__main__":
    check()
