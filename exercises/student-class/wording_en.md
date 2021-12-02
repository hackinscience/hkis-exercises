Implement a `Student`, `School`, and a `City` classes like so:

 - Student, School, and City have a `name` attribute, given at initialization time.
 - A Student have an `add_exam(grade)` method, recording a new grade for him,
   as a float.
 - A School have an `add_student(student)` method.
 - A City have an `add_school(school)` method.
 - Student, School, and City have a `get_mean()` method giving:
   - For the Student, the average of its results.
   - For the School, the average of the students averages.
   - For the City the average of the School averages.
 - School have a `get_best_student()` method, returning the best `Student`.
 - Cities have a `get_best_school()` and a `get_best_student()`
   methods, returning respectively a `School` and a `Student`..

```python
def main():
    paris = City('paris')
    hkis = School('hkis')
    paris.add_school(hkis)
    for student_name, student_grades in (('alice', (1, 2, 3)),
                                        ('bob', (2, 3, 4)),
                                        ('catherine', (3, 4, 5)),
                                        ('daniel', (4, 5, 6))):
        student = Student(student_name)
        for grade in student_grades:
            student.add_exam(grade)
        hkis.add_student(student)
    print(paris.get_best_school().name)
    print(paris.get_best_student().name)


if __name__ == '__main__':
    main()
```

## References

- Classes: <https://docs.python.org/3/tutorial/classes.html>
