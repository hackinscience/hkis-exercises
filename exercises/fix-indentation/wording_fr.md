Il y a un bug dans le code fourni : l'indentation est absente.

Votre but ? Le corriger (en ajoutant simplement quatre espaces au bon endroit).

Le code doit afficher :

```text
Gonna knock three times:
*knock*
*knock*
*knock*
- Who's there?
```


## Qu'est-ce que l'indentation ?

Vous-vous êtes peut-être posés la question en lisant le code, après le `for` :

> Comment Python define ce qui doit être répété ?

Python ne « devine » pas, c'est à vous de l'indiquer, en ajoutant
quatre espaces en début de ligne.

Chaque ligne indentée (préfixée d'espaces) fait ainsi partie de la « suite » du `for`, et les lignes qui ne le sont pas n'en font pas partie.

Exemple :

```python
for i in range(5):
    print("Bonjour")
```

affiche :

```text
Bonjour
Bonjour
Bonjour
Bonjour
Bonjour
```
