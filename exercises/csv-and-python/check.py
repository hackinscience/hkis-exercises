import csv
import datetime
import os
import io
from collections import OrderedDict
from contextlib import suppress
from itertools import zip_longest
from pathlib import Path

import correction_helper as checker

checker.exclude_file_from_traceback(__file__)

with checker.student_code(print_prefix="Your code printed:"):
    from solution import generate_csv, parse_csv

STUDENTS = [
    {
        "Firstname": "Jean",
        "Lastname": "Dupont",
        "Birthdate": datetime.date(2010, 10, 10),
        "Marks": [0, -1, 12],
        "Comments": "The Last one",
    },
    {
        "Firstname": "Ada",
        "Lastname": "Lovelace",
        "Birthdate": datetime.date(1815, 12, 10),
        "Marks": [4242, 1010],
        "Comments": "The first one",
    },
    {
        "Firstname": "Linus",
        "Lastname": "Torvald",
        "Birthdate": datetime.date(1969, 12, 28),
        "Marks": [42, 21],
        "Comments": "Have a problem with penguin",
    },
    {
        "Firstname": "Theo",
        "Lastname": "De Raadt",
        "Birthdate": datetime.date(1968, 5, 19),
        "Marks": [18, 19, 20],
        "Comments": "This guy is just crazy",
    },
    {
        "Firstname": "Dennis",
        "Lastname": "Ritchie",
        "Birthdate": datetime.date(1941, 9, 9),
        "Marks": [20, 20, 20],
        "Comments": "Like a boss",
    },
    {
        "Firstname": "Alan",
        "Lastname": "Turing",
        "Birthdate": datetime.date(1912, 6, 23),
        "Marks": [42, 42, 42],
        "Comments": "Shouldn't eat apple",
    },
    {
        "Firstname": "John",
        "Lastname": "Doe",
        "Birthdate": datetime.date(1984, 12, 30),
        "Marks": [3, 2, 6],
        "Comments": "Not a good element",
    },
]


METEO = [
    (
        ("temperature", 21),
        ("date", datetime.date(2042, 2, 22)),
        ("locations", ("Lyon", "Nime", "Paris")),
        ("weather", "sunny"),
    ),
    (
        ("temperature", -21),
        ("date", datetime.date(2000, 1, 22)),
        ("locations", ["Moscow", "Budapest"]),
        ("weather", "something strange"),
    ),
]

CSV = """temperature,date,locations,weather
21,02/22/2042,"Lyon,Nime,Paris",sunny
-21,01/22/2000,"Moscow,Budapest",something strange
"""


def easy_generate_csv_checks():
    for city in ["ABC", "BCD", "CDE"]:
        test_data = [
            (
                ("temperature", 0),
                ("date", datetime.date(2000, 1, 1)),
                ("locations", (city,)),
                ("weather", "Funny"),
            )
        ]
        prefix = [
            "While testing your function as:",
            checker.code(f"generate_csv({test_data!r})", "python"),
        ]
        with checker.student_code(prefix=prefix):
            generate_csv(test_data.copy())
        try:
            output = Path("results.csv").read_text(encoding="UTF-8")
        except FileNotFoundError:
            checker.fail(
                *prefix,
                "it did not created the `results.csv` file so "
                "I can't really test it.",
            )
        if city not in output:
            checker.fail(
                "Given:",
                checker.code(repr(test_data)),
                "your `generate_csv` function generated a CSV "
                f"not containing {city}!",
                "It contains:",
                checker.code(output),
            )


def constant_generate_csv_check():
    with checker.student_code(
        prefix=[
            "While testing your function as:",
            checker.code(f"generate_csv({METEO!r})", "python"),
        ]
    ):
        generate_csv(METEO.copy())
    try:
        with open("results.csv", encoding="UTF-8") as csvfile:
            csv1_data = csv.DictReader(csvfile)
            csv1_data = [row for row in csv1_data]
    except FileNotFoundError:
        checker.fail(
            """I can't find the `results.csv` file after running your `generate_csv`
function, is there a typo in your file name?"""
        )

    csv2_data = csv.DictReader(io.StringIO(CSV))
    csv2_data = [row for row in csv2_data]
    for i, sol_row in enumerate(csv2_data):
        try:
            line = csv1_data[i]
        except IndexError:
            line = ""
        if sol_row != line:
            checker.fail(
                """Your `generate_csv` function did not generated csv
with the correct data.""",
                "Given:",
                checker.code(METEO),
                "You stored:",
                checker.code(Path("results.csv").read_text(encoding="UTF-8")),
                "which parses as:",
                checker.code(line),
                "I expected:",
                checker.code(CSV),
                "which parses as:",
                checker.code(sol_row),
            )


def generate_csv_check():
    with checker.student_code(prefix="While testing your `parse_csv` function"):
        students_parsing = parse_csv()
    if students_parsing == STUDENTS:
        print("And your `parse_csv` is good too!")
        return  # OK
    if not isinstance(students_parsing, list):
        checker.fail(
            f"""Your `parse_csv` function should return a list,
but it returns: `{type(students_parsing)}`""",
        )
    if len(students_parsing) != len(STUDENTS):
        checker.fail(
            "Your `parse_csv` returned a list, but of the wrong length "
            "(in my test case I expected {} lines, got {}.)".format(
                len(STUDENTS), len(students_parsing)
            )
        )
    for line in students_parsing:
        if not isinstance(line, (dict, OrderedDict)):
            checker.fail(
                f"""Your `parse_csv` function is expected to return a list of dict,
it returned a list of `{type(line)}`."""
            )
    for mine, theirs in zip_longest(STUDENTS, students_parsing):
        if dict(mine) != dict(theirs):
            checker.fail(
                """Your parsed csv function returns a list of dicts,
but we disagree on a line of my example, I'm getting:""",
                checker.code(repr(dict(mine))),
                "While you're giving:",
                checker.code(repr(dict(theirs))),
            )
    if students_parsing != STUDENTS:
        checker.fail("Your `parse_csv` function doesn't return the correct answer")


def check():
    easy_generate_csv_checks()
    constant_generate_csv_check()
    print("Your `generate_csv` function is OK, checking `parse_csv` now…", end="\n\n")
    generate_csv_check()
    print(checker.congrats())


if __name__ == "__main__":
    try:
        check()
    finally:
        with suppress(Exception):
            os.unlink("students.csv")
        with suppress(Exception):
            os.unlink("results.csv")
        with suppress(Exception):
            os.unlink("results-solution.csv")
