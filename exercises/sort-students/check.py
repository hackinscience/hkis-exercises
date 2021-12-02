from operator import itemgetter

from correction_helper import code, exclude_file_from_traceback, fail, run, student_code

exclude_file_from_traceback(__file__)


ALL_CLASS = [
    [6, "Joshua Tran"],
    [37, "Jeanette Wafer"],
    [85, "Susan Maddox"],
    [84, "Joseph Pedersen"],
    [12, "Bonnie Torres"],
    [36, "John Freeman"],
    [27, "Betty Askins"],
    [37, "Melanie Noe"],
    [22, "Mark Osbourne"],
    [42, "Lidia Robel"],
    [9, "Paul Curry"],
    [63, "Tyson Madore"],
    [40, "Jim Ashley"],
    [47, "Rolanda Marks"],
    [42, "Nikki Reed"],
    [1, "Roberta Trell"],
    [74, "Robert Clouthier"],
    [10, "Erlinda Whipps"],
    [35, "Tracy Smith"],
    [97, "Juan Berdan"],
    [71, "Regina Farber"],
    [89, "Elizabeth Nyquist"],
    [71, "Yvette Zak"],
    [27, "Arthur Padilla"],
    [83, "Gary Eggert"],
    [59, "Edgar Kinroth"],
    [14, "Efrain Vail"],
    [19, "Erica Curry"],
    [0, "Kenneth Dwyer"],
    [91, "Jerome Benbow"],
    [62, "Lindsay Shaffer"],
    [81, "Gary Scheller"],
    [25, "Alan Sanders"],
    [92, "Richard Cullen"],
    [98, "David Vaughn"],
    [33, "Edith Hare"],
    [8, "Gerald Bates"],
    [5, "Ruth Keats"],
    [48, "Felice Skiles"],
    [2, "Carla Coon"],
    [7, "James Cash"],
    [97, "Kelly Kawamura"],
    [96, "Louis Henderson"],
    [79, "Robert Washington"],
    [28, "Amber Savage"],
    [38, "Theresa Hart"],
    [41, "Glenn Breland"],
    [47, "Elida Mundy"],
    [71, "Dennis Gadson"],
    [47, "Caryl Sircy"],
    [14, "Frances Brown"],
    [23, "Michael Mayle"],
    [47, "Frederick Cook"],
    [76, "Gerald Llanes"],
    [12, "Constance Dunn"],
    [57, "Larry Schlosser"],
    [71, "Virgil Mclaughlin"],
    [23, "Gene Smith"],
    [75, "Sammie Lane"],
    [54, "Elizabeth Wilson"],
    [33, "Karen Vanderveen"],
    [48, "Robin Anderson"],
    [34, "Gerardo Quiroz"],
    [67, "Randy Cann"],
    [99, "Antonio Clow"],
    [11, "Colin Wesley"],
    [41, "Arthur Rasmussen"],
    [84, "Vincent Raymond"],
    [72, "Curtis Johnson"],
    [5, "David Adriance"],
    [51, "Darron Fowler"],
    [64, "Johanna Perron"],
    [72, "Jonnie Saska"],
    [7, "Regina Miser"],
    [20, "Sam Moyers"],
    [37, "Vera Soriano"],
    [63, "Luis Mccall"],
    [83, "Jenifer Watson"],
    [93, "Nicole Mack"],
    [27, "Marilyn Malloy"],
    [5, "John Ayling"],
    [2, "Cassandra Davis"],
    [61, "Sandra Dyer"],
    [77, "Teresa Bryant"],
    [35, "Nathan Smith"],
    [83, "Vickie Walden"],
    [37, "Samantha Myers"],
]


