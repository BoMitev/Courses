from everland.appliances.fridge import Fridge
from everland.appliances.stove import Stove
from everland.appliances.tv import TV
from everland.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, pension_one + pension_two, 2)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()] * 2
        self.calculate_expenses(self.appliances)