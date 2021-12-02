from correction_helper import code, exclude_file_from_traceback, fail, student_code

exclude_file_from_traceback(__file__)


with student_code():
    from solution import City, School, Student


SCHOOL = {
    "alice": (1, 2, 3),
    "bob": (2, 3, 4),
    "catherine": (3, 4, 5),
    "daniel": (4, 5, 6),
}


def check():
    with student_code(prefix="While creating `Student` objects"):
        ada = Student("ada")
        alan = Student("alan")
    with student_code(prefix="While adding exams"):
        ada.add_exam(1.1)
        ada.add_exam(2.2)
        alan.add_exam(3.3)
        alan.add_exam(4.4)
    with student_code(prefix="While calling your `get_mean` method"):
        equals = ada.get_mean() == alan.get_mean()
    if ada.get_mean() is None:
        fail(
            "If I create just one students (no school, no city), "
            "assign it a few marks, an call `get_mean()`, I'm getting `None`.",
            "I expected a value.",
        )
    if equals:
        fail(
            """If I create just two students (no school, no city),
assign them different marks (like 1 for the first, 2 for the other),
they end up with the same mean, which is wrong.

Maybe you stored marks as a class attribute instead of an instance attribute?

Or used a mutable default argument?""",
        )
    with student_code():
        paris = City("paris")
        hkis = School("hkis")
        paris.add_school(hkis)
    if not hasattr(paris, "name"):
        fail("""You city should have a `name` attribute.""")
    if paris.name != "paris":
        fail(
            """I created `paris = City("paris")`, and checked for `city.name`,
I expected to get `'paris'` back, but you gave `{city_name!r}`""".format(
                city_name=paris.name
            )
        )
    for student_name, student_marks in SCHOOL.items():
        with student_code():
            student = Student(student_name)
        for mark in student_marks:
            with student_code():
                student.add_exam(mark)
        with student_code():
            hkis.add_student(student)

    with student_code():
        best_school = paris.get_best_school()
    if best_school is None:
        fail(
            """You `City.get_best_school` function is returning `None`,
expected a `School` instance."""
        )
    with student_code():
        paris_school_name = best_school.name
    if paris_school_name != "hkis":
        fail(
            "In my first test with a single school, you're not telling me my"
            "single school is the best, it obviously is. You're giving me:",
            code(paris_school_name),
        )
    with student_code():
        best_student = paris.get_best_student()
    if not isinstance(best_student, Student):
        fail(
            f"""Your City's `get_best_student` is returning a `{type(best_student)}`
instead of a `Student`."""
        )
    with student_code():
        best_student_name = best_student.name
    if best_student_name != "daniel":
        fail(
            "In a city with a single school with 4 students like:",
            code(repr(SCHOOL), "python"),
            "If I ask you for the best student of the city, "
            "you're not telling me the best student is daniel with 4,5,6, "
            "you're giving me:",
            code(repr(best_student), "python"),
            f"whose name is `{repr(best_student_name)}`.",
        )


if __name__ == "__main__":
    check()
