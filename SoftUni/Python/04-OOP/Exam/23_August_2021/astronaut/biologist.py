from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    _BREATHE_OXYGEN = 5

    def __init__(self, name):
        super().__init__(name, 70)

    def breathe(self):
        self.oxygen -= self._BREATHE_OXYGEN
