Jouons un peu…

## Les règles

Ce jeu se joue avec des carrés, qu'on appelera des carrés de Dirichlet.

Ils ne respectent qu'une, et une seule règle :

> Chaque case contient la moyenne des 4 cases qui l'entourrent.

Par exemple :

```text
  8
4 6 9
  3
```

On a : `(3 + 4 + 8 + 9) / 4 == 6`.

Maintenant qu'on a la règle, regardons un carré de 3×3 :

```text
  2 5 8
0 2 4 6 9
0 2 3 3 0
0 3 3 3 0
  7 3 6
```

(Oui, j'ai ajouté des nombres *autour* du carré, de manière à pouvoir
valider la règle sur chaque case du carré de 3 par 3.)

Les cellules ne peuvent contenir que des entiers positifs (`0`
inclu). Les valeurs doivent être exactes, pas d'arrondi.


## Le jeu

OK pour les règles, mais quel est le jeu ?

Le jeu consiste à remplir un carré troué, comme au Sudoku :


```text
  7 9 9
0       9
9       8
0       4
  6 0 9
```

(Je vous donnerai toujours la bordure, et jamais l'inteieur, comme cet exemple.)


## L'exercice

Vous devez écrire la fonction `dirichlet_square_solver`, elle prend un
seul argument, un `numpy array`.

Votre fonction doit **modifier** l'`array` sur place, en remplissant
les blancs (contenant en fait `-1`), et ne rien renvoyer.

Si on reprend le dernier exemple, voilà ce que ça donnerait :

```python
import numpy as np

square = np.array(
    [[0,  7,  9,  9, 0],
     [0, -1, -1, -1, 9],
     [9, -1, -1, -1, 8],
     [0, -1, -1, -1, 4],
     [0,  6,  0,  9, 0]],
    dtype=int)
dirichlet_square_solver(square)
print(square)
# Should give:
# [[0 7 9 9 0]
#  [0 5 7 8 9]
#  [9 6 6 7 8]
#  [0 4 4 6 4]
#  [0 6 0 9 0]]
```

## Bonus

À faire sur votre ordinateur, une fois que vous avez le solveur :

Créez un gros numpy array, disons 2000×6000, gardez toutes les valeurs à 0 sauf quelques "points chauds" autour.

Faites-le résoudre par votre solveur.

Affichez le résultat en utilisant
[matplotlib.imshow](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.imshow.html),
et en choisissant une palette allant des couleurs froides vers les
couleurs chaudes.

Le résultat doit vous faire penser à une plaque de métal qu'on aurait
chauffé, le résultat représentant la propagation de la chaleur dans la
plaque de métal, chez moi, en « chauffant » des parties du haut d'une
grille de 600×800 ça ressemble [à ça](https://mdk.fr/dirichlet.png).
