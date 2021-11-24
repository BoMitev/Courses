from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    _FOOD_TYPES = {
        "Bread": Bread,
        "Cake": Cake,
    }
    _DRINK_TYPES = {
        "Tea": Tea,
        "Water": Water,
    }
    _TABLE_TYPES = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable,
    }

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    @staticmethod
    def find_by_name(name, order_menu):
        for order in order_menu:
            if order.name == name:
                return order

        return False

    def find_table_by_num(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

        return False

    def find_free_table(self, people_count):
        for table in self.tables_repository:
            if table.capacity >= people_count and not table.is_reserved:
                return table

        return False

    def add_food(self, food_type, name, price):
        if self.find_by_name(name, self.food_menu):
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in self._FOOD_TYPES:
            food = self._FOOD_TYPES[food_type](name, price)
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        if self.find_by_name(name, self.drinks_menu):
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in self._DRINK_TYPES:
            drink = self._DRINK_TYPES[drink_type](name, portion, brand)
            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        if self.find_table_by_num(table_number):
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in self._TABLE_TYPES:
            table = self._TABLE_TYPES[table_type](table_number, capacity)
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        table = self.find_free_table(number_of_people)
        if not table:
            return f"No available table for {number_of_people} people"

        table.reserve(number_of_people)
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number, *foods):
        table = self.find_table_by_num(table_number)
        if not table:
            return f"Could not find table {table_number}"

        ordered_food, unordered_food = [], []
        for food_name in foods:
            food = self.find_by_name(food_name, self.food_menu)
            if food:
                ordered_food.append(repr(food))
                table.order_food(food)
            else:
                unordered_food.append(food_name)

        info = [f"Table {table_number} ordered:"]
        info.extend(ordered_food)
        info.append(f"{self.name} does not have in the menu:")
        info.extend(unordered_food)

        return '\n'.join(info)

    def order_drink(self, table_number, *drinks):
        table = self.find_table_by_num(table_number)
        if not table:
            return f"Could not find table {table_number}"

        ordered_drinks, unordered_drinks = [], []
        for drink_name in drinks:
            drink = self.find_by_name(drink_name, self.drinks_menu)
            if drink:
                ordered_drinks.append(repr(drink))
                table.order_drink(drink)
            else:
                unordered_drinks.append(drink_name)

        info = [f"Table {table_number} ordered:"]
        info.extend(ordered_drinks)
        info.append(f"{self.name} does not have in the menu:")
        info.extend(unordered_drinks)

        return '\n'.join(info)

    def leave_table(self, table_number):
        table = self.find_table_by_num(table_number)
        if table:
            bill = table.get_bill()
            self.total_income += bill
            table.clear()

            return f"Table: {table_number}\n" \
                   f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        info = []
        for table in self.tables_repository:
            if table.free_table_info():
                info.append(table.free_table_info())

        return '\n'.join(info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}"