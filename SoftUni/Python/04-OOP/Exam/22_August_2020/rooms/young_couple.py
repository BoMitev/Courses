from everland.appliances.fridge import Fridge
from everland.appliances.laptop import Laptop
from everland.appliances.tv import TV
from everland.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop()] * 2
        self.calculate_expenses(self.appliances)