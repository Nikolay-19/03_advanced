import unittest
from project.second_hand_car import SecondHandCar


class TestSecondHandCar(unittest.TestCase):
    def setUp(self):
        self.car = SecondHandCar("Astra", "coupe", 144000, 10000.0)

    def test_init_(self):
        self.assertEqual("Astra", self.car.model)
        self.assertEqual("coupe", self.car.car_type)
        self.assertEqual(144000, self.car.mileage)
        self.assertEqual(10000.0, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_invalid_price(self):
        with self.assertRaises(Exception) as ex:
            car = SecondHandCar("A", "B", 1000, 1)
        self.assertEqual("Price should be greater than 1.0!", ex.exception.args[0])

    def test_invalid_mileage(self):
        with self.assertRaises(Exception) as ex:
            car = SecondHandCar("A", "B", 100, 1000)
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", ex.exception.args[0])

    def test_promotional_price(self):
        self.assertEqual("The promotional price has been successfully set.", self.car.set_promotional_price(7500.0))
        self.assertEqual(7500.0, self.car.price)

    def test_wrong_promotional_price(self):
        with self.assertRaises(Exception) as ex:
            self.car.set_promotional_price(12500.0)
        self.assertEqual("You are supposed to decrease the price!", ex.exception.args[0])
        self.assertEqual(10000.0, self.car.price)

    def test_need_repair(self):
        self.assertEqual("Price has been increased due to repair charges.", self.car.need_repair(1000.0, "Brakes"))
        self.assertEqual(11000.0, self.car.price)
        self.assertEqual(["Brakes"], self.car.repairs)

    def test_repair_too_expensive(self):
        self.assertEqual("Repair is impossible!", self.car.need_repair(5001.0, "Fractured crankshaft"))
        self.assertEqual(10000.0, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_greater_than(self):
        car2 = SecondHandCar("Corsa", "coupe", 122000, 7500.0)
        self.assertEqual(True, self.car.__gt__(car2))
        self.assertEqual(False, car2.__gt__(self.car))

    def test_greater_than_wrong_type(self):
        car2 = SecondHandCar("Insignia", "sedan", 122000, 12500.0)
        self.assertEqual("Cars cannot be compared. Type mismatch!", self.car.__gt__(car2))

    def test_str(self):
        self.assertEqual(f"""Model Astra | Type coupe | Milage 144000km
Current price: 10000.00 | Number of Repairs: 0""",
                         self.car.__str__())


if __name__ == "__main__":
    unittest.main()
