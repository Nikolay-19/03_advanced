from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    ac_on = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__()
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        a = (self.fuel_consumption + Car.ac_on) * distance
        if self.fuel_quantity >= a:
            self.fuel_quantity -= a

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    ac_on = 1.6
    hole = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__()
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        a = (self.fuel_consumption + Truck.ac_on) * distance
        if self.fuel_quantity >= a:
            self.fuel_quantity -= a

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * Truck.hole)
