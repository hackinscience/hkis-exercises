"""
HackInScience - Sequence Mining (check)
Author: Antoine Mazières
"""
import time
from collections import Counter

from correction_helper import code, exclude_file_from_traceback, fail, student_code

exclude_file_from_traceback(__file__)


CHECKS = [
    [
        0.1,
        ["ABC", "ABAB", "BCAA"],
        10000,
        Counter(
            {
                "A": 3,
                "B": 3,
                "C": 2,
                "AB": 2,
                "BC": 2,
                "ABC": 1,
                "ABA": 1,
                "AA": 1,
                "ABAB": 1,
                "CA": 1,
                "BA": 1,
                "BCAA": 1,
                "BCA": 1,
                "CAA": 1,
                "BAB": 1,
            }
        ),
    ],
    [
        0.51,
        ["ABC", "ABAB", "BCAA"],
        4,
        Counter({"B": 3, "A": 3, "C": 2, "AB": 2, "BC": 2}),
    ],
    [
        0.5,
        ["ABCDEFGHIJKL", "ZOPQABCDLMNOP", "REWQZOPQAB", "WUEIRTKFNG", "SDFJGKSDJFG"],
        10,
        Counter({"D": 3, "K": 3, "F": 3, "AB": 3, "A": 3, "G": 3, "B": 3, "E": 3}),
    ],
    [0.34, ["ABC", "ABAB", "BCAA"], 1, Counter({"A": 3, "B": 3, "C": 2})],
]


speed_test = [
    (
        0.34,
        ["ABCD", "ABABC", "BCAABCD"],
        maxlen,
        Counter(
            {
                "AB": 3,
                "ABC": 3,
                "C": 3,
                "B": 3,
                "A": 3,
                "BC": 3,
                "BCD": 2,
                "CD": 2,
                "ABCD": 2,
                "D": 2,
            }
        ),
    )
    for maxlen in [pow(10, i) for i in range(2, 100)]
]

with student_code():
    from solution import seq_mining


def check(thres, data, maxlen, expected):
    before = time.perf_counter()
    with student_code(timeout=10):
        theirs = seq_mining(data, thres, maxlen)
    duration = time.perf_counter() - before
    if duration > 1:
        fail(
            f"""`seq_mining({data!r}, {thres!r}, {maxlen!r})`
is too slow (took {duration}s)."""
        )
    if theirs is None:
        fail(
            f"""Did you forget to return? Got `None` while calling
`seq_mining({data!r}, {thres!r}, {maxlen!r})`."""
        )

    if theirs != expected:
        fail(
            f"With `seq_mining({data!r}, {thres!r}, {maxlen!r})` "
            "we dot not agree, I'm getting:",
            code(expected),
            "You're returning:",
            code(theirs),
        )


def checks():
    for thres, data, maxlen, expected in CHECKS:
        check(thres, data, maxlen, expected)
    for thres, data, maxlen, expected in speed_test:
        check(thres, data, maxlen, expected)


if __name__ == "__main__":
    checks()
