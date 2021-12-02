from correction_helper import code, exclude_file_from_traceback, fail, student_code

exclude_file_from_traceback(__file__)

with student_code(
    print_prefix="""When I imported your code, it printed something,
which is unexpected.
Just define the `battery_charge` function, but don't call it.

Or hide the call inside a `if __name__ == "__main__"`, so you can
still try it by executing it, but it won't be called when imported.""",
):
    from solution import battery_charge


def check_battery_charge(i):
    with student_code(print_allowed=None) as test:
        returned_value = battery_charge(i)
    if not test.out and returned_value:
        fail("You need to print your answer, not return it.")
    messages = [f"I tried `battery_charge({i})`, and it printed:", code(test.out)]
    if not test.out:
        fail(
            f"I called your function as `battery_charge({i})`, "
            "and it printed nothing ☹"
        )
    if "\n" not in test.out:
        fail("Your function needs to print two lines, found a single one, ", *messages)
    line1, line2 = test.out.split("\n", maxsplit=1)
    if line1[0] != "[":
        fail(
            "The first char of the first line should be a `[`, like a battery end.",
            *messages,
        )
    if line1[-1] != "]":
        fail(
            "The last char of the first line should be a `]`, like a battery end.",
            *messages,
        )
    line1 = line1[1:-1]
    if len(line1) != 10:
        fail(
            "The inner part of the battery should be composed of 10 characters, "
            "no matter its charge, fill with spaces as needed.",
            *messages,
        )
    if len(line1.strip()) != round(i / 10):
        fail(
            "The non-blank part of the battery should represent the actual rounded "
            f"charge. I mean for 39% I want 4 bars, as for 41%. "
            f"Here I tried with {i}% so I expected {round(i/10)} bars "
            f"and got `{line1.strip()}`",
            *messages,
        )
    if str(i) not in line2:
        fail("The 2nd line should contain the charge value.", *messages)


def check():
    for i in [11, 25, 32, 38, 42, 100]:
        check_battery_charge(i)


if __name__ == "__main__":
    check()
