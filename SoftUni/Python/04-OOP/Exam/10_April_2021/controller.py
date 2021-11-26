from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    _AQUARIUM_TYPES = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium,
    }
    _DECORATION_TYPES = {
        "Ornament": Ornament,
        "Plant": Plant,
    }
    _FISH_TYPES = {
        "FreshwaterFish": FreshwaterFish,
        "SaltwaterFish": SaltwaterFish,
    }

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def find_aquarium_by_name(self, name):
        for aquarium in self.aquariums:
            if aquarium.name == name:
                return aquarium

        return False

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type not in self._AQUARIUM_TYPES:
            return "Invalid aquarium type."

        aquarium = self._AQUARIUM_TYPES[aquarium_type](aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        if decoration_type not in self._DECORATION_TYPES:
            return "Invalid decoration type."

        decoration = self._DECORATION_TYPES[decoration_type]()
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        if aquarium:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        if fish_type not in self._FISH_TYPES:
            return f"There isn't a fish of type {fish_type}."

        fish = self._FISH_TYPES[fish_type](fish_name, fish_species, price)
        aquarium = self.find_aquarium_by_name(aquarium_name)

        if aquarium.suitable_fish != fish_type:
            return "Water not suitable."

        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        fed_count = aquarium.feed()

        return f"Fish fed: {fed_count}"

    def calculate_value(self, aquarium_name):
        aquarium = self.find_aquarium_by_name(aquarium_name)

        fish_prices = sum([fish.price for fish in aquarium.fish])
        decoration_prices = sum([decoration.price for decoration in aquarium.decorations])
        total = fish_prices + decoration_prices

        return f"The value of Aquarium {aquarium_name} is {total:.2f}."

    def report(self):
        info = [str(aquarium) for aquarium in self.aquariums]

        return '\n'.join(info)
