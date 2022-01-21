from correction_helper import exclude_file_from_traceback, fail, student_code

exclude_file_from_traceback(__file__)

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


with student_code():
    from solution import to_roman_numeral


def check():
    for i, expected in FROM_WIKIPEDIA.items():
        with student_code(prefix=f"While testing `to_roman_numeral({i!r})`:"):
            theirs = to_roman_numeral(i)
        if theirs != expected:
            fail(
                "Roman numeral notation for `{i}`, according to Wikipedia, is "
                f"`{expected}`, not `{theirs}`."
            )
    # ôter I de L ou de C n'est pas pratiqué (49 s'écrit XLIX et non
    # IL ; 99 s'écrit XCIX et pas IC).
    with student_code(prefix="While testing `to_roman_numeral(49)`:"):
        theirs = to_roman_numeral(49)
    if theirs == "IL":
        fail(
            "Roman numeral substractive notation for of `I` "
            "is not allowed with `L` or `C`.",
            "So I don't want your function to represent `49` as `IL` but as `XLIX`.",
        )
    if theirs != "XLIX":
        fail(
            "Roman numeral notation for `49`, according to Wikipedia, is "
            f"`XLIX`, not `{theirs}`."
        )
    with student_code(prefix="While testing `to_roman_numeral(99)`:"):
        theirs = to_roman_numeral(99)
    if theirs == "IC":
        fail(
            "Roman numeral substractive notation for of `I` "
            "is not allowed with `L` or `C`.",
            "So I don't want your function to represent `99` as `IC` but as `XCIX`.",
        )
    if theirs != "XCIX":
        fail(
            "Roman numeral notation for `99`, according to Wikipedia, is "
            f"`XCIX`, not `{theirs}`."
        )


if __name__ == "__main__":
    check()
