import gettext
from pprint import pformat
from random import randint

import correction_helper as checker

checker.exclude_file_from_traceback(__file__)
_ = gettext.translation(
    "check", "/opt/hkis-celery/exercises/locale/", fallback=True
).gettext


MY_CLASS = [
    [74, "Robert Clouthier"],
    [0, "Kenneth Dwyer"],
    [38, "Theresa Hart"],
    [33, "Edith Hare"],
    [57, "Larry Schlosser"],
    [64, "Tyson Madore"],
    [65, "Johanna Perron"],
    [97, "Juan Berdan"],
    [40, "Jim Ashley"],
    [71, "Dennis Gadson"],
    [11, "Colin Wesley"],
    [89, "Elizabeth Nyquist"],
    [51, "Darron Fowler"],
    [20, "Sam Moyers"],
    [47, "Caryl Sircy"],
    [81, "Gary Scheller"],
    [9, "Paul Curry"],
    [48, "Felice Skiles"],
    [59, "Edgar Kinroth"],
    [84, "Joseph Pedersen"],
    [28, "Amber Savage"],
    [85, "Susan Maddox"],
    [22, "Mark Osbourne"],
    [76, "Gerald Llanes"],
    [19, "Erica Curry"],
    [23, "Gene Smith"],
    [91, "Jerome Benbow"],
    [98, "David Vaughn"],
    [54, "Elizabeth Wilson"],
    [34, "Gerardo Quiroz"],
    [8, "Gerald Bates"],
    [62, "Lindsay Shaffer"],
    [77, "Teresa Bryant"],
    [1, "Roberta Trell"],
    [6, "Joshua Tran"],
    [79, "Robert Washington"],
    [25, "Alan Sanders"],
    [37, "Jeanette Wafer"],
    [36, "John Freeman"],
    [7, "James Cash"],
    [72, "Curtis Johnson"],
    [42, "Lidia Robel"],
    [2, "Carla Coon"],
    [10, "Erlinda Whipps"],
    [83, "Vickie Walden"],
    [61, "Sandra Dyer"],
    [93, "Nicole Mack"],
    [67, "Randy Cann"],
    [99, "Antonio Clow"],
    [35, "Nathan Smith"],
    [75, "Sammie Lane"],
    [5, "David Adriance"],
    [41, "Arthur Rasmussen"],
    [63, "Luis Mccall"],
    [96, "Louis Henderson"],
    [12, "Bonnie Torres"],
    [73, "Jonnie Saska"],
    [27, "Arthur Padilla"],
    [92, "Richard Cullen"],
    [14, "Efrain Vail"],
]


def main():
    my_class = [[x[1], x[0]] for x in MY_CLASS]
    thres = randint(20, 80)
    with checker.student_code(
        print_prefix="""Your code printed something (see below),
while it should just `return` a `dict`."""
    ):
        from solution import select_student
    with checker.student_code(print_prefix="Your `select_student` function prints:"):
        got = select_student(my_class, thres)
    if not isinstance(got, dict):
        if got is None:
            checker.fail(
                "Your function must return a dictionnary, got `None`.",
                "Your full output:",
                checker.code(got),
            )
        checker.fail(
            f"Your function must return a dictionnary, got a `{type(got)}`.",
            "Your full output",
            checker.code(got),
        )
    if "Accepted" not in got:
        checker.fail(
            "Please give at least an `Accepted` key in your result.",
            "Your function returned:",
            checker.code(pformat(got), "python"),
        )
    if "Refused" not in got:
        checker.fail(
            "Please give at least a `Refused` key in your result.",
            "Your function returned:",
            checker.code(pformat(got), "python"),
        )
    try:
        len(got["Accepted"])
        len(got["Refused"])
    except TypeError:
        checker.fail(
            "Your `Accepted` and `Refused` dictionary entries should be measurable.",
            "In other words, I want to be able to call `len()` on them.",
            "In case it helps, here what's your function returned:",
            checker.code(pformat(got)),
        )
    for accepted in got["Accepted"]:
        try:
            name, grade = accepted
        except ValueError:
            checker.fail(
                "The accepted list should contain students as a pair of "
                "`[name, grade]`, like given initially."
            )
        if grade < thres:
            checker.fail(
                f"You accepted student {name} which has a grade of {grade}. "
                f"It's less than the given test threshold of `{thres}`!",
                "In case it helps, here what's your function returned:",
                checker.code(pformat(got)),
            )
    for refused in got["Refused"]:
        try:
            name, grade = refused
        except ValueError:
            checker.fail(
                "The refused list should contain students as a pair of "
                "`[name, grade]`, like given initially."
            )
        if grade >= thres:
            checker.fail(
                f"You refused student {name} which has a grade of {grade}. "
                f"It's more (or equal) than the given test threshold of `{thres}`!",
                "In case it helps, here what's your function returned:",
                checker.code(pformat(got)),
            )
    if sorted(got["Accepted"], key=lambda x: x[1]) == got["Accepted"]:
        checker.fail(
            "Looks like you ordered `Accepted` in ascending order, "
            "while I asked for a descending order here."
        )
    if sorted(got["Refused"], key=lambda x: x[1], reverse=True) == got["Refused"]:
        checker.fail(
            "Looks like you ordered `Refused` in descending order, "
            "while I asked for an ascending order here."
        )
    if sorted(got["Accepted"], key=lambda x: x[1], reverse=True) != got["Accepted"]:
        checker.fail(
            "Looks like you did not ordered properly the `Accepted` list of students. "
            "I need them to be ordered in descending order of grade."
        )
    if sorted(got["Refused"], key=lambda x: x[1]) != got["Refused"]:
        checker.fail(
            "Looks like you did not ordered properly the `Refused` list of students. "
            "I need them to be ordered in ascending order of grade."
        )


if __name__ == "__main__":
    main()
