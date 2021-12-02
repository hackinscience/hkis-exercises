import correction_helper as checker

checker.exclude_file_from_traceback(__file__)

EXPECTED = """0
21
42
63
84
105
126
147
168
189
210
231
252
273
294
315
336
357
378
399
420
441
462
483
504
525
546
567
588
609
630
651
672
693
714
735
756
777
798
819
840
861
882
903
924
945
966
987"""


def check():
    stdout = checker.run("solution.py")
    messages = ["Here's your full output:", checker.code(stdout)]
    if "None" in stdout:
        checker.fail("You're printing `None`, why?", *messages)

    if "[" in stdout and "]" in stdout:
        checker.fail(
            "Looks like you're printing the representation of a `list`, "
            "I just ask for the numbers, on by line.",
            *messages,
        )
    given = set(stdout.split())
    expected = set(EXPECTED.split())
    missing = expected - given
    too_much = given - expected
    if missing and len(too_much) < len(missing):
        i = missing.pop()
        checker.fail(
            f"You're missing {len(missing)} elements, like {i} for example.",
            *messages,
        )
    if too_much:
        checker.fail(
            f"You're giving {len(too_much)} number{'s' if len(too_much) > 1 else ''}, "
            "that's too much.",
            f"For example, why is your code printing `{too_much.pop()}`?",
            *messages,
        )
    if given != expected:
        checker.fail(
            f"Not what I'm expecting (you're giving {len(given)} values, "
            "I'm having {len(expected)} values).",
            *messages,
        )


if __name__ == "__main__":
    check()
