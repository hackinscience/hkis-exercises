!!! warning
    It's better to try this exercise with your own installation of Python,
    on your computer. Learn how for
    [Mac OSX](https://framagit.org/hackinscience/hkis-website/wikis/How-to-work-on-an-exercise-from-Mac-OSX)
    or [Windows](https://framagit.org/hackinscience/hkis-website/wikis/How-to-work-on-an-exercise-from-Windows).

Write a program which reads and prints the content of the `words.txt`
file.  That's all. I'll put the file is in the same directory as your
code, so no absolute path required, just `"words.txt"` (or
`"./words.txt"`).


## Advice

You can use the [`open` builtin
function](https://docs.python.org/fr/3/library/functions.html#open) or
[pathlib](https://docs.python.org/fr/3/library/pathlib.html#pathlib.Path.read_text).

If you're running this exercise on your computer, with your own
Python, you can try this exercise by manually creating a `words.txt`
file, in the same directory than your Python file, write some words in
it.

My test code will create the file before running your code, don't
worry, don't write code to create the file, don't write code to write
in the file, just read it.
