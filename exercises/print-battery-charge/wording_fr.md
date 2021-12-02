Rédigez une fonction, nommée `battery_charge`, représentant
graphiquement la charge d'une batterie.

Votre fonction ne doit rien renvoyer (donc renvoyer `None`, c'est ce
que Python renvoie par défaut lorsqu'une fonction n'a pas de
`return`.), elle doit uniquement afficher la barre, et la charge en
pourcent.

La fonction prend un `int` en paramètre, entre `0` et `100` (en Python
on écrirait `in range(101)`).

La fonction affiche une barre, représentant le remplissage de la
batterie, sur une ligne, puis le pourcentage, sur une 2ème ligne.

La barre commence par `[`, se termine par `]`, et contient de 0 à 10
caraceres ❚ pour représenter visuellement le remplissage de la
batterie.


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
