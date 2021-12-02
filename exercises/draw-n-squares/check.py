import correction_helper as checker

checker.exclude_file_from_traceback(__file__)

with checker.student_code():
    from solution import draw_n_squares


CHECKS = {
    1: """
+---+
|   |
+---+
""".strip(),
    3: """
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
""".strip(),
    5: """
+---+---+---+---+---+
|   |   |   |   |   |
+---+---+---+---+---+
|   |   |   |   |   |
+---+---+---+---+---+
|   |   |   |   |   |
+---+---+---+---+---+
|   |   |   |   |   |
+---+---+---+---+---+
|   |   |   |   |   |
+---+---+---+---+---+
""".strip(),
}


def check():
    for i in (1, 3, 5):
        with checker.student_code(
            prefix=[
                "While calling your function as:",
                checker.code(f"draw_n_squares({i})", "python"),
            ]
        ):
            result = draw_n_squares(i)
        if type(result) != str:
            if result is None:
                checker.fail("Your function returns `None`, it should return a `str`.")
            checker.fail(
                f"Your function returns a `{type(result)}`, it should return a `str`."
            )
        if CHECKS[i] != result.strip():
            checker.fail(
                f"Your rectangle is wrong for size {i}, expected:",
                checker.code(CHECKS[i]),
                "But your function returned:",
                checker.code(result.strip()),
            )


if __name__ == "__main__":
    check()
