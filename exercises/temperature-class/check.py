import math

import correction_helper as checker

checker.exclude_file_from_traceback(__file__)


def isclose(a, b):
    try:
        return math.isclose(a, b, rel_tol=1e-05, abs_tol=1e-05)
    except TypeError:
        return False


def main():
    with checker.student_code():
        from solution import Temperature
    for kelvin, celsius, fahrenheit in [
        (0, -273.15, -459.67),
        (255.3722222222222, -17.7777777777, 0.00),
        (273.15, 0.00, 32),
        (1941.15, 1668, 3034.4),
    ]:
        with checker.student_code():
            t0 = Temperature()
            t0.kelvin = kelvin
            their_celsius = t0.celsius
            their_fahrenheit = t0.fahrenheit
            their_kelvin = t0.kelvin
        tail = [
            "My test case looks like:",
            checker.code(
                f"""t0 = Temperature()
t0.kelvin = {kelvin}
print(t0.celsius)
print(t0.fahrenheit)
print(t0.kelvin)
""",
                "python",
            ),
        ]
        if not isclose(their_celsius, celsius):
            checker.fail(
                f"""Converting {kelvin}K to celsius:
found {their_celsius},expected {celsius}.""",
                *tail,
            )
        if not isclose(their_fahrenheit, fahrenheit):
            checker.fail(
                f"""Converting {kelvin}K to fahrenheit:
found {their_fahrenheit}, expected {fahrenheit}""",
                *tail,
            )
        if not isclose(their_kelvin, kelvin):
            checker.fail(
                f"""Converting {kelvin}K back to kelvin:
found {their_kelvin}, expected {kelvin}""",
                *tail,
            )

        with checker.student_code():
            t0.celsius = celsius
            their_celsius = t0.celsius
            their_fahrenheit = t0.fahrenheit
            their_kelvin = t0.kelvin
        if not isclose(their_celsius, celsius):
            checker.fail(
                f"""Converting {celsius}°C back to celsius:
found {their_celsius}, expected {celsius}"""
            )
        if not isclose(their_fahrenheit, fahrenheit):
            checker.fail(
                f"""Converting {celsius}°C to fahrenheit:
found {their_fahrenheit}, expected {fahrenheit}"""
            )
        if not isclose(their_kelvin, kelvin):
            checker.fail(
                f"""Converting {celsius}°C to kelvin:
found {their_kelvin}, expected {kelvin}"""
            )

        with checker.student_code():
            t0.fahrenheit = fahrenheit
            their_celsius = t0.celsius
            their_fahrenheit = t0.fahrenheit
            their_kelvin = t0.kelvin
        if not isclose(their_celsius, celsius):
            checker.fail(
                f"""Converting {fahrenheit}°F to celsius:
found {their_celsius}, expected {celsius}"""
            )
        if not isclose(their_fahrenheit, fahrenheit):
            checker.fail(
                f"""Converting {fahrenheit}°F back to fahrenheit:
found {their_fahrenheit}, expected {fahrenheit}"""
            )
        if not isclose(their_kelvin, kelvin):
            checker.fail(
                f"""Converting {fahrenheit}°F to kelvin:
found {their_kelvin}, expected {kelvin}"""
            )

        # Test if they don't get lost when I change from an attr to another.
        with checker.student_code():
            t0 = Temperature()
            t0.kelvin = 12
            t0.celsius = 12
            t0.fahrenheit = fahrenheit
            their_celsius = t0.celsius
            their_fahrenheit = t0.fahrenheit
            their_kelvin = t0.kelvin
        if not isclose(their_celsius, celsius):
            checker.fail(
                "I executed the following test:",
                checker.code(
                    f"""t0 = Temperature()
t0.kelvin = 12
t0.celsius = 12
t0.fahrenheit = {fahrenheit}
print(t0.celsius)
"""
                ),
                f"""Basically I'm converting {fahrenheit}°F to celsius,
(after messing around with other values):
found {their_celsius}, expected {celsius}""",
            )
        if not isclose(their_fahrenheit, fahrenheit):
            checker.fail(
                "I executed the following test:",
                checker.code(
                    f"""t0 = Temperature()
t0.kelvin = 12
t0.celsius = 12
t0.fahrenheit = {fahrenheit}
print(t0.fahrenheit)
"""
                ),
                f"""Basically I'm setting fahrenheit and try to get it back again,
(after messing around with other values):
found {their_fahrenheit}, expected {fahrenheit}""",
            )
        if not isclose(their_kelvin, kelvin):
            checker.fail(
                "I executed the following test:",
                checker.code(
                    f"""t0 = Temperature()
t0.kelvin = 12
t0.celsius = 12
t0.fahrenheit = {fahrenheit}
print(t0.kelvin)
"""
                ),
                f"""Basically I'm trying to convert {fahrenheit}°F to kelvin
(after messing around with other values):
found {their_kelvin}, expected {kelvin}""",
            )


if __name__ == "__main__":
    main()
