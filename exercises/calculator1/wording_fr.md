Rédigez un programme se comportant comme un calculatrice élémentaire.

!!! warning
    You should work on this exercise with your own installation of Python,
    on your computer. Learn how for
    [Mac OSX](https://framagit.org/hackinscience/hkis-website/wikis/How-to-work-on-an-exercise-from-Mac-OSX)
    or [Windows](https://framagit.org/hackinscience/hkis-website/wikis/How-to-work-on-an-exercise-from-Windows).

Votre calculatrice devra gérer les opérateurs suivants : `+`, `-` ,
`*`, `/`, `%` (modulo) et `^` (exponentiation).  Les paramètres seront
toujours des nombres entiers.

Dans le cas où votre programme reçoit moins de trois paramètres, il
doit afficher un message d'aide.

Pour toute autre erreur, votre programme doit afficher `input error`.

## Examples

```bash
oa@localhost$ ./solution.py 1 + 1
2
oa@localhost$ ./solution.py
usage: ./solution.py a_number (an_operator +-*/%^) a_number
oa@localhost$ ./solution.py 1 / 0
input error
oa@localhost$
```

## Conseils

Sur les shells **Mac** et **Linux**, vous devrez protéger les
astérisques en les préfixant par des antislash, exemples :

```bash
mbp|110-$ python solution.py 3 / 5
0.6
mbp|110-$ python solution.py 3 + 5
8
mbp|110-$ python solution.py 3 - 5
-2
mbp|110-$ python solution.py 3 * 5  # Ici l'étoile est remplacée par le shell, votre programme ne comprend pas.
usage: python3 ./solution.py a_number (an_operator +-*/%^) a_number
mbp|110-$ python solution.py 3 \* 5
15
```

De même, sur **Windows** dans `cmd.exe`, `^` doit être mis entre guillemets : `"^"`.
