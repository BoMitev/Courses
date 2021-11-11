from everland.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    BREATH_UNITS = 5
    DEFAULT_OXYGEN_LEVEL = 70

    def __init__(self, name: str) -> None:
        super().__init__(name, self.DEFAULT_OXYGEN_LEVEL)

    def breathe(self) -> None:
        self.oxygen -= self.BREATH_UNITS
