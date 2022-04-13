from correction_helper import (
    exclude_file_from_traceback,
    fail,
    student_code,
    code,
    congrats,
)

exclude_file_from_traceback(__file__)

KNOWN_vALUES = {
    1: 0,
    2: 1,
    3: 7,
    4: 2,
    5: 5,
    6: 8,
    7: 16,
    8: 3,
    9: 19,
    27: 111,
}


class TooShort(ValueError):
    ...


class TooFar(ValueError):
    ...


def flight(i, n):
    """Flight the collatz sequence, from i, during n-steps."""
    for step in range(n):
        if i == 1:
            raise TooFar("Unexpected enconter with 1.", step)
        i = i * 3 + 1 if i % 2 else i // 2
    if i != 1:
        raise TooShort("Did not reached 1", i)


with student_code():
    from solution import collatz_length


def check_float_usage():
    if collatz_length(1267189310707289) == 495:
        fail(
            """Beware, by dividing using a true division (`/` operator) Python gives
you a float.
Float [have limited precision](https://docs.python.org/3/tutorial/floatingpoint.html)

You should better use an integer division (`//` operator) as you know it's divisible,
to keep using integers (which have no limit in Python).
"""
        )
    if collatz_length(1267189310707289) != 314:
        fail(
            "For `collatz_length(1267189310707289)`, I do not agree, "
            "I think it's `314`, "
            f"you said it's `{collatz_length(1267189310707289)}`."
        )


def check_with_known_values():
    for i, expected in KNOWN_vALUES.items():
        with student_code(
            prefix=[
                "While running your function as:",
                code(f"collatz_length({i})", "python"),
            ]
        ):
            result = collatz_length(i)
        if result != expected:
            fail(
                f"For `collatz_length({i})`, I do not agree, "
                f"I think it's `{expected}`, "
                f"you said it's `{collatz_length(i)}`."
            )


def check_by_flying_it():
    for i in range(1, 200):
        with student_code(
            prefix=[
                "While running your function as:",
                code(f"collatz_length({i})", "python"),
            ]
        ):
            result = collatz_length(i)
        try:
            flight(i, result)
        except TooShort as err:
            fail(
                f"For `collatz_length({i})`, you said I would reach 1 after "
                f"{result} steps. "
                f"Sadly I reached {err.args[1]} instead."
            )
        except TooFar as err:
            fail(
                f"For `collatz_length({i})`, you said I would reach 1 after "
                f"{result} steps. "
                f"Sadly I reached `1` sooner, at step {err.args[1]}."
            )


if __name__ == "__main__":
    check_float_usage()
    check_with_known_values()
    check_by_flying_it()
    print(congrats())
