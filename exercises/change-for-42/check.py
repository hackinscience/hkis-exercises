from time import perf_counter
import correction_helper as checker

checker.exclude_file_from_traceback(__file__)

with checker.student_code():
    from solution import changes

EURO = (1, 2, 5, 10, 20, 50, 100, 200, 500)


def check():
    deadline = perf_counter() + 10
    previous = -1
    i = 0
    for amount, expected in ((1, 1), (42, 271), (99, 4366), (200, 73682)):
        args = amount, EURO
        with checker.student_code(
            too_slow_message="You function, when called as"
            f" `changes{args!r}` is too slow."
        ):
            theirs = changes(*args)
            i += 1
        if theirs != expected:
            checker.fail(f"Wrong number of combinations for `amount={amount}`")
    for amount in range(3, 666):
        nways = changes(amount, EURO)
        i += 1
        if perf_counter() > deadline:
            checker.fail(
                "I'm expecting your code to be a bit faster: "
                f"you solved {i} changes in ~10s, "
                "while I want to test 1000 of them in less than 10s."
            )
        if nways <= previous:
            checker.fail(
                "The number of ways to change is expected be increasing "
                "with an increasing amount.",
                f"I called your changes function twice with `coins={EURO}`"
                f"once with `amount={amount-1}` and once with `amount={amount}",
                "Respectively I got {previous} and {nways}.",
            )
            previous = nways


if __name__ == "__main__":
    check()
