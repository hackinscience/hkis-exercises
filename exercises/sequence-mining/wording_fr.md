## Overview

Sequence mining is useful for analyzing list of events when order matters. It's used for example for DNA and natural language analysis.

Here, you'll implement an algorithm to extract common patterns among a set of sequences.


## Exercise

You must provide a function `seq_mining` that takes as argument:

+ A list of strings (representing the sequences), such as:
    - `['CFEDS', 'SKDJFGKSJDFG', 'OITOER']`

+ The minimum proportion of the number of sequences that must have this pattern for being taken into account (float between 0 and 1):
    - if `0.34`, at least a third of the sequences must have a given pattern for the function to return it.

+ The maximum pattern length that must be considered (int)

If a given pattern occurs several time in a sequence, it must be counted only once.

The function `seq_mining` must return a
[`Counter`](https://docs.python.org/fr/3/library/collections.html#collections.Counter)
containing:

- The found patterns as keys
- The number of sequences containing this pattern as values.

In `["ABC", "BCD"]` there are three patterns common to both sequences:

- `B`
- `C`
- `BC`

(`A` and `AB` occurs only in the first string, and `D` and `CD` only
in the last one).


So `seq_mining(["ABC", "BCD"], 0.66, 2)` (searching patterns of length
2 maximum, must appear on at lest 66% of sequences) should return:

```python
Counter({'B': 2, 'C': 2, 'BC': 2})
```

(because as we have only two sequences, 66% already means the two of them)

while `seq_mining(["ABC", "BCD"], 0.33, 2)` (searching patterns of length
2 maximum, must appear on at lest 33% of sequences) should return:

```python
Counter({'C': 2, 'B': 2, 'BC': 2, 'A': 1, 'D': 1, 'AB': 1, 'CD': 1})
```

This tells us that `BC` is found in two sequences while `AB` is found
in a single one.

(because as we have only two sequences, 33% allows a pattern to be
found in a single sequence).


## Exemple

```ipython
In [1]: from solution import seq_mining

In [2]: data = ['ABCD', 'ABABC', 'BCAABCD']

In [3]: seq_mining(data, 0.34, 3)
Out[3]:
Counter({'A': 3,
         'AB': 3,
         'ABC': 3,
         'B': 3,
         'BC': 3,
         'BCD': 2,
         'C': 3,
         'CD': 2,
         'D': 2})

In [4]: seq_mining(data, 0.34, 4)
Out[4]:
Counter({'A': 3,
         'AB': 3,
         'ABC': 3,
         'ABCD': 2,
         'B': 3,
         'BC': 3,
         'BCD': 2,
         'C': 3,
         'CD': 2,
         'D': 2})

In [5]: seq_mining(data, 0.50, 2)
Out[5]: Counter({'A': 3, 'AB': 3, 'B': 3, 'BC': 3, 'C': 3, 'CD': 2, 'D': 2})
```
