from abc import ABC, abstractmethod


class Supply(ABC):
    def __init__(self, name, energy):
        if type(self) == Supply:
            raise Exception

        self.name = name
        self.energy = int(energy)

        if not self.name:
            raise ValueError("Name cannot be an empty string.")

        if self.energy < 0:
            raise ValueError("Energy cannot be less than zero.")

    @abstractmethod
    def details(self):
        pass
