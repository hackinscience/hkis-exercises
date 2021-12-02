Write a program that print the result of simple addition.

!!! warning
    You should work on this exercise with your own installation of Python, 
    on your computer. Learn how for 
    [Mac OSX](https://framagit.org/hackinscience/hkis-website/wikis/How-to-work-on-an-exercise-from-Mac-OSX) 
    or [Windows](https://framagit.org/hackinscience/hkis-website/wikis/How-to-work-on-an-exercise-from-Windows).

If no parameters are given, you must print the following error message:

`usage: python3 solution.py OP1 OP2`

## Example

```bash
julien@localhost$ python3 solution.py 1 2
3
julien@localhost$ python3 solution.py 2 3
5
julien@localhost$ python3 solution.py
usage: python3 solution.py OP1 OP2
julien@localhost$
```

## Hints

To get the parameters given from the command line, you'll need [sys.argv](https://docs.python.org/3/library/sys.html#sys.argv).
