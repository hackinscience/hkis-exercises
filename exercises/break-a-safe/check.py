from correction_helper import code, fail, run, exclude_file_from_traceback

exclude_file_from_traceback(__file__)

digits = [1, 5, 8]

expected = set()
for a in digits:
    for b in digits:
        for c in digits:
            for d in digits:
                if all(x in (a, b, c, d) for x in digits):
                    expected.add(f"{a} {b} {c} {d}")


def check():
    output = run("solution.py")
    if not output:
        fail("You printed nothing ☹")
    for line in output.split("\n"):
        if " " not in line:
            fail(
                f"""I need digits separated by spaces, one combination per line,
you printed:

{code(output)}
"""
            )
        try:
            a, b, c, d = line.split(" ")
            a, b, c, d = int(a), int(b), int(c), int(d)
        except Exception:
            fail(
                f"""Line `{line}` looks malformed, I expect 4 digits per line,
separated by a single space."""
            )
    lineset = set(output.split("\n"))
    for unexpected in lineset - expected:
        a, b, c, d = unexpected.split(" ")
        a, b, c, d = int(a), int(b), int(c), int(d)
        for digit in a, b, c, d:
            if digit not in digits:
                fail(
                    f"""Why trying `{unexpected}`? The digit {digit} is not dirty,
better not even try a combination with it."""
                )
        for digit in 1, 5, 8:
            if digit not in (a, b, c, d):
                fail(
                    f"""You should not even try `{unexpected}`:

As the digit `{digit}` is dirty, it is necessarity in the combination.

So don't try any combination without it, it's a waste of time."""
                )
        fail(f"Why trying `{unexpected}` (are you missing a digit?)?")
    for missing in expected - lineset:
        fail(f"Why not trying `{missing}`?")


if __name__ == "__main__":
    check()
