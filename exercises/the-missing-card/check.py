from itertools import product
from random import shuffle

from correction_helper import code, exclude_file_from_traceback, fail, student_code

exclude_file_from_traceback(__file__)

with student_code():
    from solution import missing_card


def check_deck(deck, expected):
    with student_code(
        prefix=[
            "While calling your `missing_card` function as:",
            code(f"missing_card({deck!r})", "python"),
        ]
    ):
        missing = missing_card(deck)
    if not isinstance(missing, str):
        fail(
            f"Your `missing_card` function returned a `{type(missing)}` (`{missing!r}`)"
            ", I expected a string."
        )
    more = ""
    if len(missing) > 5:
        more = "(I just need the name of the card, nothing more, keep it simple.)"
    elif " " in missing:
        more = "(Beware, there's a space in your output)"
    if missing != expected:
        fail(
            f"With the following deck (missing card is `{expected}`):",
            code(deck, "text"),
            "You're returning:",
            code(missing, "text"),
            more,
        )


def check():
    colors = {"S", "H", "D", "C"}
    values = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}
    for _ in range(10):
        all_cards = [a + b for a, b in product(colors, values)]
        shuffle(all_cards)
        missing = all_cards.pop()
        check_deck(" ".join(all_cards), missing)


if __name__ == "__main__":
    check()
