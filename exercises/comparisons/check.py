import ast
from pathlib import Path

from correction_helper import code, exclude_file_from_traceback, fail, run

exclude_file_from_traceback(__file__)


class FlattenVisitor(ast.NodeVisitor):
    def __init__(self, **kwargs):
        self.nodes = []
        super().__init__(**kwargs)

    def generic_visit(self, node):
        self.nodes.append(node)
        super().generic_visit(node)


def check():
    output = run("solution.py")
    solution = Path("solution.py").read_text(encoding="UTF-8")
    if solution.count("elif") > 5:
        fail(
            """This look overly complicated, why so many `elif`s? Simply use a
[for](https://docs.python.org/3/tutorial/controlflow.html#for-statements) to
iterate over the values."""
        )
    if "1871655963" not in solution:
        fail(
            "Do you edited my list? Please don't, "
            "it's hard to me to check your code if you do so.",
            "Please copy-paste the list back from the exercise instructions, please.",
        )
    if not output:
        if "print" in solution:
            fail(
                """You printed nothing, proofread your code,
your `print` is never called maybe?"""
            )
        else:
            fail(
                "You printed nothing, did you forget to call the "
                "[print()](https://docs.python.org/3/library/functions.html#print) "
                "function?"
            )
    if "\n" in output:
        lines = output.split("\n")
        fail(
            f"""I'm asking for the biggest one, you're printing {len(lines)} lines.

You printed:

{code(output)}"""
        )
    if "," in output:
        fail(
            f"""I'm asking for the biggest number, but I see a coma in your output,
it does not looks like a number.

You printed:

{code(output)}"""
        )
    try:
        int(output)
    except ValueError:
        if "430158267" in output:
            fail(
                f"""I'm expecting a number, you're giving:

{code(output)}"""
            )
        if "1871655963" in output:
            fail(
                f"""Looks like the right answer, but I just need a single number,
no words, please simplify you `print()`.
You're giving:

{code(output)}"""
            )
        fail(
            f"""I'm expecting a number, you're giving:

{code(output)}"""
        )
    if output == "143266561":
        fail(
            """Sure? You printed the first one, but the 2nd one is bigger,
maybe an issue in your implementation?"""
        )
    if output == "430158267":
        fail("Sure? You printed the last one, which looks small to me.")
    if output != "1871655963":
        fail(f"Sure? I get another one, you gave: `{output}`.")


if __name__ == "__main__":
    check()
