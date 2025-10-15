from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

    @staticmethod
    @abstractmethod
    def make_sound():
        pass


class Cat(Animal):
    def __init__(self, species):
        super().__init__(species)

    @staticmethod
    def make_sound():
        return "Meow"


class Dog(Animal):
    def __init__(self, species):
        super().__init__(species)

    @staticmethod
    def make_sound():
        return "Woof"


animals = [Cat('cat'), Dog('dog')]
for animal in animals:
    print(animal.make_sound())
