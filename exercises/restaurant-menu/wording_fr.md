Implementez les classes `Dish` et `Menu` comme suit :

- Dish a les attributs  `name`, `preparation_time` et `dish_type`, donnés dans cet ordre au moment de l'initialisation.
- La valeur de l'attribut `dish_type` dans la classe Dish peut être l'une des suivantes :
    - starter
    - dish
    - dessert


- Menu a l'attribut `name`, donné au moment de l'initialisation.
- Menu a la méthode `add_dish(dish)`.
- Lorsque que vous comparez 2 objets `Dish` avec les opérateurs `>`, `<`, `==`, `<=`, `>=`, celà doit comparer leurs attributs `preparation_time`.
- Menu a une méthode `get_starters()` donnant tous les Dish ayant un `dish_type` ayant pour valeur "starter".
- Menu a une méthode `get_dishes()` donnant tous les Dish ayant un `dish_type` ayant pour valeur "dish".
- Menu a une méthode `get_desserts()` donnant tous les Dish ayant un `dish_type` ayant pour valeur "dessert".

- Menu a la méthode `get_minimum_preparation_time()` renvoyant la somme de :
    - la plus petite valeur `preparation_time` de tous les Dish présents dans le Menu avec l'attribut `dish_type` ayant pour valeur "starter" `dish_type` (0 s'il n'y a aucune `dish_type` starter)
    - la plus petite valeur `preparation_time` de tous les Dish présents dans le Menu avec l'attribut `dish_type` ayant pour valeur "dish" `dish_type` (0 s'il n'y a aucune `dish_type` dish)
    - la plus petite valeur `preparation_time` de tous les Dish présents dans le Menu avec l'attribut `dish_type` ayant pour valeur "dessert" `dish_type` (0 s'il n'y a aucune `dish_type` dessert)


- Menu a une méthode `get_maximum_preparation_time()` renvoyant la somme de :
    - la plus grande valeur `preparation_time` de tous les Dish présents dans le Menu avec l'attribut `dish_type` ayant pour valeur "starter" `dish_type` (0 s'il n'y a aucune `dish_type` starter)
    - la plus grande valeur `preparation_time` de tous les Dish présents dans le Menu avec l'attribut `dish_type` ayant pour valeur "dish" `dish_type` (0 s'il n'y a aucune `dish_type` dish)
    - la plus grande valeur `preparation_time` de tous les Dish présents dans le Menu avec l'attribut `dish_type` ayant pour valeur "dessert" `dish_type` (0 s'il n'y a aucune `dish_type` dessert)

- Lorsque vous additionnez 2 objets `Menu` avec l'opérateur `+`, cela retourne un troisième menu contenant tous les Dish des 2 objets 2 Menu et ayant l'attribut `name` étant les 2 `name` des Menu `name` séparés par " & ".

  eg :

```python
>>> menu_1 = Menu("One")
>>> menu_2 = Menu("Two")
>>> menu_3 = menu_1 + menu_2
>>> print(menu_3.name)
One & Two
```



- Lorsque vous utilisez la fonction print() sur un objet `Menu` cela doit :

    - Afficher le `name` de chaque Dish, 1 par ligne, triés par `dish_type` (starter, dish, dessert) et leur `preparation_time` (du plus petit au plus grand)
    - Séparer chaque nouveau `dish_type` par une ligne vide
    - Ajouter le `dish_type`, tout en majuscule, avant tous les Dish ayant le-dit `dish_type`



Voici ce à quoi cela doit ressembler :

```python
>>> print(my_menu)
STARTER
eggs & mayonaise
salad

DISH
burger
pizza
coq au vin

DESSERT
chocolate cookie
waffle
```
