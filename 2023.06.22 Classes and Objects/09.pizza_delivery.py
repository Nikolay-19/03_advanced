class PizzaDelivery:
    def __init__(self, name, price, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient, quantity, price_per_qt):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        elif ingredient in self.ingredients.keys():
            self.ingredients[ingredient] += quantity
            self.price += quantity * price_per_qt
        else:
            self.ingredients[ingredient] = quantity
            self.price += quantity * price_per_qt

    def remove_ingredient(self, ingredient, quantity, price_per_qt):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        elif ingredient not in self.ingredients.keys():
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        elif ingredient in self.ingredients.keys() and quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"
        else:
            self.ingredients[ingredient] -= quantity
            self.price -= quantity * price_per_qt

    def make_order(self):
        self.ordered = True
        list1 = []
        for key, value in self.ingredients.items():
            list1.append(f"{key}: {value}")
        return f"You've ordered pizza {self.name} prepared with {', '.join(str(el) for el in list1)} and the price will be {self.price}lv."

