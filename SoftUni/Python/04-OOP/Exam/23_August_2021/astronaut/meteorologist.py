from everland.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    BREATH_UNITS = 15
    DEFAULT_OXYGEN_LEVEL = 90

    def __init__(self, name: str) -> None:
        super().__init__(name, self.DEFAULT_OXYGEN_LEVEL)

    def breathe(self) -> None:
        self.oxygen -= self.BREATH_UNITS
