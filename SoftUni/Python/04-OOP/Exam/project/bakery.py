from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


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

    def add_food(self, food_type, name, price):
        for food in self.food_menu:
            if food.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in self._FOOD_TYPES:
            new_food = self._FOOD_TYPES[food_type](name, price)
            self.food_menu.append(new_food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        for drink in self.drinks_menu:
            if drink.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in self._DRINK_TYPES:
            new_drink = self._DRINK_TYPES[drink_type](name, portion, brand)
            self.drinks_menu.append(new_drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        for table in self.tables_repository:
            if table.table_number == table_type:
                raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in self._TABLE_TYPES:
            new_table = self._TABLE_TYPES[table_type](table_number, capacity)
            self.tables_repository.append(new_table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def _find_table_by_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    @staticmethod
    def _request_food(order_menu, order_names, table: Table, type_food):
        _MENU_TYPES = {
            "food": table.order_food,
            "drink": table.order_drink,
        }

        ordered, unordered = [], []
        menu_names = [f.name for f in order_menu]

        for order_name in order_names:
            if order_name not in menu_names:
                unordered.append(order_name)
                continue
            for order in order_menu:
                if order_name == order.name:
                    _MENU_TYPES[type_food](order)
                    ordered.append(repr(order))

        return ordered, unordered

    def order_food(self, table_number, *food_names):
        table = self._find_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        ordered_food, unordered_food = self._request_food(self.food_menu, food_names, table, "food")
        info = [f"Table {table_number} ordered:"] + ordered_food +\
               [f"{self.name} does not have in the menu:"] + unordered_food

        return '\n'.join(info)

    def order_drink(self, table_number, *drinks_names):
        table = self._find_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        ordered_drinks, unordered_drinks = self._request_food(self.drinks_menu, drinks_names, table, "drink")
        info = [f"Table {table_number} ordered:"] + ordered_drinks +\
               [f"{self.name} does not have in the menu:"] + unordered_drinks

        return '\n'.join(info)

    def leave_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                bill = table.get_bill()
                self.total_income += bill
                table.clear()
                return f"Table: {table.table_number}\n" \
                       f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        info = []
        for table in self.tables_repository:
            if table.free_table_info() is not None:
                info.append(table.free_table_info())

        return '\n'.join(info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
