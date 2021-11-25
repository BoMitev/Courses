from .dessert import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name: str):
        grams = Cake.GRAMS
        calories = Cake.CALORIES
        price = Cake.PRICE
        super().__init__(name, price, grams, calories)
