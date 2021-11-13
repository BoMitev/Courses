from abc import ABC


class BaseDecoration(ABC):
    def __init__(self, comfort, price):
        self.comfort = comfort
        self.price = price
