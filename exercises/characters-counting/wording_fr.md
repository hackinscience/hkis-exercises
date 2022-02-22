Affichez le nombre de caractères du paragraphe suivant :

```text
Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.
```

J'ai pré-rempli la zone de code avec le paragraphe, sous forme d'une chaîne
de caractères (entre guillemets), que j'ai nommé `whetting_your_appetite` (c'est ce qu'on appelle « une variable »).


## Conseils

Vous aurez besoin de la fonction
[`len`](https://docs.python.org/fr/3/library/functions.html#len),
qui peut mesurer quasiment n'importe quoi : des listes, des chaînes de caractères, …

Si vous êtes bloqués, vous pouvez relire le
[tutoriel sur les chaînes de caractères](https://docs.python.org/fr/3/tutorial/introduction.html#strings).

Vous n'avez pas besoin de toucher aux 12 premières lignes, codez
simplement sous le commentaire `# Enter your code below:`.

N'oubliez pas d'utiliser la fonction
[print](https://docs.python.org/fr/3/library/functions.html#print)
pour afficher le résultat !


## Qu'est-ce qu'une fonction ?

Une fonction est quelque chose de nommé, qui prend une (ou plusieurs)
valeurs, fait quelque chose avec, et renvoie un résultat.

Par exemple, la fonction nommée `max` prend plusieurs valeurs, et
renvoie la plus grande de ces valeurs.

La syntaxe pour lui donner les différentes valeurs est :

```python
max(1, 5, 2)
```

Et, dans ce cas, elle renvoie `5`.

Ce qui est renvoyé par la fonction peut être utilisé :

- En nommant cette valeur (ce qu'on appelle une variable).
- En passant la valeur directeur à une autre fonction.

Typiquement, si vous voulez afficher le `5` de l'exemple précédent, vous
pouvez soit faire :

```python
le_plus_grand = max(1, 5, 2)
print(le_plus_grand)
```

soit:

```python
print(max(1, 5, 2))
```
