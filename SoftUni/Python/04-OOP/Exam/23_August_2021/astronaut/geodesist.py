from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 50)

    def breathe(self):
        self.oxygen -= self._BREATHE_OXYGEN
