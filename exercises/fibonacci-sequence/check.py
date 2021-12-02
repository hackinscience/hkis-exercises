import correction_helper as checker

checker.exclude_file_from_traceback(__file__)


FIB = [
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
    6765,
    10946,
    17711,
    28657,
    46368,
    75025,
    121393,
    196418,
    317811,
    514229,
    832040,
    1346269,
    2178309,
    3524578,
    5702887,
    9227465,
    14930352,
    24157817,
    39088169,
    63245986,
    102334155,
    165580141,
    267914296,
    433494437,
    701408733,
    1134903170,
    1836311903,
    2971215073,
    4807526976,
    7778742049,
    12586269025,
    20365011074,
]


def check():
    checker.run("solution.py")
    with checker.student_code(
        print_prefix="While importing your solution, it printed:"
    ):
        from solution import fibonacci
    for i in range(50):
        with checker.student_code(
            prefix=[
                "While calling your function as:",
                checker.code(f"fibonacci({i})", "python"),
            ],
        ):
            f = fibonacci(i)
        try:
            f = list(f)
        except Exception:
            checker.fail(
                "Expected your `fibonacci` function to return an interable.",
                f"Called `fibonacci({i})`, got:",
                checker.code(f),
            )
        if f != FIB[:i]:
            checker.fail(
                f"We do not agree for `fibonacci({i!r})`, I expected:",
                checker.code(FIB[:i]),
                "But your `fibonacci` function returned:",
                checker.code(f),
            )
    print(checker.congrats())


if __name__ == "__main__":
    check()
