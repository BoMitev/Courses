from abc import ABC


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
        return sum([decoration.comfort for decoration in self.decorations])

    def add_fish(self, fish):
        TYPES_OF_FISH = ["FreshwaterFish", "SaltwaterFish"]

        if len(self.fish) >= self.capacity :
            return "Not enough capacity."

        if fish.__class__.__name__ in TYPES_OF_FISH:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def feed(self):
        count = 0
        for fish in self.fish:
            fish.eat()
            count += 1

        return count

    def __str__(self):
        fish_names = [fish.name for fish in self.fish]

        return f"{self.name}:\n" \
               f"Fish: {' '.join(fish_names) if fish_names else 'none'}\n" \
               f"Decorations: {len(self.decorations)}\n" \
               f"Comfort: {self.calculate_comfort()}"
