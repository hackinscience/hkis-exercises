Write a function computing the perimeter of a circle given its radius.

First read the [function tutorial](https://docs.python.org/3/tutorial/controlflow.html#defining-functions).

Your function should be named `circle_perimeter(radius)`,
where the `radius` parameter is the radius of a cirle.

Your function should return the perimeter of a circle of the given `radius`.

To test it, we will import your function and try it with different values, such as:

```python
>>> circle_perimeter(1)
6.283185307179586
>>> circle_perimeter(10)
62.83185307179586
>>> circle_perimeter(100)
628.3185307179587
```

## Functions

For example, here is a simple function which takes a value and give it back unmodified:

```python
def identity(x):
    return x
```

We can call our `identity` function and check it gave us back the given value:

```pycon
>>> identity(42) == 42
True
```

So:

```pycon
>>> print(42)
42
```

and:

```pycon
>>> print(identity(42))
42
```

are behaving the same. In the first case, we give `42` to `print`,
which prints "42". In the 2nd example we give `42` to `identity`,
which gives back `42`, which is directly given to `print`, printing
"42" again.

We could also compare those equivalent codes:

```pycon
>>> fourty_two = 42
>>> print(fourty_two)
```

```pycon
>>> fourty_two = identity(42)
>>> print(fourty_two)
```

```pycon
>>> fourty_two = 42
>>> fourty_two = identity(fourty_two)
>>> print(fourty_two)
```



## Hints

- Do not print the result, you [function should return it](https://docs.python.org/3/tutorial/controlflow.html#defining-functions).
- You'll need to [import](https://docs.python.org/3/tutorial/modules.html#standard-modules) the standard [math](https://docs.python.org/3/library/math.html) module.
- More specifically you may use [math.pi](https://docs.python.org/3/library/math.html#math.pi) (or [math.tau](https://docs.python.org/3/library/math.html#math.tau)).
