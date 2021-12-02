from random import randint
import inspect

import correction_helper as checker


checker.exclude_file_from_traceback(__file__)

with checker.student_code():
    from solution import flatten


def check(test, expected):
    tested = repr(test)
    with checker.student_code(
        prefix=[
            "While calling your function like:",
            checker.code(f"flatten({test})", "python"),
        ]
    ):
        theirs = flatten(test)
    if type(theirs) != list:
        checker.fail(
            f"""I'm expecting your function to return a `list`,
it returns a `{type(theirs)}`."""
        )
    if repr(test) != tested:
        checker.fail(
            "Your function is modifying the given parameter, why?",
            "I tried:",
            checker.code(
                f"""test = {tested}
result = flatten(test)
print(test)""",
                "python",
            ),
            f"I expected test to be unmodified, being `{tested}` "
            f"but my test variable now equals to `{test!r}`.",
        )
    if theirs is None:
        checker.fail("Your function is returning `None`, you should return a `list`.")
    if theirs != expected:
        checker.fail(
            f"I called `flatten({test!r})` and expected:",
            checker.code(expected),
            "But your `flatten` function returned:",
            checker.code(theirs),
            """Beware of globals or mutable function parameters, they can hold
a state between two calls and yield unexpected behaviors.

(Yes, I'm calling your function many times with many different tests.)

To ensure you're not having this kind of issue you can run, for example:""",
            checker.code("flatten([1, 2, 3, 4])\nflatten([1, 2])", "python"),
        )


def main():
    try:
        signature = inspect.signature(flatten)
    except ValueError:
        checker.fail("I need you to define a `flatten` function, what have you done?")
    try:
        signature.bind([])
    except TypeError:
        checker.fail(
            (
                "Your function should be callable as `flatten(a_list)`: "
                "accepting a single parameter, but your function wants: "
                "`{}`"
            ).format(str(signature))
        )

    with checker.student_code():
        first_ptr = flatten([1])

    if type(first_ptr) != list:
        checker.fail(
            f"""I'm expecting your function to return a `list`,
it returns a `{type(first_ptr)}`."""
        )
    first_result = list(first_ptr)  # Copy it in case they reuse their global...

    second_ptr = flatten([1])
    if type(second_ptr) != list:
        checker.fail(
            f"""I'm expecting your function to return a `list`,
it returns a `{type(second_ptr)}`."""
        )
    second_result = list(second_ptr)

    if first_result != second_result:
        checker.fail(
            "I called your function twice, the first time I called:",
            checker.code("flatten([1])"),
            "and got:",
            checker.code(repr(first_result)),
            "The 2nd time I called:",
            checker.code("flatten([1])"),
            "and got:",
            checker.code(repr(second_result)),
            """Avoid globals or mutable function parameters, they can hold
a state between two calls and yield this kind of behavior.""",
        )

    for test, expected in (
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 2, [3, 4]], [1, 2, 3, 4]),
        ([[1, 2], 3], [1, 2, 3]),
        ([[[[1], 2], 3], 4], [1, 2, 3, 4]),
        ([10, 1], [10, 1]),
        ([9999, [9998]], [9999, 9998]),
    ):
        check(test, expected)
    a, b, c, d = (
        randint(10_000, 100_000_000),
        randint(10_000, 100_000_000),
        randint(10_000, 100_000_000),
        randint(10_000, 100_000_000),
    )
    check([a, b, c, d], [a, b, c, d])
    check([a, [b, c, d]], [a, b, c, d])
    check([[a, b, c], d], [a, b, c, d])
    check([a, [b, c], d], [a, b, c, d])
    check([[a], [b], [c], [d]], [a, b, c, d])
    check([a, [[[[[[b]]]]], c, d]], [a, b, c, d])
    check([[[[[[[[[[[[[[a, b, c]]]]]]]]]]]]], d], [a, b, c, d])
    check([[a, [b, c], d]], [a, b, c, d])


if __name__ == "__main__":
    main()
