from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    __ASTRONAUT_TYPES = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist,
    }

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.unsuccessful_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.__ASTRONAUT_TYPES:
            raise Exception("Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name) is not None:
            return f"{name} is already added."

        astronaut = self.__ASTRONAUT_TYPES[astronaut_type](name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name) is not None:
            return f"{name} is already added."

        planet = Planet(name)
        planet.items.extend(items.split(", "))
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astronaut = self.astronaut_repository.find_by_name(name)

        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception("Invalid planet name!")

        suitable_astronauts = [astronaut for astronaut in self.astronaut_repository.astronauts if astronaut.oxygen > 30]
        if not suitable_astronauts:
            raise Exception(f"You need at least one astronaut to explore the planet!")

        approved_astronauts = []
        for astronaut in sorted(suitable_astronauts, key=lambda ast: -ast.oxygen):
            if len(approved_astronauts) == 5:
                break
            approved_astronauts.append(astronaut)

        participated_astronauts = 0
        for astronaut in approved_astronauts:
            participated_astronauts += 1
            while astronaut.oxygen > 0 and planet.items:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()

            if not planet.items:
                self.successful_missions += 1
                return f"Planet: {planet_name} was explored. " \
                       f"{participated_astronauts} astronauts participated in collecting items."

        self.unsuccessful_missions += 1
        return "Mission is not completed."

    def report(self):
        info = [
            f"{self.successful_missions} successful missions!",
            f"{self.unsuccessful_missions} missions were not completed!",
            f"Astronauts' info:"
        ]

        info.extend([str(astronaut) for astronaut in self.astronaut_repository.astronauts])
        return '\n'.join(info)
