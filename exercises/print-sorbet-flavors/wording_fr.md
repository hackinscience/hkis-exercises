Vous travaillez pour un restaurant, et on vous demande de générer le menu des sorbets...

Fournissez un script qui affiche tous les sorbets de deux boules
possibles (la liste des parfums vous est fournie).

Ne proposez pas deux boules du même parfum (pas de "Chocolate
Chocolate"), et attention, si vous avez affiché "Chocolate Banana",
n'affichez pas "Banana Chocolate" plus loin.

Les goûts proposés sont :

```python
FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]
```

Affichez une paire par ligne, en séparant les parfums par des
virgules, ce qui doit ressemble à :

```text
Banana, Chocolate
Banana, Lemon
Banana, Pistachio
Banana, Raspberry
Banana, Strawberry
Banana, Vanilla
Chocolate, Lemon
…
```
