from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    _DEFAULT_INCREASE_PER_EAT = 3
    AQUARIUM = "FreshwaterAquarium"

    def __init__(self, name, species, price):
        super().__init__(name, species, 3, price)

    def eat(self):
        self.size += self._DEFAULT_INCREASE_PER_EAT
