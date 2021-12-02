## Description

!!! warning
    Il est intéressant de tester cet exercice sur votre machine.

    La documentation d'installation et d'utilisation de Python est traduite en français :
    [https://docs.python.org/fr/3/using/index.html](https://docs.python.org/fr/3/using/index.html).

Ceci est une très courte introduction au module
[`requests`](http://www.python-requests.org/en/latest/), module qui
permet de récupérer du contenu depuis internet assez facilement.

`requests` ne fait _PAS_ partie de la bibliothèque standard de Python,
mais est installé sur HackInScience.

Vous pouvez l'installer sur votre machine via : `python3 -m pip install requests`.

Pour résoudre cet exercice, vous devez effectuer une requête
[`GET`](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods)
sur la page `https://api.github.com/users/python`, puis afficher le résultat.

Dans le cas où votre ordinateur n'est pas connecté à internet, le
programme devra afficher `No internet connectivity` sur la sortie
standard.

Attention !! `requests` lève une exception en cas de perte de
connexion, et je vais tester ce cas !

## Références

- Requests: <https://requests.readthedocs.io>


## Exemple

```ipython
$ python solution.py
{
  "login": "python",
  "id": 1525981,
  ...
```

On coupe sa connexion Wi-Fi, on retente :

```ipython
$ python solution.py
No internet connectivity.
```