def main():
    run("solution.py")

    marks_already_seen = set()
    my_class = []

    for elem in ALL_CLASS:
        if elem[0] not in marks_already_seen:
            my_class.append(elem)
        marks_already_seen.add(elem[0])

    with student_code():
        from solution import sort_a_list

    for a_list in (
        ["a", "c", "b"],
        [],
        [3, 2, 1],
        [1, 1, 1],
        [1, 3, 2],
        [3.3, 2.2, 5.5, 8.8, 1.1],
    ):
        with student_code(prefix=f"While calling `sort_a_list({a_list!r})`"):
            their = sort_a_list(a_list.copy())
        if their != sorted(a_list, reverse=True):
            if their == sorted(a_list):
                fail(
                    "I called to your `sort_a_list` function like this:",
                    code(f"sort_a_list({a_list!r})", "python"),
                    f"I expect `{sorted(a_list, reverse=True)}`, but got:",
                    code(their),
                    """Looks like you forgot to reverse, read the doc of the
[sorted](https://docs.python.org/3/library/functions.html#sorted) function
(or the [sort method](https://docs.python.org/3/library/stdtypes.html#list.sort))
to learn how it works.
""",
                )

            fail(
                "I called to your `sort_a_list` function like this:",
                code(f"`sort_a_list({a_list!r})`", "python"),
                f"I expected it to **return** `{sorted(a_list, reverse=True)}`, "
                "but got:",
                code(their),
                """Are you ignoring the parameter? The variable name, inside the
parenthesis of your `def sort_a_list` is called a
[parameter](https://docs.python.org/3/tutorial/controlflow.html#defining-functions),
when I call `sort_a_list([1, 2, 3])`, the list `[1, 2, 3]` is bound to
this variable, so you can use it. You don't have to declare another list.
""",
            )

    with student_code():
        from solution import sort_by_mark

    for test_class in [
        [[6, "Alan"], [37, "Ada"], [99, "Boole"], [2, "John"]],
        [[40, "Shannon"], [39, "Boole"], [38, "Conway"], [55, "John"]],
        my_class,
    ]:
        with student_code(prefix=f"While calling `sort_by_mark({test_class!r})`"):
            got = sort_by_mark(test_class.copy())
        expected = sorted(test_class, key=itemgetter(0), reverse=True)
        if got != expected:
            if got == sorted(test_class, key=itemgetter(0), reverse=False):
                fail(
                    """Your `sort_by_mark` function looks to sort in
**ascending** order, while the exercise is to sort in **descending** order."""
                )
            if got == sorted(test_class, key=itemgetter(1), reverse=True):
                fail(
                    """Your `sort_by_mark` function looks to sort in
descending order or **name**, while the exercise is to sort in descending order
of **mark**."""
                )
            if got == test_class:
                fail(
                    "Your `sort_by_mark` function does **not** return a sorted list.",
                    "Maybe you're mixing "
                    "[sort](https://docs.python.org/3/library/stdtypes.html#list.sort)"
                    " and "
                    "[sorted](https://docs.python.org/3/library/functions.html#sorted)",
                )
            if got == list(reversed(test_class)):
                fail(
                    "Your `sort_by_mark` function does **not** return a sorted list.",
                    "It just reverse the given list.",
                    "Maybe you're mixing "
                    "[sort](https://docs.python.org/3/library/stdtypes.html#list.sort)"
                    " and "
                    "[sorted](https://docs.python.org/3/library/functions.html#sorted)",
                    "Also take a look at the `reverse` argument of those functions.",
                )
            if len(test_class) < 10:
                fail(
                    f"I expected `sort_by_mark({test_class!r})` "
                    "to **return** a `list` looking like:",
                    code(expected),
                    f"Got a `{type(got)}` looking like:",
                    code(got),
                )
            else:
                fail("Wrong output for `sort_by_mark`!")

    with student_code():
        from solution import sort_by_name

    for test_class in [
        [[6, "Alan"], [37, "Shannon"]],
        [[40, "Boole"], [39, "Ada"]],
        my_class,
    ]:
        with student_code(prefix=f"While calling `sort_by_name({test_class!r})`"):
            got = sort_by_name(test_class.copy())
        expected = sorted(test_class, key=itemgetter(1))
        if got != expected:
            if got == sorted(test_class, key=itemgetter(1), reverse=True):
                fail(
                    """Your `sort_by_name` function looks to sort in reverse order,
while the exercise is to sort in ascending order."""
                )
            if len(test_class) < 10:
                fail(
                    f"Calling `sort_by_name({test_class!r})` I expected:",
                    code(expected),
                    "Got:",
                    code(got),
                )
            else:
                fail("Wrong output for sort_by_name!")


if __name__ == "__main__":
    main()
