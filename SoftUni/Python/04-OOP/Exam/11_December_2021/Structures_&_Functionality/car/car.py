from abc import ABC, abstractmethod


class Car(ABC):
    _MINIMUM_SPEED_LIMIT = 0
    _MAXIMUM_SPEED_LIMIT = 0

    def __init__(self, model, speed_limit):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value not in range(self._MINIMUM_SPEED_LIMIT, self._MAXIMUM_SPEED_LIMIT):
            raise ValueError(f"Invalid speed limit! Must be between {self._MINIMUM_SPEED_LIMIT} and {self._MAXIMUM_SPEED_LIMIT - 1}!")

        self.__speed_limit = value
