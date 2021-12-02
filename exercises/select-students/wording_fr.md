Write a function telling appart accepted and refused students according to a threshold.

The function should be called `select_student` and takes as arguments:

 - A list where each element is a list of a student name, and his mark.
 - A mark. The student mark must be superior or equal to the given mark to be accepted.

Your function must return a dictionnary with two entries:

 - `Accepted` which list the accepted students sorted by marks in the
   descending order.
 - `Refused` which list the refused students sorted by marks in ascending order.

## Example

```ipython
In [1]: from solution import select_student

In [2]: my_class = [['Kermit Wade', 27], ['Hattie Schleusner', 67], ['Ben Ball', 5], ['William Lee', 2]]

In [3]: select_student(my_class, 20)
Out[3]:
{'Accepted': [['Hattie Schleusner', 67], ['Kermit Wade', 27]],
 'Refused': [['William Lee', 2], ['Ben Ball', 5]]}

In [4]: select_student(my_class, 50)
Out[4]:
{'Accepted': [['Hattie Schleusner', 67]],
 'Refused': [['William Lee', 2], ['Ben Ball', 5], ['Kermit Wade', 27]]}
```
