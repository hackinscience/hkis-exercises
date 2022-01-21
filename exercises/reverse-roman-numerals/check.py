from correction_helper import exclude_file_from_traceback, fail, student_code

exclude_file_from_traceback(__file__)

with student_code():
    from solution import from_roman_numeral

# fmt: off
FROM_WIKIPEDIA = {
    1000: "M",   100: "C",    10: "X",    1: "I",  # noqa: E241
    2000: "MM",  200: "CC",   20: "XX",   2: "II",  # noqa: E241
    3000: "MMM", 300: "CCC",  30: "XXX",  3: "III",  # noqa: E241
                 400: "CD",   40: "XL",   4: "IV",  # noqa: E241,E131
                 500: "D",    50: "L",    5: "V",  # noqa: E241,E131
                 600: "DC",   60: "LX",   6: "VI",  # noqa: E241,E131
                 700: "DCC",  70: "LXX",  7: "VII",  # noqa: E241,E131
                 800: "DCCC", 80: "LXXX", 8: "VIII",  # noqa: E241,E131
                 900: "CM",   90: "XC",   9: "IX",  # noqa: E241,E131
}
# fmt: on


for decimal, roman in FROM_WIKIPEDIA.items():
    with student_code(prefix=f"While testing `from_roman_numeral({roman!r})`:"):
        result = from_roman_numeral(roman)
    if decimal != result:
        fail(
            f"I expect `from_roman_numeral({roman!r})` to "
            f"return `{decimal}` but your function returned `{result!r}`."
        )
