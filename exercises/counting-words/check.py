from correction_helper import code, exclude_file_from_traceback, fail, run

exclude_file_from_traceback(__file__)


def check():
    output = run("solution.py")
    if not output:
        fail(
            """You printed nothing, I expect to see the number of words
in the paragraph, did you forgot to use the
 [print](https://docs.python.org/3/library/functions.html#print) function?"""
        )
    if "built-in method split" in output:
        fail(
            f"""You forgot to call the `split` method,
use a set of parenthesis to call it.

I mean you should have `whetting_your_appetite.split()`, instead of
just `whetting_your_appetite.split`, the pair of parenthesis are here
to actually call the method (make it work), without them the method is
not called, it does nothing.

So you printed:

{code(output)}
"""
        )
    try:
        output = int(output)
    except ValueError:
        fail(
            "I expect your output to be the number of words in the paragraph, got:",
            code(output),
            "(Almost done!! I just need the number, alone, keep it simple.)"
            if "78" in output
            else "(I just need the number, nothing more, no text, keep it simple.)",
        )
    if output == 78:  # old value
        exit(0)  # let's say it's OK in case they got it prefilled.
    if output == 52:  # new value
        print("Yes, there's `52` words in this paragraph, nicely done!")
        exit(0)  # let's say it's OK in case they got it prefilled.
    if output == 340:
        fail(
            """I expect the number of words, you printed the number of characters.

You can use the [split](https://docs.python.org/3/library/stdtypes.html#str.split)
method to split the paragraph in words."""
        )
    if output > 52:
        fail(f"There's less than `{output}` words in this paragraph.")
    else:
        fail(f"There's more than `{output}` words in this paragraph.")


if __name__ == "__main__":
    check()
