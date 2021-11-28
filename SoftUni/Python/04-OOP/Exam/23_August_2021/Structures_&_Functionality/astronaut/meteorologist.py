from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    _BREATHE_OXYGEN = 15

    def __init__(self, name):
        super().__init__(name, 90)

    def breathe(self):
        self.oxygen -= self._BREATHE_OXYGEN
