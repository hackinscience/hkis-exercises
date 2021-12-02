import ast
import sys
import gettext
from pathlib import Path

import correction_helper as ch

ch.exclude_file_from_traceback(__file__)
_ = gettext.translation("check", Path(__file__).parent, fallback=True).gettext


the_paragraph = '''whetting_your_appetite = "Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms."'''  # noqa


class FlattenVisitor(ast.NodeVisitor):
    def __init__(self, **kwargs):
        self.nodes = []
        super().__init__(**kwargs)

    def generic_visit(self, node):
        self.nodes.append(node)
        super().generic_visit(node)


def check():
    output = ch.run("solution.py")
    if output == "485":
        print(ch.congrats())
        sys.exit(0)  # It's the solution for the old one, let's say it's OK.
    solution = Path("solution.py").read_text(encoding="UTF-8")
    tree = ast.parse(solution)
    flat = FlattenVisitor()
    expected = 359
    flat.visit(tree)
    for node in flat.nodes:
        if not isinstance(node, ast.Constant):
            continue
        if node.value == expected or node.value == str(expected):
            ch.fail(
                f"""Nice catch! But try to do it with the
[len](https://docs.python.org/3/library/functions.html#len)
function instead. (Yes, I see the `{expected}` in your file)"""
            )
    if solution.count("Python is an easy to learn") > 1:
        ch.fail(
            """
Looks like you copy-pasted the paragraph multiple times.
Please don't, it's not needed, just keep the:

```python
whetting_your_appetite = "Python…
```

variable, a single time, and refer to the variable by its name,
`whetting_your_appetite`, in your code.

Also read [the tutorial](https://docs.python.org/3/tutorial/introduction.html) if you
need a reminder about how to use variables."""
        )
    if not output:
        ch.fail(
            "You printed nothing, did you forgot to call the "
            "[print](https://docs.python.org/3/library/functions.html#print) function?"
        )
    try:
        output = int(output)
    except ValueError:
        ch.fail(
            """I expect your program to print the **number** of characters.

You can count the nmber of characters in a string by using the
[len](https://docs.python.org/fr/3/library/functions.html#len) function.

Instead of the number of characters, your code printed:""",
            ch.code(output),
        )
    if output == len("whetting_your_appetite"):
        if "len('whetting_your_appetite')" in solution.replace(
            " ", ""
        ) or 'len("whetting_your_appetite")' in solution.replace(" ", ""):
            ch.fail(
                """Measure the *variable* `whetting_your_appetite`,
not the *str* `"whetting_your_appetite"`."""
            )
    if the_paragraph not in solution:
        ch.fail(
            """Looks like you modified the paragraph,
so now you don't get the right result.

Maybe just copy-paste it again, it should be:""",
            ch.code(the_paragraph),
        )
    if output > expected:
        ch.fail("It's less (you gave `{}`)".format(output))
    if output < expected:
        ch.fail("It's more (you gave `{}`)".format(output))
    print(
        ch.congrats(),
        "It's faster than counting them manually!",
        "Your code printed:",
        ch.code(output),
        sep="\n\n",
    )


if __name__ == "__main__":
    check()
