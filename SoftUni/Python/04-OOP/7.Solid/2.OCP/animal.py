from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def animal_sound(self):
        pass


class Dog(Animal):
    def animal_sound(self):
        return 'woof-woof'


class Cat(Animal):
    def animal_sound(self):
        return 'meow'
