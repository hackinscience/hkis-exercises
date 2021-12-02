Afficher les 10 premiers nombres carrés, un par ligne.

Démarrez à `0`, le premier carré est donc 0<sup>2</sup> (qui vaut
`0`), suivi de 1<sup>2</sup>, 2<sup>2</sup>, etc jusqu'à
9<sup>2</sup>.

Pour rappel, l'opérateur puissance en Python s'écrit `**`, donc :

```pycon
>>> 5 ** 2
25
```

# Conseils

Vous aurez besoin d'un
[for](https://docs.python.org/fr/3/tutorial/controlflow.html#for-statements)
pour parcourir une [intervalle
(`range`)](https://docs.python.org/fr/3/library/functions.html#func-range).

L'instruction `for` est un outil pour parcourir tout ce qui contient
des éléments.

Les chaînes de caractères, les listes, les intervalles (`range`) contiennent des des éléments.

Vous pouvez donc utiliser un `for` pour les parcourir, exemple :

```pycon
>>> for lettre in "Hello":
...     print("La lettre est", c)
...
La lettre est H
La lettre est e
La lettre est l
La lettre est l
La lettre est o
```

Ou :

```pycon
>>> for nombre in [1, 10, 100, 1000]:
...     print(nombre)
...
1
10
100
1000
```

Ou encore :

```pycon
>>> for i in range(10):
...     print(i * 2)
...
0
2
4
6
8
10
12
14
16
18
```
