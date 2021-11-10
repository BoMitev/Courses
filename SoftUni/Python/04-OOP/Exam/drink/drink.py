from abc import ABC


class Drink(ABC):
    def __init__(self, name, portion, price, brand):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or value == " ":
            raise ValueError("Name cannot be empty string or white space!")

        self._name = value

    @property
    def portion(self):
        return self._portion

    @portion.setter
    def portion(self, value):
        if value <= 0:
            raise ValueError("Portion cannot be less than or equal to zero!")

        self._portion = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if value == "" or value == " ":
            raise ValueError("Brand cannot be empty string or white space!")

        self._brand = value

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"
