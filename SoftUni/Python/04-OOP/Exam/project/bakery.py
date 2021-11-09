from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water

class Bakery:
    __TYPE_OF_FOODS = {
        "Bread": Bread,
        "Cake": Cake,
    }
    __TYPE_OF_DRINKS = {
        "Tea": Tea,
        "Water": Water,
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
        if not value or value == " ":
            raise "Name cannot be empty string or white space!"

        self.__name = value

    def add_food(self, food_type, name, price):
        food = Bakery.__TYPE_OF_FOODS[food_type](name, price)
        if food in self.food_menu:
            raise Exception(f"{food_type} {name} is already in the menu!")

        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        drink = Bakery.__TYPE_OF_DRINKS[drink_type](name, portion, brand)
        if drink in self.drinks_menu:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        self.drinks_menu.append(drink)
        return f"Added {name} ({drink_type}) to the food menu"

    def reserve_table(self, number_of_people):
        for table in self.tables_repository:
            if not table._is_reversed and table.capacity >= number_of_people:
                table._is_reversed = True
                table.number_of_people = number_of_people
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number, *food_name):
        table = self._select_table(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        ordered, unordered = [], []
        for order in food_name:
            for food in self.food_menu:
                if order == food.name:
                    ordered.append(repr(food))
                else:
                    unordered.append(repr(food))

        info = [f"Table {table_number} ordered:"]
        info.extend(ordered)
        info.extend([f"{self.name} does not have in the menu:"])
        info.extend(unordered)
        return '\n'.join(info)

    def _select_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    def order_drink(self, table_number, *drinks_name):
        table = self._select_table(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        ordered, unordered = [], []
        for order in drinks_name:
            for drink in self.drinks_menu:
                if order == drink.name:
                    ordered.append(repr(drink))
                else:
                    unordered.append(repr(drink))

        info = [f"Table {table_number} ordered:"]
        info.extend(ordered)
        info.extend([f"{self.name} does not have in the menu:"])
        info.extend(unordered)
        return '\n'.join(info)

    def leave_table(self, table_number):
        table = self._select_table(table_number)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f"Table: {table_number}\n" \
               f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        info = []
        for table in self.tables_repository:
            if not table._is_reversed:
                info.append(table.free_table_info())

        return '\n'.join(info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"