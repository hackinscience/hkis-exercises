Implémentez une fonction affichant tous les nombres pairs dans
l'intervalle demandée, un nombre par ligne.

Votre fonction doit se nommer `print_even_numbers` et accepter deux
paramètres : `start` et `stop`.

Tout comme la fonction
[range](https://docs.python.org/3/library/stdtypes.html#range) de
Python, qui produit des intervalles, votre fonction doit commencer par
chercher des nombres pairs incluant `start` mais excluant `stop`,
rappelez-vous :

```python
for i in range(0, 10):
    print(i)
```

donne :

```
0
1
2
3
4
5
6
7
8
9
```

Je veux que `print_even_numbers(0, 10)` affiche :

```
0
2
4
6
8
```

## Astuces

Vous pouvez utiliser le reste de la division entière par 2 pour savoir
si un nombre est pair ou impair. En Python c'est l'opérateur `%` qu'on
utilise pour obtenir le reste de la division entière :

```pycon
>>> 2 % 2
0
>>> 3 % 2
1
>>> 4 % 2
0
>>> 5 % 2
1
>>> 6 % 2
0
```

Si le reste vaut `1`, le nombre est impair, s'il vaut `0` le nombre est pair.

Vous aurez donc besoin d'un
[if](https://docs.python.org/fr/3/tutorial/controlflow.html#if-statements)
et d'un [print](https://docs.python.org/fr/3/library/functions.html#print).
