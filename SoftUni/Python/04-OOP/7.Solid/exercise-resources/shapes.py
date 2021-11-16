from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, side_a, height):
        self.height = height
        self.side_a = side_a

    def area(self):
        return self.side_a * self.height * 0.5


class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        assert isinstance(value, list), "`shapes` should be of type `list`."

        self.__shapes = value

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area()

        return total


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
