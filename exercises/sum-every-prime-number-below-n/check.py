from correction_helper import code, exclude_file_from_traceback, fail, student_code

exclude_file_from_traceback(__file__)

CHECKS = {79: 712, 0: 0, 5: 5, 10: 17, 50: 328, 10: 17, 500: 21536, 1000: 76127}

with student_code():
    from solution import sum_primes


def test_is_increasing():
    prev = None
    for i in range(1, 100, 2):
        with student_code(
            prefix=[
                "While testing your `sum_primes` function as:",
                code(f"sum_primes({i})", "python"),
            ]
        ):
            current = sum_primes(i)
        if prev is not None:
            if current < prev:
                fail(
                    f"`sum_prime({i})` can only be greater or equal to "
                    f"`sum_prime({i-1})`.",
                    "Your implemtation gave:",
                    "- `sum_primes({i-1}) → {prev!r}\n"
                    "- `sum_primes({i}) → {current!r}\n",
                )
        prev = current


def test_some_small_obvious_ones():
    # Based on first primes : 2, 3, 5, 7, 11
    with student_code(
        prefix=[
            "While testing your `sum_primes` function as:",
            code("sum_primes(2)", "python"),
        ]
    ):
        result = sum_primes(2)
    if result != 0:
        fail(
            "`sum_primes(2)` is expected to give `0` "
            "because there's no prime number less than two.",
            f"Your function returned: `{result!r}`.",
        )
    with student_code(
        prefix=[
            "While testing your `sum_primes` function as:",
            code("sum_primes(4)", "python"),
        ]
    ):
        result = sum_primes(4)
    if result != 5:
        fail(
            "`sum_primes(4)` is expected to give `5` "
            "because there's the prime numbers `2` and `3` "
            "being less than `4`, and `2+3` gives `5`.",
            f"Your function returned: `{result!r}`.",
        )
    with student_code(
        prefix=[
            "While testing your `sum_primes` function as:",
            code("sum_primes(12)", "python"),
        ]
    ):
        result = sum_primes(12)
    if result != 2 + 3 + 5 + 7 + 11:
        fail(
            f"`sum_primes(12)` is expected to give `{2+3+5+7+11}` "
            "because there's the prime numbers `2`, `3`, `5`, `7`, and `11` "
            f"being less than `12`, and `2+3+5+7+11` gives `{2+3+5+7+11}`.",
            f"Your function returned: `{result!r}`.",
        )


def test_known_values():
    for i, expected in CHECKS.items():
        with student_code(
            prefix=[
                "While testing your `sum_primes` function as:",
                code(f"sum_primes({i})", "python"),
            ]
        ):
            their = sum_primes(i)
        if their != expected:
            fail(
                f"For `sum_primes({i})` we do not agree, "
                f"I found `{expected}`, but your function returned:",
                code(their),
            )


if __name__ == "__main__":
    test_some_small_obvious_ones()
    test_is_increasing()
    test_known_values()
