from everland.appliances.tv import TV
from everland.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, family_name, salary):
        super().__init__(family_name, salary, 1)
        self.room_cost = 10
        self.appliances = [TV()]
        self.calculate_expenses(self.appliances)