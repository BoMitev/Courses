from project.car.car import Car


class MuscleCar(Car):
    _MINIMUM_SPEED_LIMIT = 250
    _MAXIMUM_SPEED_LIMIT = 451

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)