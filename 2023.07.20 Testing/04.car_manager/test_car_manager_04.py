class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


import unittest


class CarTest(unittest.TestCase):
    def setUp(self):
        self.car = Car("A", "B", 1, 10)

    def test_initialization(self):
        self.assertEqual("A", self.car.make)
        self.assertEqual("B", self.car.model)
        self.assertEqual(1, self.car.fuel_consumption)
        self.assertEqual(10, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter(self):
        car = Car("C", "D", 1, 1)
        self.assertEqual("C", car.make)

    def test_make_setter_empty(self):
        with self.assertRaises(Exception) as ex:
            car = Car("", "D", 1, 1)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception.args[0]))

    def test_model_setter(self):
        car = Car("C", "D", 1, 1)
        self.assertEqual("D", car.model)

    def test_model_setter_empty(self):
        with self.assertRaises(Exception) as ex:
            car = Car("C", "", 1, 1)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception.args[0]))

    def test_fuel_consumption_setter(self):
        car = Car("C", "D", 2, 1)
        self.assertEqual(2, car.fuel_consumption)

    def test_fuel_consumption_setter_zero(self):
        with self.assertRaises(Exception) as ex:
            car = Car("C", "D", 0, 1)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception.args[0]))

    def test_fuel_capacity_setter(self):
        car = Car("C", "D", 1, 2)
        self.assertEqual(2, car.fuel_capacity)

    def test_fuel_capacity_setter_zero(self):
        with self.assertRaises(Exception) as ex:
            car = Car("C", "D", 1, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception.args[0]))

    def test_fuel_amount_setter(self):
        self.car.fuel_amount = 3
        self.assertEqual(3, self.car.fuel_amount)

    def test_fuel_amount_setter_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = - 1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception.args[0]))

    def test_refuel_correct(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(5)
        self.assertEqual(5, self.car.fuel_amount)

    def test_refuel_with_negative(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception.args[0]))

    def test_refuel_overflow(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(20)
        self.assertEqual(10, self.car.fuel_amount)

    def test_drive_correct(self):
        self.car.fuel_amount = 10
        self.assertEqual(10, self.car.fuel_amount)
        self.car.drive(10)
        self.assertEqual(9.9, self.car.fuel_amount)

    def test_drive_not_enough_fuel(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception.args[0]))


if __name__ == "__main__":
    unittest.main()
