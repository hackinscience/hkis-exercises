import sys
from itertools import permutations

import correction_helper as checker

checker.exclude_file_from_traceback(__file__)

with checker.student_code():
    from solution import how_to_pay


def test(amount, coins, expected):
    args = (amount, coins)
    with checker.student_code(
        prefix=f"While testing `how_to_pay({amount}, {coins!r})`"
    ):
        their = how_to_pay(amount, coins.copy())
    if their is None:
        checker.fail(
            f"Your function, called as `how_to_pay{args!r}` returned `None`.",
            "Maybe you forgot the `return` statement?",
        )
    if not isinstance(their, dict):
        checker.fail(
            f"Your function, called as `how_to_pay{args!r}` "
            f"returned a `{type(their)}`.",
            "I expected a `dict`.",
        )
    for coin, value in their.items():
        if not isinstance(coin, int):
            checker.fail(
                f"Your function, called as `how_to_pay{args!r}` "
                "returned a `dict` with something else than integer (coins values) "
                "as keys:",
                checker.code(their),
            )
    clean_expected = {k: v for k, v in expected.items() if v != 0}
    clean_their = {k: v for k, v in their.items() if v != 0}
    if clean_expected != clean_their:
        print("I do not agree with your result:\n\n")
        print(f"I called `how_to_pay{args!r}`\n\n")
        if not clean_expected:
            print("I think the best way is to give nothing.")
        else:
            print("I think the best way is to give:\n")
            for value, qty in clean_expected.items():
                try:
                    if value < 10:
                        name = "coin"
                    else:
                        name = "bill"
                except ValueError:
                    name = "??"
                print(f"- {qty!r} {name} of {value!r}")
        if not clean_their:
            print("\n\nYour implementation told to gave nothing.\n")
        else:
            print("\n\nYour implementation gave:\n")
            for value, qty in clean_their.items():
                try:
                    if value < 10:
                        name = "coin"
                    else:
                        name = "bill"
                except ValueError:
                    name = "??"
                print(f"- {qty!r} {name} of {value!r}")
        sys.exit(1)


def main():
    euro = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    test(0, euro, {})
    for amount in euro:
        test(amount, euro, {amount: 1})
    for coin1, coin2 in permutations(euro, 2):
        test(coin1 + coin2, euro, {coin1: 1, coin2: 1})
    for coin1, coin2, coin3 in permutations(euro, 3):
        test(coin1 + coin2 + coin3, euro, {coin1: 1, coin2: 1, coin3: 1})
    test(3, euro, {1: 1, 2: 1})
    test(101, euro, {100: 1, 1: 1})
    test(666, euro, {500: 1, 100: 1, 50: 1, 10: 1, 5: 1, 1: 1})


if __name__ == "__main__":
    main()
