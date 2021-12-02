Rédigez une fonction nommée `how_to_pay` et acceptant deux
paramètres : `amount` et `currency`.

- `amount` est un montant à payer.
- `currency` décrit une monnaie par une liste de pièces et de billets existants.

La fonction doit renvoyer un dictionnaire indiquant comment payer le
montant donné avec le minimum de pièces et de billets de la monnaie
donnée.


Par exemple, pour payer `3` dans une monnaie composée des pièces `[1,
2, 5]` vous devez utiliser une pièce de `2` et une pièce de `1`, votre
fonction doit donc renvoyer `{2: 1, 1: 1}`.


## Exemple d'utilisation

```pycon
>>> euro = [1, 2, 5, 10, 20, 50, 100, 200, 500]
>>> how_to_pay(500, euro)
{500: 1}  # means: To pay 500€: give one bill of 500€
>>> how_to_pay(10, euro)
{10: 1}  # means: To pay 10€: give one bill of 10€
>>> how_to_pay(123, euro)    # To pay 123 euros:
{100: 1, 20: 1, 2: 1, 1: 1}  # give 1 bill of 100€, one bill of 20€,
                             # one coin of 2€, and one coin of 1€.
```

## Astuce

C'est acceptable de donner dans le dictionnaire renvoyé les pièces et
billets ne devant pas être utilisés, en indiquant explicitement
`0`. Mais ce n'est pas obligatoire.

Donc les deux solutions suivantes sont values :

```python
>>> how_to_pay(1, [1, 5])
{1: 1, 5: 0}
>>> how_to_pay(1, [1, 5])
{1: 1}
```
