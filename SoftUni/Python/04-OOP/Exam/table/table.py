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
        self.is_reserved = False

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")

        self._capacity = value

    def reserve(self, number_of_people):
        if not self.is_reserved and number_of_people <= self.capacity:
            self.number_of_people = number_of_people
            self.is_reserved = True
            return f"Table {self.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        products = self.drink_orders + self.food_orders
        return sum(p.price for p in products)

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\n" \
                   f"Type: {self.__class__.__name__}\n" \
                   f"Capacity: {self.capacity}"

        return None
