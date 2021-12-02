from textwrap import indent

from correction_helper import code, exclude_file_from_traceback, fail, student_code

exclude_file_from_traceback(__file__)


def main():
    failed_to_import = False
    with student_code(print_prefix="Your code printed:"):
        try:
            from solution import longest_word
        except ImportError:
            failed_to_import = True

    if failed_to_import:
        fail(
            """Cannot find your `longest_word` function.
Please name it correctly, here's the syntax:
```python
def longest_word(text):
    ...
```
and see the [function tutorial](
https://docs.python.org/3/tutorial/controlflow.html#defining-functions).

"""
        )
    tests = {
        "Monty Python and the Holy Grail": "Python",
        "I love shrubberies": "shrubberies",
        "None shall pass": "shall",
        "Please": "Please",
        "Ask me the questions, bridgekeeper I am not afraid.": "bridgekeeper",
        """It is I Arthur Son of Uther Pendragon from the castle of Camelot
King of the Britons defeater of the Saxons""": "Pendragon",
        "You’ve got two empty halves of coconuts and you’re bangin’ em": "coconuts",
    }
    for test, expected in tests.items():
        with student_code(
            print_prefix=[
                "Your function, called as:",
                code("longest_word({})".format(repr(test))),
                "printed:",
            ]
        ):
            theirs = longest_word(test)
        if theirs is None:
            fail(
                "Your function returned `None`, it should [return]"
                "(https://docs.python.org/3/tutorial/controlflow.html"
                "#defining-functions) a string."
            )
        if theirs != expected:
            message = f"""In the text:

{indent(test, '> ')}

you found `{theirs!r}` as the longest word, while I find `{expected!r}`.
"""
            try:
                if "\n" in theirs:
                    message += """
!!! note
    The `\\n` thing means 'new line' (in many languages, it's not a Python thing).
    To also split on new lines, don't give an argument to the
    [split](https://docs.python.org/3/library/stdtypes.html?highlight=splitlines#str.split)
    function, this way it will split on any blanks.
    """
            except Exception:  # theirs could not be iterable.
                pass
            fail(message)


if __name__ == "__main__":
    main()
