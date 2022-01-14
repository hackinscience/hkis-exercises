In the given snippet, there's a bug: there's no indentation.

Your goal is to fix it (by just adding 4 spaces at the right place).

The code should display:

```text
Gonna knock three times:
*knock*
*knock*
*knock*
- Who's there?
```


## What's indentation?

As you may have guessed by reading the actual code, after the `for`
line asking Python to repeat three times, Python can't guess what
should be repeated: should Python only repeat `print("*knock*")` or
should Python print the two following `print`?

To indicate this in Python we do use 4 spaces in front of the lines, like this:


```python
for i in range(5):
    print("Hello")
```

which will display:

```text
Hello
Hello
Hello
Hello
Hello
```
