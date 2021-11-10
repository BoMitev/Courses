from project.baked_food.cake import Cake
from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:
    __TYPE_OF_FOODS = {
        "Bread": Bread,
        "Cake": Cake,
    }
    __TYPE_OF_DRINKS = {
        "Tea": Tea,
        "Water": Water,
    }
    __TYPE_OF_TABLE = {
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
        return self._name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Name cannot be empty string or white space!")

        self._name = value

    def add_food(self, food_type, name, price):
        if name in [f.name for f in self.food_menu]:
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in self.__TYPE_OF_FOODS:
            food = self.__TYPE_OF_FOODS[food_type](name, price)
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        if name in [d.name for d in self.drinks_menu]:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in self.__TYPE_OF_DRINKS:
            drink = self.__TYPE_OF_DRINKS[drink_type](name, portion, brand)
            self.drinks_menu.append(drink)
            return f"Added {name} ({drink_type}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        if table_number in [t.table_number for t in self.tables_repository]:
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in self.__TYPE_OF_TABLE:
            table = self.__TYPE_OF_TABLE[table_type](table_number, capacity)
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def _available_table(self, number_of_people):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                return table

        return None

    def reserve_table(self, number_of_people):
        for table in self.tables_repository:
            return table.reserve(number_of_people)

    def _table_from_table_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

        return False

    def _table_order(self, table_number, products_names, products_menu):
        table = self._table_from_table_number(table_number)
        if not table:
            return f"Could not find table {table_number}"

        ordered = [f'Table {table_number} ordered:']
        unordered = [f'{self.name} does not have in the menu:']

        for product in products_names:
            for p in products_menu:
                if p.name == product:
                    ordered.append(repr(p))
                else:
                    unordered.append(p.name)

        info = ordered + unordered
        return '\n'.join(info)

    def order_food(self, table_number, *food_names):
        return self._table_order(table_number, *food_names, self.food_menu)

    def order_drink(self, table_number, *drink_names):
        return self._table_order(table_number, *drink_names, self.drinks_menu)

    def leave_table(self, table_number):
        table = self._table_from_table_number(table_number)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f"Table: {table_number}\n" \
               f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        info = []
        for table in self.tables_repository:
            if not table.is_reserved:
                info.append(table.free_table_info())

        return '\n'.join(info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"