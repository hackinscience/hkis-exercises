from pathlib import Path

from correction_helper import code, exclude_file_from_traceback, fail, run

exclude_file_from_traceback(__file__)


def check():
    output = run("solution.py")
    if output == "42":
        print("""42 est la bonne réponse, bien joué !""")
        exit(0)
    solution = Path("solution.py").read_text()
    if any(quote in solution for quote in ('"', "'")):
        fail(
            "Si vous utilisez des guillemets, ce n'est pas un nombre, "
            "mais une chaîne de caractères",
            "Votre code affiche :",
            code(output),
        )
    if "print" not in solution and "42" in solution:
        fail(
            """Vous n'êtes pas dans un REPL Python ici,
il n'y a donc pas de [print](https://docs.python.org/3/library/functions.html#print)
implicite, vous devez appeler la fonction `print()`."""
        )
    if not output:
        fail(
            """Votre code n'affiche rien, avez-vous oublié d'appeler la fonction
[print](https://docs.python.org/3/library/functions.html#print) ?"""
        )
    if "42" in output:
        fail(
            "Presque ! J'ai juste besoin d'un `42`, rien de plus, rien de moins.",
            "Votre code affiche :",
            code(output),
        )
    fail(
        """Ça n'est pas bon. J'ai juste besoin que votre code
[affiche](https://docs.python.org/3/library/functions.html#print) `42`.""",
        "Votre code m'a affiché :",
        code(output),
    )


if __name__ == "__main__":
    check()
