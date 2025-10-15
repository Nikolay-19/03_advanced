import unittest
from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.car = Vehicle(10, 20)

    def test_initialization(self):
        self.assertEqual(10, self.car.fuel)
        self.assertEqual(20, self.car.horse_power)
        self.assertEqual(10, self.car.capacity)
        self.assertEqual(1.25, self.car.fuel_consumption)

    def test_drive_correct(self):
        self.assertEqual(10, self.car.fuel)
        self.car.drive(1)
        self.assertEqual(8.75, self.car.fuel)

    def test_drive_wrong(self):
        self.assertEqual(10, self.car.fuel)
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual("Not enough fuel", str(ex.exception.args[0]))

    def test_refuel_correct(self):
        self.car.fuel = 5
        self.assertEqual(5, self.car.fuel)
        self.car.refuel(1)
        self.assertEqual(6, self.car.fuel)

    def test_refuel_wrong(self):
        self.assertEqual(10, self.car.fuel)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception.args[0]))

    def test_str(self):
        self.assertEqual(f"The vehicle has {self.car.horse_power} horse power with {self.car.fuel} fuel left and "
                         f"{self.car.fuel_consumption} fuel consumption", self.car.__str__())


if __name__ == "__main__":
    unittest.main()
