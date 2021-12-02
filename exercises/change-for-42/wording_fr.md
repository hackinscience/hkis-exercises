Given the € currency without cents,
the possible change is composed of:
1, 2, 5, 10, 20, 50, 100, 200, 500

There is 4 ways to change 5 euros:

 - 5
 - 2 + 2 + 1
 - 2 + 1 + 1 + 1
 - 1 + 1 + 1 + 1 + 1

Write a function `changes` that returns how many set of change
can be made for a given amount and a set of coins:

```python
def changes(amount, coins):
    ...
```

Moulinette will call your programm like this:

```
>>> from solution import *
>>> changes(42, (1, 2, 5, 10, 20, 50, 100, 200, 500))
>>> 271
```

For this one, I expect to get 271, in less than 100ms.

Yep, I'll try with other set of pieces and other amounts.

## Advices

Search for dynamic programming or recursive with
memoization, or divide and conquer.
