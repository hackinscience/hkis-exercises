Write a function called `mul` taking a single iterable argument.

The function have to multiply all values from the given iterable.

As an example `mul([1, 2, 3])` should compute 1 × 2 × 3.

It is not usefull to use `print` in this kind of functions (you can still, for debugging purpose),
better use `return` so the result is given back to the caller, and can be used again.

It could then be used like:

```python
print(mul([1, 2, 3]))  # prints 6
print(mul([0, 1, 2, 3]))  # prints 0
print(mul([2, 3, 4]))  # prints the result of 2 * 3 * 4, being 24
print(mul([2, 3, 4]) + mul([1, 2]))  # prints the result of 2×3×4 + 1×2, which is 48
```
