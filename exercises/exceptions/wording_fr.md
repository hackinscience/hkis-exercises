## Description

This is a rapid introduction about [`Exception`](https://docs.python.org/fr/3/tutorial/errors.html).

In this exercice you'll just have to print the first argument passed to the script:

```python
print(sys.argv[1])
```

**But** without actually checking if `len(sys.argv)` is long enough to have it.

So, sometimes, it will fail with an
[IndexError](https://docs.python.org/fr/3/library/exceptions.html#IndexError).

You'll have to catch this IndexError and print:

`Not enough parameters.`

## Advice

I'll search for any occurence of `if` in your code. If found, I'll reject your
solution, so use `try`.
