from project.appliances.appliance import Appliance
from project.people.child import Child


class Room:
    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

        self.__expenses = value

    def calculate_expenses(self, *args):
        total = 0
        for list_el in args:
            for appliance in list_el:
                if isinstance(appliance, Appliance):
                    total += appliance.get_monthly_expense()
                elif isinstance(appliance, Child):
                    total += appliance.cost * 30

        self.expenses = total
