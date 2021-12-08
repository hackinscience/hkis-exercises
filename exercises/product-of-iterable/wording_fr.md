Rédigez une fonction nommée `mul` prenant un seul argument : un itéralbe.

La fonction doit multiplier entres elles toutes les valeurs de l'argument donné,
et renvoyer le résultat.

`mul([1, 2, 3])` doit donc calculer, et renvoyer, `1 * 2 * 3`.

Il est déconsillé d'utiliser `print` dans ce genre de fonctions,
utilisez `return` pour renvoyer la valeur afin qu'on puisse utiliser le résultat.


On peut donc imaginer l'utiliser comme ça :

```python
print(mul([1, 2, 3]))  # Affiche 6
print(mul([0, 1, 2, 3]))  # Affiche 0 (multiplication par zéro)
print(mul([2, 3, 4]))  # Affiche le résultat de 2 * 3 * 4, soit 24.
print(mul([2, 3, 4]) + mul([1, 2]))  # Affiche le résultat de 2 * 3 * 4 + 1 * 2,  soit 26.
```
