from random import choice

import correction_helper as checker

checker.exclude_file_from_traceback(__file__)


ARRONDISSEMENTS = [
    "I",
    "II",
    "III",
    "IV",
    "V",
    "VI",
    "VII",
    "VIII",
    "IX",
    "X",
    "XI",
    "XII",
    "XIII",
    "XIV",
    "XV",
    "XVI",
    "XVII",
    "XVIII",
    "XIX",
    "XX",
]


def gen_path(size):
    return [choice(ARRONDISSEMENTS) for _ in range(size)]


with checker.student_code():
    from solution import love_meet, affair_meet


def main():
    # Basic verifications:
    bob_path = gen_path(4)
    alice_path = gen_path(4)
    silvester_path = gen_path(4)
    check_love_meet(alice_path, bob_path)
    check_love_meet(["I", "II"], ["II", "III"])
    bob_path = gen_path(4)
    alice_path = gen_path(4)
    silvester_path = gen_path(4)
    check_affair_meet(alice_path, bob_path, silvester_path)

    # Typical bad case
    check_affair_meet(["I", "II", "III"], ["I", "II"], ["II", "III"])

    # OK ... nice ... more in-depth verifications just in case:
    for difficulty in [3, 10, 50]:
        for _ in range(5):
            bob_path = gen_path(difficulty)
            alice_path = gen_path(difficulty)
            silvester_path = gen_path(difficulty)
            check_love_meet(alice_path, bob_path)
    for difficulty in [3, 10, 50]:
        for _ in range(5):
            bob_path = gen_path(difficulty)
            alice_path = gen_path(difficulty)
            silvester_path = gen_path(difficulty)
            check_affair_meet(alice_path, bob_path, silvester_path)


def check_love_meet(alice_path, bob_path):
    with checker.student_code(
        prefix=[
            "While testing your function as:",
            checker.code(f"love_meet({bob_path!r}, {alice_path!r})", "python"),
        ],
    ):
        answer = love_meet(bob_path, alice_path)
    if not isinstance(answer, set):
        if answer is None:
            checker.fail(
                """From `love_meet`, I expected a
    [set](https://docs.python.org/3/library/stdtypes.html#set), got `None`.""",
                "Maybe you forgot the `return` statement?",
            )
        checker.fail(
            f"""From love_meet, I expected a
    [set](https://docs.python.org/3/library/stdtypes.html#set), you gave a
    {type(answer)!r}"""
        )
    messages = [
        "# Exercise one",
        "If Alice goes to districts:",
        checker.code(alice_path),
        "And Bob to:",
        checker.code(bob_path),
        "Your `love_meet` function returns:",
        checker.code(answer),
    ]
    for district in answer:
        if district not in alice_path:
            checker.fail(
                *messages,
                f"Your `love_meet` function says they can meet in district {district} "
                "in which Alice never goes!!",
            )
        if district not in bob_path:
            checker.fail(
                *messages,
                f"Your `love_meet` function says they can meet in district {district} "
                "in which Bob never goes!!",
            )
    for common in set(alice_path) & set(bob_path):
        if common not in answer:
            checker.fail(
                *messages,
                "Your `love_meet` function forgot to say Alice and Bob "
                f"can meet in district {common}",
            )


def check_affair_meet(alice_path, bob_path, silvester_path):
    code = checker.code(
        f"affair_meet({bob_path!r}, {alice_path!r}, {silvester_path!r})",
        "python",
    )
    with checker.student_code(prefix=["While calling your function as:", code]):
        answer = affair_meet(bob_path, alice_path, silvester_path)
    messages = [
        "# Exercise 1",
        "Looks fine!",
        "# Exercise 2",
        "If Alice goes to districts:",
        checker.code(alice_path),
        "Bob to districts:",
        checker.code(bob_path),
        "And Silvester to:",
        checker.code(silvester_path),
        "Your `affair_meet` function returns:",
        checker.code(answer),
    ]
    if not isinstance(answer, set):
        checker.fail(
            "From `affair_meet`, called as:",
            code,
            "I expected a [set](https://docs.python.org/3/library/stdtypes.html#set), "
            f"you gave a {type(answer)!r}",
        )

    for district in bob_path:
        if district in answer:
            checker.fail(
                *messages,
                "Your `affair_meet` function tells Alice and Silvester can meet in "
                f"district `{district}`, but Bob sometime goes there!!",
            )
    for district in answer:
        if district not in alice_path:
            checker.fail(
                *messages,
                "Your `affair_meet` function tells Alice and Silvester can meet in "
                f"district `{district}`, but Alice never goes there!!",
            )
        if district not in silvester_path:
            checker.fail(
                *messages,
                "Your `affair_meet` function tells Alice and Silvester can meet in "
                f"district `{district}`, but Silvester never goes there!!",
            )


if __name__ == "__main__":
    main()
    print("♥ It works! They can meet thanks to Python! ♥")
