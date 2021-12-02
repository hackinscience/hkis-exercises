from math import isclose

from correction_helper import code, exclude_file_from_traceback, fail, student_code

exclude_file_from_traceback(__file__)


def check_fahrenheit_to_celsius():
    with student_code(prefix="While importing your solution:"):
        from solution import fahrenheit_to_celsius
    for celsius, fahrenheit in [
        (-273.15, -459.67),
        (-17.7777777777, 0.00),
        (0.00, 32),
        (1668, 3034.4),
    ]:
        with student_code(
            prefix=f"While calling `fahrenheit_to_celsius({fahrenheit!r})`",
        ):
            their_c = fahrenheit_to_celsius(fahrenheit)
        if their_c is None:
            fail(
                "Your `fahrenheit_to_celsius` function returned `None`, "
                "did you forget to add a `return` statement?"
            )
        try:
            if not isclose(celsius, their_c, rel_tol=1e-05, abs_tol=1e-05):
                if f"{their_c:.2f}°C" != f"{celsius:.2f}°C":
                    fail(
                        f"Your fahrenheit_to_celsius function tells that "
                        f"{fahrenheit:.2f}°F is {their_c:.2f}°C, "
                        f"but it is {celsius:.2f}°C."
                    )
                else:
                    fail(
                        f"Your fahrenheit_to_celsius function tells that "
                        f"{fahrenheit:.2f}°F is {their_c!r}°C, "
                        f"but it is {celsius!r}°C."
                    )

        except TypeError as err:
            if "real number" in str(err):
                fail(
                    f"Your function is expected to return a real number, "
                    f"it returned a `{type(their_c)}`:",
                    code(their_c),
                )
            raise


def check_celsius_to_fahrenheit():
    with student_code(prefix="While importing your solution:"):
        from solution import celsius_to_fahrenheit

    for celsius, fahrenheit in [
        (-273.15, -459.67),
        (-17.7777777777, 0.00),
        (0.00, 32),
        (1668, 3034.4),
    ]:

        with student_code(
            prefix=f"While calling `celsius_to_fahrenheit({celsius!r})`",
        ):
            their_f = celsius_to_fahrenheit(celsius)
        if their_f is None:
            fail(
                """Your `celsius_to_fahrenheit` function returned `None`,
did you forget to add a `return` statement?"""
            )
        if isinstance(their_f, complex):
            fail(
                f"""Your function is expected to return a real number,
it returned a `{type(their_f)}`:""",
                code(their_f),
            )
        try:
            if not isclose(fahrenheit, their_f, rel_tol=1e-05, abs_tol=1e-05):
                fail(
                    f"""Your celsius_to_fahrenheit function tells that
{celsius:.2f}°C is {their_f:.2f}°F, but it is {fahrenheit:.2f}°F."""
                )
        except TypeError as err:
            if "real number" in str(err):
                fail(
                    f"""Your function is expected to return a real number,
it returned a `{type(their_f)}`:""",
                    code(their_f),
                )
            raise


def main():
    check_fahrenheit_to_celsius()
    check_celsius_to_fahrenheit()
    print("Your temperature conversions looks good to me!")


if __name__ == "__main__":
    main()
