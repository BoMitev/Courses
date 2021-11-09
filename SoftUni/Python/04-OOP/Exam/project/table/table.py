from abc import ABC
from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self._is_reversed = False

    def reserve(self, number_of_people):
        self.number_of_people = number_of_people
        self._is_reversed = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        bill = 0
        for item in self.food_orders:
            bill += item.price

        for drink in self.drink_orders:
            bill += drink.price

        return bill

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self._is_reversed = False

    def free_table_info(self):
        if not self._is_reversed:
            return f"Table: {self.table_number}\n" \
                   f"Type: {type(self).__name__}\n" \
                   f"Capacity: {self.capacity}"
