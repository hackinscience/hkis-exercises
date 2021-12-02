This is a triple exercise, it's an introduction to sorting lists in Python.


### Exercise 1

Write a function `sort_a_list` that takes a list as argument and
return the list sorted in the descending order, such as:

```python
>>> sort_a_list([1, 3, 2, 4, 6, 5, 9, 7])
[9, 7, 6, 5, 4, 3, 2, 1]
```

Beware, I'll test it with other types, not only integers!
But always with list of elements of the same type.


### Exercise 2

Given a list where each element is a pair of a mark, and a student
name, such as:

```python
>>> my_class = [(85, 'Susan Maddox'), (6, 'Joshua Tran'), (37, 'Jeanette Wafer')]
```

Write a function named `sort_by_mark` that take as argument a similar
list and returns it sorted by **mark** in **descending** order. Such as:

```python
>>> sort_by_mark(my_class)
[(85, 'Susan Maddox'), (37, 'Jeanette Wafer'), (6, 'Joshua Tran')]
```

### Exercise 3

Write a function named `sort_by_name` that take as argument a similar
list and returns it sorted by **name** in **ascending** order, such as:

```python
>>> sort_by_name(my_class)
[(37, 'Jeanette Wafer'), (6, 'Joshua Tran'), (85, 'Susan Maddox')]
```


# Advices

Take a look at the [Sorting howto](https://docs.python.org/fr/3/howto/sorting.html).
