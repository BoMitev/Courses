from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    _DEFAULT_INCREASE_PER_EAT = 2
    AQUARIUM = "SaltwaterAquarium"

    def __init__(self, name, species, price):
        super().__init__(name, species, 5, price)

    def eat(self):
        self.size += self._DEFAULT_INCREASE_PER_EAT
