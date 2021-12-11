from project.car.car import Car


class SportsCar(Car):
    _MINIMUM_SPEED_LIMIT = 400
    _MAXIMUM_SPEED_LIMIT = 601

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)