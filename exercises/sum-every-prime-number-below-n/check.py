from correction_helper import code, exclude_file_from_traceback, fail, student_code

exclude_file_from_traceback(__file__)

CHECKS = {79: 712, 0: 0, 5: 5, 10: 17, 50: 328, 10: 17, 500: 21536, 1000: 76127}

with student_code():
    from solution import sum_primes


def check():
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
    check()
