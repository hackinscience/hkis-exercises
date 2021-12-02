You're working for a restaurant and they're asking you to genrate the sorbet menu.


Provide a script printing every possible sorbet duos from a given list
of flavors.

Don't print recipes with twice the same flavor (no "Chocolate
Chocolate"), and don't print twice the same recipe (if you print
"Vanilla Chocolate", don't print "Chocolate Vanilla", or vice-versa).

The flavors are:

```python
FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]
```

Print one duo per line, and separate flavors by comas, so your output
should look like:

```text
Banana, Chocolate
Banana, Lemon
Banana, Pistachio
Banana, Raspberry
Banana, Strawberry
Banana, Vanilla
Chocolate, Lemon
…
```
