Implement a `Dish` and a `Menu` classes like so:

- Dish have a `name`, `preparation_time`, and a `dish_type` attribute , given in this order at initialization time.
- Dish's `dish_type` attribute value can be :
  - starter
  - dish
  - dessert

- Menu have a `name` attribute, given at initialization time.
- Menu have an `add_dish(dish)` method.
- When you compare 2 `Dish` items with the operators `>`, `<`, `==`, `<=`, `>=`, it must compare its `preparation_time`.
- Menu have a `get_starters()` method giving all the Dish with "starter" `dish_type`
- Menu have a `get_dishes()` method giving all the Dish with "dish" `dish_type`
- Menu have a `get_desserts()` method giving all the Dish with "dessert" `dish_type`

- Menu have a `get_minimum_preparation_time()` method giving the sum of :
   - the lowest `preparation_time` from Dish with "starter" `dish_type` on the Menu (0 if there is no starter)
   - the lowest `preparation_time` from Dish with "dish" `dish_type` on the Menu (0 if there is no dish)
   - the lowest `preparation_time` from Dish with "dessert" `dish_type` on the Menu (0 if there is no dessert)

- Menu have a `get_maximum_preparation_time()` method giving the sum of :
   - the highest `preparation_time` from Dish with "starter" `dish_type` on the Menu (0 if there is no starter)
   - the highest `preparation_time` from Dish with "dish" `dish_type` on the Menu (0 if there is no dish)
   - the highest `preparation_time` from Dish with "dessert" `dish_type` on the Menu (0 if there is no dessert)

- When you add 2 `Menu` items with the `+` operator, it will return a third Menu containing the Dish of the 2 Menu and with `name` being the 2 Menu `name` separated by " & ".

  eg :

```python
>>> menu_1 = Menu("One")
>>> menu_2 = Menu("Two")
>>> menu_3 = menu_1 + menu_2
>>> print(menu_3.name)
One & Two
```

  

- When you print a `Menu` item it must :

  - Print all the Dish's `name` 1 per line sorted by `dish_type` (starter, dish, dessert) and `preparation_time` (lowest to highest)
  - Separate every `dish_type` by an empty line
  - Adding the `dish_type` all in uppercase before all the Dish with the given `dish_type`



Here is what it should look like :

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
