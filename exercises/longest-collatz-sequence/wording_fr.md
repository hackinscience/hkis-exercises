The [collatz sequence](https://simple.wikipedia.org/wiki/Collatz_sequence)
goes like this:

- Start by any number greater than zero.
- If your number is even, divide it by two.
- If your number os odd, multiply by three and add one.

For example, starting by `10` we have:

    10 → 5 → 16 → 8 → 4 → 2 → 1

Write a function, named `collatz_length`, given a number the function return
the length of the sequence before reaching 1, for example:

```python
>>> collatz_length(10)
6
```

Because it takes 6 steps (6 `→` in the previous example) to reach 1.


## Advice

Have fun.
