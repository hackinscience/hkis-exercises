Rédigez une classe permettant de convertir des Fahrenheit, Celsius, et Kelvins.

Vous devrez utiliser des
[descripteurs](https://docs.python.org/fr/3/howto/descriptor.html),
prenez bien le temps de lire la documentation.

Votre classe doit être nomée `Temperature`, elle représente une
température, peu importe l'unité de mesure.

(Cependant je ne testerai que Fahrenheit, Celsius, et Kelvins, vous
pouvez en ajouter si vous voulez.)


À l'utilisation, voilà à quoi ça doit ressembler :

```python
>>> t1 = Temperature()
>>> t1.kelvin = 0
>>> t1.celsius
-273.15
>>> t1.fahrenheit
-459.67
```

Votre classe doit accepter des modifications de sa valeur depuis
n'importe lequel des trois attributs, et doit donner les bonnes
valeurs lorsqu'on accède à n'importe lequel des trois attributs :

```python
>>> t0 = Temperature()
>>> t0.celsius = 50
>>> t0.kelvin
323.15
>>> t0.celsius += 1
>>> t0.kelvin
324.15
>>> t0.kelvin -= 1
>>> t0.kelvin
323.15
```

Vous trouverez des tableaux de conversion sur [Wikipedia](https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature).


# Astuces

Ne stockez qu'une seule valeur de référence dans votre classe : elle
n'aura ainsi qu'une source de vérité.
