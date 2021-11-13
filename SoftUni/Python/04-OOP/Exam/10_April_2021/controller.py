from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    _TYPES_OF_AQUARIUMS = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium,
    }
    _TYPES_OF_DECORATIONS = {
        "Ornament": Ornament,
        "Plant": Plant,
    }
    _TYPES_OF_FISH = {
        "FreshwaterFish": FreshwaterFish,
        "SaltwaterFish": SaltwaterFish,
    }

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type not in self._TYPES_OF_AQUARIUMS:
            return "Invalid aquarium type."

        aquarium = self._TYPES_OF_AQUARIUMS[aquarium_type](aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        if decoration_type not in self._TYPES_OF_DECORATIONS:
            return "Invalid decoration type."

        decoration = self._TYPES_OF_DECORATIONS[decoration_type]()
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def _aquarium_by_name(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium

    def insert_decoration(self, aquarium_name, decoration_type):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = self._aquarium_by_name(aquarium_name)
        if aquarium is not None:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        if fish_type not in self._TYPES_OF_FISH:
            return f"There isn't a fish of type {fish_type}."

        fish = self._TYPES_OF_FISH[fish_type](fish_name, fish_species, price)
        aquarium = self._aquarium_by_name(aquarium_name)

        if fish.AQUARIUM != aquarium.__class__.__name__:
            return "Water not suitable."

        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name):
        aquarium = self._aquarium_by_name(aquarium_name)
        fed_count = aquarium.feed()

        return f"Fish fed: {fed_count}"

    def calculate_value(self, aquarium_name):
        aquarium = self._aquarium_by_name(aquarium_name)

        total = 0
        for decorations in aquarium.decorations:
            total += decorations.price

        for fish in aquarium.fish:
            total += fish.price

        return f"The value of Aquarium {aquarium_name} is {total:.2f}."

    def report(self):
        info = []
        for aquarium in self.aquariums:
            info.append(str(aquarium))

        return '\n'.join(info)
