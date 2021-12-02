Print the number of characters in the given paragraph.

I prefilled the answer box with the paragraph, and assigned it the
name `whetting_your_appetite`.

Just in case you lose it, here it is, so you can copy/paste it:

```python
whetting_your_appetite = "Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms."
```


## Advice

You'll need the
[`len`](https://docs.python.org/3/library/functions.html#len)
function, which can measure almost anything: lists, strings, …

If you feel lost, you should start by reading the
[string tutorial](https://docs.python.org/3/tutorial/introduction.html#strings).

You don't have to edit line 1-12, write your code below the `# Enter your code below:`
comment and don't forget to use the [print](https://docs.python.org/3/library/functions.html#print)
function to print the result!


## How do functions work

A function is a named thing, that take a value (or multiple ones), do
something with it, and often give back another value.

A basic example would be the `max` function that take multiple values
and give back the biggest one, the syntax is:

```python
max(1, 5, 2)
```

and it would give back `5`.

What's given back by a function can be used:

- By naming the given value using a variable.
- By passing the given value directly to another function.

Typically if you want to print the `5` from the previous example, you
can either do:

```python
biggest_one = max(1, 5, 2)
print(biggest_one)
```

or:

```python
print(max(1, 5, 2))
```
