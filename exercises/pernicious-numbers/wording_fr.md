Rédigez un programme ne prenant aucun paramètres.

Ce programme doit afficher les [nombres pernicieux
(en)](https://en.wikipedia.org/wiki/Pernicious_number) dans
l'intervalle `range(222281, 222381)`

Cet exercice peut être compliqué si vous ne comprennez pas
parfaitement ce qu'est un `nombre pernicieux`, et puisqu'aucun
exercice n'est obligatoire pour passer à la suite, sentez-vous libre
de le sauter.

Affichez un et un seul nombre par ligne, rien d'autre.

Si le but de l'exercice était d'afficher les nombres pernicieux de
l'intervalle `range(100, 110)`, on verrait :

```
$ ./solution.py
100
103
104
107
109
```

Parce que :

 - 100 vaut 1100100 en base 2, qui est composé d'un nombre premier de uns (3).
 - 103 vaut 1100111 en base 2, qui est composé d'un nombre premier de uns (5).
 - 104 vaut 1101000 en base 2, qui est composé d'un nombre premier de uns (3).
 - 107 vaut 1101011 en base 2, qui est composé d'un nombre premier de uns (5).
 - 109 vaut 1101101 en base 2, qui est composé d'un nombre premier de uns (5).
