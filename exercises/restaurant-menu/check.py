from correction_helper import exclude_file_from_traceback, fail, student_code, code

exclude_file_from_traceback(__file__)


with student_code():
    from solution import Dish, Menu


menu_to_check = """STARTER
Eggs & Mayonnaise
Salad

DISH
burger
pizza
Coq au vin

DESSERT
Chocolate Cookie
Waffles"""


def check():
    with student_code(prefix="While creating `Menu` objects"):
        menu_monday = Menu("Monday")
        menu_tuesday = Menu("Tuesday")

    with student_code(prefix="While creating `Dish` objects"):
        pizza = Dish("pizza", 30, "dish")
        burger = Dish("burger", 15, "dish")

    with student_code(prefix="While adding dishes to menus"):
        menu_monday.add_dish(pizza)
        menu_tuesday.add_dish(burger)

        menu_monday.add_dish(Dish("Eggs & Mayonnaise", 5, "starter"))
        menu_monday.add_dish(Dish("Salad", 10, "starter"))
        menu_monday.add_dish(Dish("Waffles", 10, "dessert"))

        menu_tuesday.add_dish(Dish("Coq au vin", 60, "dish"))
        menu_tuesday.add_dish(Dish("Chocolate Cookie", 8, "dessert"))

    with student_code(prefix="While we are comparing `Dish` objects with operator"):
        pizza_lt_burger = pizza < burger
        burger_lt_pizza = burger < pizza

        pizza_eq_pizza = pizza == Dish("another pizza", 30, "dish")

        pizza_gt_burger = pizza > burger
        burger_gt_pizza = burger > pizza

    if pizza_lt_burger or not (burger_lt_pizza):
        fail(
            "If I create 2 Dish objects with differents `preparation_time` "
            "and compare them with `<` operator, I haven't the expected results"
        )

    if not (pizza_eq_pizza):
        fail(
            "If I create 2 Dish objects with same `preparation_time` "
            "and compare them with `==` operator, I'm getting `False`."
            "I expected `True`.",
        )

    if not (pizza_gt_burger) or burger_gt_pizza:
        fail(
            "If I create 2 Dish objects with differents `preparation_time` "
            "and compare them with `>` operator, I haven't the expected results"
        )

    with student_code(prefix="While getting all the starters on a `Menu` object"):
        monday_starters = menu_monday.get_starters()
        dishes_types = set([dish.dish_type for dish in monday_starters])

    if (
        len(monday_starters) != 2
        or len(dishes_types) != 1
        or list(dishes_types)[0] != "starter"
    ):
        fail(
            "If I create a menu with multiple dishes, starters and desserts, "
            "and try to get only the starters, I don't get the expected values.",
            "I get {dishes_len!r} dishes and {dtype!r} dishes types\n".format(
                dishes_len=len(monday_starters), dtype=len(dishes_types)
            ),
            "But I wanted 1 dish and 1 dish_type",
        )

    with student_code(prefix="While getting all the dishes on a `Menu` object"):
        monday_dishes = menu_monday.get_dishes()
        dishes_types = set([dish.dish_type for dish in monday_dishes])

    if (
        len(monday_dishes) != 1
        or len(dishes_types) != 1
        or list(dishes_types)[0] != "dish"
    ):
        fail(
            "If I create a menu with multiple dishes, starters and desserts, "
            "and try to get only the dishes, I don't get the expected values.",
            "I get {dishes_len!r} dishes for {dtype!r} dishes types\n".format(
                dishes_len=len(monday_dishes), dtype=len(dishes_types)
            ),
            "But I wanted 1 dish and 1 dish_type",
        )

    with student_code(prefix="While getting all the desserts on a `Menu` object"):
        monday_desserts = menu_monday.get_desserts()
        dishes_types = set([dish.dish_type for dish in monday_desserts])

    if (
        len(monday_desserts) != 1
        or len(dishes_types) != 1
        or list(dishes_types)[0] != "dessert"
    ):
        fail(
            "If I create a menu with multiple dishes, starters and desserts, "
            "and try to get only the desserts, I don't get the expected values.",
            "I get {dishes_len!r} dishes and {dtype!r} dishes types\n".format(
                dishes_len=len(monday_desserts), dtype=len(dishes_types)
            ),
            "But I wanted 1 dish and 1 dish_type",
        )

    with student_code(
        prefix="While getting the minimum preparation time of multiple `Menu` objects"
    ):
        menu_monday_mini = menu_monday.get_minimum_preparation_time()
        menu_tuesday_mini = menu_tuesday.get_minimum_preparation_time()

    if menu_monday_mini != 45:
        fail(
            "If I create a menu with multiple starter Dish and call "
            "`get_minimum_preparation_time`, I don't get the expected result.",
            "I expected to get `45` back, but you gave `{mini_time!r}`".format(
                mini_time=menu_monday_mini
            ),
        )

    if menu_tuesday_mini != 23:
        fail(
            "If I create a menu with no starter Dish and call "
            "`get_minimum_preparation_time`, I don't get the expected result.",
            "I expected to get `23` back, but you gave `{mini_time!r}`".format(
                mini_time=menu_tuesday_mini
            ),
        )

    with student_code(
        prefix="While getting the maximum preparation time of multiple `Menu` objects"
    ):
        menu_monday_maxi = menu_monday.get_maximum_preparation_time()
        menu_tuesday_maxi = menu_tuesday.get_maximum_preparation_time()

    if menu_monday_maxi != 50:
        fail(
            "If I create a menu with multiple starter Dish and call "
            "`get_maximum_preparation_time`, I don't get the expected result.",
            "I expected to get `50` back, but you gave `{maxi_time!r}`".format(
                maxi_time=menu_monday_maxi
            ),
        )

    if menu_tuesday_maxi != 68:
        fail(
            "If I create a menu with no starter Dish and call "
            "`get_maximum_preparation_time`, I don't get the expected result.",
            "I expected to get `68` back, but you gave `{maxi_time!r}`".format(
                maxi_time=menu_tuesday_maxi
            ),
        )

    with student_code(prefix="While adding 2 `Menu` items with `+` operator"):
        menu_montue = menu_monday + menu_tuesday

    if (
        sorted(menu_montue.get_starters())
        != sorted(menu_monday.get_starters() + menu_tuesday.get_starters())
        or sorted(menu_montue.get_dishes())
        != sorted(menu_monday.get_dishes() + menu_tuesday.get_dishes())
        or sorted(menu_montue.get_desserts())
        != sorted(menu_monday.get_desserts() + menu_tuesday.get_desserts())
    ):
        fail(
            "If I add 2 `Menu` items with the `+` operator, "
            "I don't have all the `Dish` of the 2 `Menu`s"
        )

    if menu_montue.name != "Monday & Tuesday":
        fail(
            "If I add 2 `Menu` items with the `+` operator, "
            "I don't have the wanted name.",
            "I expected to get `Monday & Tuesday`, but it's `{name!r}`".format(
                name=menu_montue.name
            ),
        )

    with student_code(prefix="While printing `Menu` item"):
        menu_output = str(menu_montue)

    if menu_output != menu_to_check:
        fail(
            "If I print a `Menu` item, I don't get the expected output.",
            "I expected the following output:",
            code(menu_to_check),
            "But you gave:",
            code(menu_output),
        )


if __name__ == "__main__":
    check()
