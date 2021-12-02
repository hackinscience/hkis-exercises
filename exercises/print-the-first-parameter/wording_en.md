Write a script that print the first parameter given to the script.

!!! warning
    You should work on this exercise with your own installation of Python,
    on your computer. Learn how for
    [Mac OSX](https://framagit.org/hackinscience/hkis-website/wikis/How-to-work-on-an-exercise-from-Mac-OSX)
    or [Windows](https://framagit.org/hackinscience/hkis-website/wikis/How-to-work-on-an-exercise-from-Windows).

If there is no parameters given, it should print the following error
message on **stdout**:

`usage: python3 solution.py PARAM`

## Advice

Maybe you'll need to import a few modules in your program.


## Example

```bash
julien@localhost$ python3 solution.py antoine
antoine
julien@localhost$ python3 solution.py julien
julien
julien@localhost$ python3 solution.py
usage: python3 solution.py PARAM
julien@localhost$
```

## references

if: <https://docs.python.org/3/reference/compound_stmts.html#if>

sys.argv: <https://docs.python.org/3/library/sys.html#sys.argv>

len: <https://docs.python.org/3/library/functions.html#len>
