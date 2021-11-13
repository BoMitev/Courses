from abc import ABC, abstractmethod
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")

        self.__name = value

    def calculate_comfort(self):
        total = 0
        for decoration in self.decorations:
            total += decoration.comfort

        return total

    def add_fish(self, fish: BaseFish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."

        if fish.__class__.AQUARIUM == self.__class__.__name__:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        count = 0
        for fish in self.fish:
            fish.eat()
            count += 1

        return count

    def __str__(self):
        names = [fish.name for fish in self.fish]
        return f"{self.name}:\n" \
               f"Fish: {' '.join(names) if len(names) > 0 else 'none'}\n" \
               f"Decorations: {len(self.decorations)}\n" \
               f"Comfort: {self.calculate_comfort()}"
