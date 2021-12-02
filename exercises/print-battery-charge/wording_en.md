Write a function named `battery_charge` that graphically represents
a battery’s charge. Your function doesn't need to return anything,
but just show how much a battery is charged.

This function will takes an `int` between `0` and `100` (in Python
words `in range(101)`) as a parameter, display a bar to represent how
much the battery is "filled" (from `0` to `10` bars), then prints the
percentage.


## Examples

```
>>> for i in range(20):
...    battery_charge(i)
...    print()  # Just to add a newline between them
...
[          ]
0%

[          ]
1%

[          ]
2%

[          ]
3%

[          ]
4%

[          ]
5%

[❚         ]
6%

[❚         ]
7%

[❚         ]
8%

[❚         ]
9%

[❚         ]
10%

[❚         ]
11%

[❚         ]
12%

[❚         ]
13%

[❚         ]
14%

[❚❚        ]
15%

[❚❚        ]
16%

[❚❚        ]
17%

[❚❚        ]
18%

[❚❚        ]
19%
```

If the ❚ character causes you problems in your editor or terminal, feel free to
use a simple | instead.


## References

- The [round](https://docs.python.org/3/library/functions.html#round) builtin function.
