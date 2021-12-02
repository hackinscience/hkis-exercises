from random import choice
from time import perf_counter

import correction_helper as checker
from sympy.ntheory import factorint

checker.exclude_file_from_traceback(__file__)


with checker.student_code():
    from solution import is_prime as student_is_prime


FEW_BIG_PRIMES = [  # Carefully choosen to be slow (>1s) with a dumb
    # algorithm and fast (~0.001s) on a fast implem.
    20021399,
    20021411,
    20021413,
    20021429,
    20021467,
    20021501,
    20021527,
    20021537,
    20021539,
    20021549,
    20021623,
    20021641,
    20021663,
    20021669,
    20021689,
    20021693,
    20021711,
    20021723,
    20021731,
    20021737,
    20021741,
    20021759,
    20021821,
    20021831,
    20021843,
    20021849,
    20021851,
    20021873,
    20021879,
]


def factors(n):
    f = factorint(n, multiple=True)
    if n in f:  # I don't care to learn it can be divided by itself.
        f.remove(n)
    return f


def check_a_number(n, student_guess):
    if not isinstance(student_guess, bool):
        checker.fail(
            "Your `is_prime` function is expected to return a `bool` "
            "(`True` or `False`)",
            f"I called it with `{n}` and it returned the "
            f"`{type(student_guess).__name__}` `{student_guess!r}`",
        )
    if student_guess is True:
        if n == 1:
            checker.fail(
                """[`1` is not prime](
https://en.wikipedia.org/wiki/Prime_number#Primality_of_one)
(your function, called as `is_prime(1)` returned `True`)."""
            )
        for factor in factors(n):
            checker.fail(
                f"`{n}` is divisible by {factor}, so it's not a prime!",
                f"Your `is_prime({n})` function returned `True`.",
            )
    if student_guess is False:
        if n == 1:
            return
        if not factors(n):
            checker.fail(
                f"`{n}` cannot be devided by any integer (other than itself and 1), "
                "so it's prime!"
                f"But your `is_prime({n})` function returned `False`.",
            )


def is_prime_upper_bound_failure(a):
    return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5))))


def is_prime_round_failure(a):
    return not (a < 2 or any(a % x == 0 for x in range(2, round(a ** 0.5))))


def check():
    checker.run("solution.py")
    with checker.student_code():
        their_first_100 = [i for i in range(1, 100) if student_is_prime(i)]
    if their_first_100 == [i for i in range(1, 100) if is_prime_upper_bound_failure(i)]:
        checker.fail(
            """Beware, upper bound of range is excluded leading your function
to tell that 4, 6, 8, ... are primes"""
        )

    if their_first_100 == [i for i in range(100) if is_prime_round_failure(i)]:
        checker.fail(
            """Beware, you may have used 'round', which leads your function
to sometime miss a divisor, for example you're telling that 9 and 15 are primes."""
        )

    for i in range(1, 256):
        with checker.student_code():
            result = student_is_prime(i)
        check_a_number(i, result)

    start = perf_counter()
    random_big_prime = choice(FEW_BIG_PRIMES)
    with checker.student_code(timeout=10):
        result = student_is_prime(random_big_prime)
    stop = perf_counter()
    if stop - start > 0.1:
        checker.fail(
            f"""Your function is too slow:
It took {stop - start:.2f}s to compute `is_prime({random_big_prime})`,
which should take around 0.0001s.

Hint: Don't search for divisors bigger than the square root of n.
"""
        )


if __name__ == "__main__":
    check()
