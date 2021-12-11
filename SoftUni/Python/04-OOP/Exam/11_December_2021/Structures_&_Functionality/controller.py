from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    _CAR_TYPES = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar,
    }

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def check_car_by_model(self, model):
        for car in self.cars:
            if car.model == model:
                return car

        return False

    def check_driver_by_name(self, name):
        for driver in self.drivers:
            if driver.name == name:
                return driver

        return False

    def check_race_by_name(self, name):
        for race in self.races:
            if race.name == name:
                return race

        return False

    def check_car_by_type(self, car_type):
        if car_type in self._CAR_TYPES:
            for car in self.cars[-1::-1]:
                if car.__class__.__name__ == car_type and not car.is_taken:
                    return car

        return False

    def create_car(self, car_type, model, speed_limit):
        if car_type in self._CAR_TYPES:
            if self.check_car_by_model(model):
                raise Exception(f"Car {model} is already created!")

            new_car = self._CAR_TYPES[car_type](model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        if self.check_driver_by_name(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        if self.check_race_by_name(race_name):
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        driver = self.check_driver_by_name(driver_name)
        car = self.check_car_by_type(car_type)

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        if not car:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None:
            old_model = driver.car.model
            driver.car.is_taken = False

            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."

        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name, driver_name):
        driver = self.check_driver_by_name(driver_name)
        race = self.check_race_by_name(race_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        for d in race.drivers:
            if d.name == driver_name:
                return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        race = self.check_race_by_name(race_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        won_list = sorted(race.drivers, key=lambda x: x.car.speed_limit, reverse=True)

        info = []

        for driver in won_list[0:3]:
            driver.number_of_wins += 1
            info.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return '\n'.join(info)