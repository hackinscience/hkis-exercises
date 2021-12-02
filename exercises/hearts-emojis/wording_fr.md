Find all the emojis containing a heart (usefull on social networks, I bet).

Given almost any character in almost any alphabet has an attributed
number in the [Unicode table](https://unicode-table.com/en/) (from 1 to 230000),
you could access them using the
[range](https://docs.python.org/fr/3/library/functions.html#range) and
the [chr](https://docs.python.org/fr/3/library/functions.html#chr) functions.

Using the
[unicodedata](https://docs.python.org/fr/3/library/unicodedata.html#unicodedata.name)
module, specifically its `name` function, you could filter them to
keep only those having 'HEART' in their name. Print characters all in a
single line without any separator (not their names).

```bash
mbp|~-$ python3 solution.py
[Some hearts and some undisplayable characters as your terminal don't know how to render them]
mbp|~-$
```

Beware, `unicodedata.name` throws an exception when a character has no
name, give it an empty second parameter to avoid it.
