Print the 10 first square number, one per line.

Start at 0, so the first square number is 0<sup>2</sup>, followed by
1<sup>2</sup>, 2<sup>2</sup>, and so on up to 9<sup>2</sup>.

As a reminder, the power operator in Python is written `**`, so:

```pycon
>>> 5 ** 2
25
```

# Advices

You'll need a [for statement](https://docs.python.org/fr/3/tutorial/controlflow.html#for-statements)
to iterate over the [range](https://docs.python.org/fr/3/library/functions.html#func-range) function.

The `for` statement is a tool to traverse things containing items.
Strings, lists, and ranges are things containing items,
so you can use a `for` to iterate their elements, like:

```pycon
>>> for c in "Hello":
...     print("The letter is", c)
...
The letter is H
The letter is e
The letter is l
The letter is l
The letter is o
```

Or like:
```pycon
>>> for i in [1, 10, 100, 1000]:
...     print(i)
...
1
10
100
1000
```

Or:
```pycon
>>> for i in range(10):
...     print(i * 2)
...
0
2
4
6
8
10
12
14
16
18
```
