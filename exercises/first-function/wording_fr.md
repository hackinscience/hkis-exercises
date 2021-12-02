Rédigez une fonction calculant le périmètre d'un cercle de rayon donné.

Lisez tout d'abord le [tutoriel sur les
fonctions](https://docs.python.org/fr/3/tutorial/controlflow.html#defining-functions).

Votre fonction doit être nommée `circle_perimeter`, et accepter le
paramètre `radius`, c'est ce paramètre qui recevra le rayon du cercle.

Votre fonction doit renvoyer le périmètre d'un cercle du rayon donné.

Pour tester votre fonction, je vais l'importer et essayer différentes
valeurs, un peu comme :

```python
>>> circle_perimeter(1)
6.283185307179586
>>> circle_perimeter(10)
62.83185307179586
>>> circle_perimeter(100)
628.3185307179587
```

## Les fonctions

Par exemple, voici la plus simple des fonctions, elle accepte une
valeur, qu'elle renvoie directement, sans la modifier :

```python
def identité(x):
    return x
```

On peut appeler notre fonction `identité` et vérifier qu'elle renvoie
bien la valeur qu'on lui a donné :

```python
>>> identité(42) == 42
True
```

Ainsi, comparons :

```pycon
>>> print(42)
42
```

et :

```pycon
>>> print(identité(42))
42
```

Les deux se comportent exactement pareil, dans le premier exemple on
donne `42` à `print` qui affiche « 42 », dans le second on donne `42`
à `identité`, qui renvoie `42`, qu'on donne directement à `print`, qui
reçoit donc `42`, et l'affiche aussi.

On pourrait aussi comparer :

```pycon
>>> quarante_deux = 42
>>> print(quarante_deux)
```

et :

```pycon
>>> quarante_deux = identité(42)
>>> print(quarante_deux)
```

ou encore :

```pycon
>>> quarante_deux = 42
>>> quarante_deux = identité(quarante_deux)
>>> print(quarante_deux)
```

qui font aussi, tous, exactement la même chose.


## Astuces

- N'utilisez pas `print` dans votre fonction, elle doit simplement [renvoyer le résultat](https://docs.python.org/fr/3/tutorial/controlflow.html#defining-functions).
- Vous aurez besoin d'[importer](https://docs.python.org/fr/3/tutorial/modules.html#standard-modules) le module [math](https://docs.python.org/fr/3/library/math.html).
- Vous trouverez PI dans le module math : [math.pi](https://docs.python.org/fr/3/library/math.html#math.pi) (vous pouvez aussi utiliser [math.tau](https://docs.python.org/fr/3/library/math.html#math.tau)).
