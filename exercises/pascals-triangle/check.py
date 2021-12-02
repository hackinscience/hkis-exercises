import re
from itertools import zip_longest

from correction_helper import code, fail, run, student_code, exclude_file_from_traceback

exclude_file_from_traceback(__file__)


# fmt: off
TRIANGLE = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
    [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1],
    [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1],
    [1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1],
    [1, 13, 78, 286, 715, 1287, 1716, 1716, 1287, 715, 286, 78, 13, 1],
    [1, 14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1],
    [1, 15, 105, 455, 1365, 3003, 5005, 6435, 6435, 5005, 3003, 1365, 455, 105, 15, 1],
    [1, 16, 120, 560, 1820, 4368, 8008, 11440, 12870, 11440, 8008, 4368, 1820, 560, 120, 16, 1],  # noqa: E501
    [1, 17, 136, 680, 2380, 6188, 12376, 19448, 24310, 24310, 19448, 12376, 6188, 2380, 680, 136, 17, 1],  # noqa: E501
    [1, 18, 153, 816, 3060, 8568, 18564, 31824, 43758, 48620, 43758, 31824, 18564, 8568, 3060, 816, 153, 18, 1],  # noqa: E501
    [1, 19, 171, 969, 3876, 11628, 27132, 50388, 75582, 92378, 92378, 75582, 50388, 27132, 11628, 3876, 969, 171, 19, 1],  # noqa: E501
]
# fmt: on


def check_triangle(n, output):
    """Check if student's triangle (in output) match a correct Pascal's
    triangle of height *n*.
    """
    for line_no, (my_line, their_line) in enumerate(
        zip_longest(TRIANGLE[:n], output.split("\n")), start=1
    ):
        if my_line is None:
            fail(
                f"For a triangle of size {n}, "
                f"on line {line_no}, I'm not expecting anything, it's the end.",
                "But you printed something!",
                "Your full output is:",
                code(output),
            )
        my_line_str = " ".join(str(i) for i in my_line)
        if their_line is None:
            fail(
                f"For a triangle of size {n}, "
                f"on line {line_no}, I'm expecting to see: "
                f"`{my_line_str}`, "
                "but you printed nothing.",
                "Your full output is:",
                code(output),
            )
        unexpected_chars = re.sub("[ 0-9]", "", their_line)
        if unexpected_chars:
            unexpected_chars = "".join(set(unexpected_chars))
            fail(
                f"Found some unexpected characters (`{unexpected_chars}`).",
                "Your full output is:",
                code(output),
            )
        their_line_as_integers = [int(i) for i in their_line.split()]
        if my_line != their_line_as_integers:
            fail(
                f"""For a triangle of size {n},
on line {line_no}, there's an error,
I expected the following values: `{my_line!r}`,
but you give those values: `{their_line_as_integers!r}`,
your full output is:""",
                code(output),
            )


def main():
    run("solution.py")
    with student_code():
        from solution import print_pascal_triangle

    for n in range(1, 20):
        with student_code(print_allowed=None) as output:
            print_pascal_triangle(n)
        check_triangle(n, output.out)


if __name__ == "__main__":
    main()
