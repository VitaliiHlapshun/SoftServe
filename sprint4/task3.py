class Pizza:
    order_number = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients

        Pizza.order_number += 1
    @classmethod
    def hawaiian(cls):
        ingredients = ["ham", "pineapple"]
        return cls(ingredients)

    @classmethod
    def meat_festival(cls):
        ingredients = ["beef", "meatball", "bacon"]
        return cls(ingredients)

    @classmethod
    def garden_feast(cls):
        ingredients = ["spinach", "olives", "mushroom"]
        return cls(ingredients)

p1 = Pizza(["bacon", "parmesan", "ham"])
p2 = Pizza.hawaiian()

print(p1.ingredients)
print(p1.order_number)
print(p2.ingredients)
