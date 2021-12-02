Write a program that do basic calculations.

!!! warning
    You should work on this exercise with your own installation of Python,
    on your computer. Learn how for
    [Mac OSX](https://framagit.org/hackinscience/hkis-website/wikis/How-to-work-on-an-exercise-from-Mac-OSX)
    or [Windows](https://framagit.org/hackinscience/hkis-website/wikis/How-to-work-on-an-exercise-from-Windows).

You need to be able to get basic operators such as `+`, `-` , `*`,
`/`, `%` (modulo) and `^` (Exponentiation).  Input will be integer
numbers.

Your program will give a usage message if you don't give the three parameters.

For every other errors like if an operand is not an integer, you'll
print an `input error`.

## Examples

```bash
oa@localhost$ ./solution.py 1 + 1
2
oa@localhost$ ./solution.py
usage: ./solution.py a_number (an_operator +-*/%^) a_number
oa@localhost$ ./solution.py 1 / 0
input error
oa@localhost$
```

## Advices

On **Mac** and **Linux** (shell), to input an asterix to a python script you must type `\*` or `"*"`, such as:

```bash
mbp|110-$ python solution.py 3 / 5
0.6
mbp|110-$ python solution.py 3 + 5
8
mbp|110-$ python solution.py 3 - 5
-2
mbp|110-$ python solution.py 3 * 5
usage: python3 ./solution.py a_number (an_operator +-*/%^) a_number
mbp|110-$ python solution.py 3 \* 5
15
```

Similarly, on **Windows** with Command Prompt, `^` must be passed with double quotes: `"^"`.
