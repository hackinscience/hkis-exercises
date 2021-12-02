## Description

Find the distance between the two furthest apart values in a list.

Create a `dist` function, receiving a list of numbers (integers or
floating points), and returning the bigger distance between any two
given values, so typically the distance between the biggest and the
smallest, like:

```ipython
>>> dist([1, 2, 3])
2
>>> dist([1, 2, 3, 2.5])
2
>>> dist([1, 2, 3, 2.5, 3.5])
2.5
>>> dist([1, 2, 3, 2.5, 3.5, 120])
119
>>> dist([1, 2, 3, 2.5, 3.5, 120, -1000])
1120
```
