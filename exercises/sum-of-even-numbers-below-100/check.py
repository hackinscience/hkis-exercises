from pathlib import Path

from correction_helper import code, exclude_file_from_traceback, fail, run

exclude_file_from_traceback(__file__)


def check():
    output = run("solution.py")
    if not output:
        fail(
            """Your code printed nothing, did you forgot to call the
[print](https://docs.python.org/3/library/functions.html#print) function?"""
        )
    solution = Path("solution.py").read_text()
    try:
        output = int(output)
    except ValueError:
        try:
            integers = [int(x) for x in output.split("\n")]
            fail(
                f"""I expect your output to be an integer,
got {len(integers)} numbers instead:""",
                code(output),
            )
        except ValueError:
            fail("I expect your output to be an integer (the sum), got:", code(output))
    if output == 100 and "=+" in solution:
        fail(
            """Did you mistyped `+=` as `=+`?

```python
value =+ 10  # is equivalent to:
value = (+ 10)  # which is equivalent to:
value = 10
```

in the other hand:

```python
value += 10  # is a shortcut to:
value = value + 10
```
"""
        )

    if output == sum(i for i in range(103) if i % 2 == 0):
        fail("Looks like you counted 102, which is greater than 100.")
    if output == sum(i for i in range(100) if i % 2 == 0):
        fail(
            """I'm asking `<= 100`, not `< 100`.
Beware, in Python, ranges are semi-open: start is included, stop is not."""
        )
    if output == sum(i for i in range(100) if i % 2):
        fail("This is the sum of odd number < 100 :(")
    if output == sum(i for i in range(101) if i % 2):
        fail("This is the sum of odd number :(")
    if output == sum(range(100)):
        fail(
            """This is the sum of natural numbers < 100,
I need only even numbers (divisible by two)."""
        )
    if output == sum(range(101)):
        fail(
            """This is the sum of natural numbers <= 100,
I need only even numbers (divisible by two)."""
        )
    if output == sum(i for i in range(101) if i % 2 == 0):
        return  # Success!

    if output < 100:
        fail(
            "You gave:",
            code(output),
            """which looks low. There's 98 and 96 that are both even numbers below 100
and whose sum is greater than 100.""",
        )

    fail(f"I don't get the same sum as you, FYI you gave:\n\n{code(output)}")


if __name__ == "__main__":
    check()
