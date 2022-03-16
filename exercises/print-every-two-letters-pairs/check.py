import ast
import string
from pathlib import Path

import correction_helper as checker

checker.exclude_file_from_traceback(__file__)


def check():
    output = checker.run("solution.py")
    solution = Path("solution.py").read_text(encoding="UTF-8")
    if all(letter in solution for letter in string.ascii_lowercase):
        checker.fail(
            "Don't type the whole alphabet manually.",
            "When you do this, the computer made you work for him: you lost."
            "Instead you should make the computer work for you.",
            "Every time you spot a repetitive task, remember this: "
            "the computer should work, not you."
            "so, you should do:",
            checker.code("import string", "python"),
            "or:",
            checker.code("from string import ascii_lowercase", "python"),
            "Take a look at the"
            "[string]("
            "https://docs.python.org/3/library/string.html#string.ascii_lowercase)"
            "documentation.",
        )
    if output == "\n".join(
        a + " " + b for a in string.ascii_lowercase for b in string.ascii_lowercase
    ):
        checker.fail(
            "You added a space between every letters, like:",
            checker.code("> a b"),
            "which I don't expect. I expect:",
            checker.code("> ab"),
            "instead.",
            "Notice the "
            "[print](https://docs.python.org/3/library/functions.html#print)"
            "function automatically adds a space between each given parameters by"
            "default.",
        )
    if any(letter not in string.ascii_lowercase + "\n" for letter in output):
        checker.fail(
            "I'm asking for letter pairs, one pair per line, like:",
            checker.code("aa\nab\n..."),
            "you printed something unexpected:",
            checker.code(output),
        )

    solution = "\n".join(
        a + b for a in string.ascii_lowercase for b in string.ascii_lowercase
    )
    if not output:
        checker.fail(
            "You printed nothing :(",
            "Did you forgot to call the [print]("
            "https://docs.python.org/3/library/functions.html#print) function?",
        )
    if " object at " in output or "generator object" in output:
        checker.fail(
            "Looks like you printed a generator, see:",
            checker.code(output),
            "A generator is an object ready to give you values,"
            "that may not be already computed.",
            "To actually get the values just iterate over the object,"
            "or give it to the"
            "[list](https://docs.python.org/3/library/functions.html#func-list)"
            "function.",
        )
    if len(output) < len(solution):
        message = ["Your output is a bit short, I expected 26×26 lines."]
        for pair in solution.split("\n"):
            if pair not in output:
                message.append(f"For example, where's {pair!r}?")
                break
        checker.fail(*(message + ["Got:", checker.code(output)]))
    if len(output) > len(solution):
        message = ["Your output seems a bit long"]
        lines = output.split("\n")
        if len(lines) > 1:
            if lines[0] != "aa":
                message.append(f"Your first line is: {lines[0]}, why?")
        checker.fail(*(message + ["Your full output is:", checker.code(output)]))
    if output != solution:
        if output[:10] != solution[:10]:
            checker.fail(
                "Wrong, your answer starts with:",
                checker.code(output[:11]),
                "and mine starts with:",
                checker.code(solution[:11]),
            )
        elif output[-10:] != solution[-10:]:
            checker.fail(
                "Wrong, your answer ends with:",
                checker.code(output[-11:]),
                "and mine ends with:",
                checker.code(solution[-11:]),
            )
        else:
            checker.fail(
                "Wrong, sry, don't know why. Your code printed:", checker.code(output)
            )
    print(checker.congrats())
    print("\nYour code printed:\n")
    print(checker.code(output))


if __name__ == "__main__":
    check()
