import os

from correction_helper import code, exclude_file_from_traceback, fail, run

exclude_file_from_traceback(__file__)


def validate_format(output):
    if ", " not in output:
        fail(
            f"""You're expected to write two logins, separated by a coma and a space.
I don't find the coma-space thing in your output, you printed:

{code(output)}
"""
        )
    if "\n" in output:
        fail(
            f"""You're expected to write two logins, separated by a coma and a space.
I see multiple line, while it should fit on a single line, you printed:

{code(output)}
"""
        )


def check_no_leave():
    with open("francejs.csv", "w") as francejs:
        francejs.write("""1,1380612632141,"mdk","oa: Hello :)"\n""")
        francejs.write("""1,1380612679888,"oa","mdk: salut"\n""")
        francejs.write("""4,1380612632141,"mdk2","oa2: Hello :)"\n""")
        francejs.write("""4,1380612679888,"oa2","mdk2: salut"\n""")
        francejs.write("""4,1380612632141,"mdk2","oa2: Hello :)"\n""")
        francejs.write("""4,1380612679888,"oa2","mdk2: salut"\n""")

    output = run("solution.py")
    validate_format(output)
    if output == "mdk2, oa2" or output == "oa2, mdk2":
        fail(
            """The first column indicates the message type.
Leaving the chan is not speaking.
"""
        )


def check_one_clique():
    with open("francejs.csv", "w") as francejs:
        francejs.write("""1,1380612632141,"mdk","oa: Hello :)"\n""")
        francejs.write("""1,1380612679888,"oa","mdk: salut"\n""")

    output = run("solution.py")
    validate_format(output)
    if output != "mdk, oa" and output != "oa, mdk":
        fail(
            f"""For a very simple test with only two lines, it does not work.
Expected:

    mdk, oa

(or `oa, mdk`, I don't care about the order)

Got:

{code(output)}
"""
        )


def check_two_cliques():
    with open("francejs.csv", "w") as francejs:
        francejs.write("""1,1380612632141,"mdk","oa: Hello :)"\n""")
        francejs.write("""1,1380612679888,"oa","mdk: salut"\n""")
        francejs.write("""1,1380612632141,"mdk2","oa2: Hello :)"\n""")
        francejs.write("""1,1380612679888,"oa2","mdk2: salut"\n""")
        francejs.write("""1,1380612632141,"mdk2","oa2: Hello :)"\n""")
        francejs.write("""1,1380612679888,"oa2","mdk2: salut"\n""")

    output = run("solution.py")
    validate_format(output)
    if output == "mdk, oa" or output == "oa, mdk":
        fail("I found a group speaking more than this one")


def check_spaces():
    with open("francejs.csv", "w") as francejs:
        francejs.write("""1,1380612632141,"mdk","oa: Hello :)"\n""")
        francejs.write("""1,1380612679888,"oa","mdk: salut"\n""")
        francejs.write("""1,1380612632141,"mdk2","oa2 : Hello :)"\n""")
        francejs.write("""1,1380612679888,"oa2","mdk2 : salut"\n""")
        francejs.write("""1,1380612632141,"mdk2","oa2 : Hello :)"\n""")
        francejs.write("""1,1380612679888,"oa2","mdk2 : salut"\n""")

    output = run("solution.py")
    validate_format(output)
    if output == "mdk, oa" or output == "oa, mdk":
        fail("Some are putting spaces before the column when highlighing someone :(")


def main():
    try:
        check_no_leave()
        check_one_clique()
        check_two_cliques()
        check_spaces()
    finally:
        try:
            os.unlink("francejs.csv")
        except Exception:
            pass


if __name__ == "__main__":
    main()
