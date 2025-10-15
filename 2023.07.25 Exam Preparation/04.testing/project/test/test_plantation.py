import unittest
from project.plantation import Plantation


class TestPlantation(unittest.TestCase):
    def setUp(self):
        self.plant = Plantation(2)

    def test_init(self):
        self.assertEqual(2, self.plant.size)
        self.assertEqual({}, self.plant.plants)
        self.assertEqual([], self.plant.workers)

    def test_wrong_size(self):
        with self.assertRaises(Exception) as ex:
            plant = Plantation(-1)
        self.assertEqual("Size must be positive number!", ex.exception.args[0])

    def test_hire_worker(self):
        worker = "Prokopi"
        self.assertEqual("Prokopi successfully hired.", self.plant.hire_worker(worker))
        self.assertEqual(["Prokopi"], self.plant.workers)

    def test_hire_existing_worker(self):
        worker = "Prokopi"
        self.plant.hire_worker(worker)
        with self.assertRaises(Exception) as ex:
            self.plant.hire_worker(worker)
        self.assertEqual("Worker already hired!", ex.exception.args[0])

    def test_len(self):
        plant = Plantation(4)
        plant.hire_worker("Prokopi")
        plant.hire_worker("John")
        plant.planting("Prokopi", "lily")
        plant.planting("Prokopi", "daffodil")
        plant.planting("John", "rose")
        self.assertEqual({"Prokopi": ["lily", "daffodil"], "John": ["rose"]}, plant.plants)
        self.assertEqual(3, plant.__len__())

    def test_planting_non_existing_worker(self):
        worker = "Prokopi"
        with self.assertRaises(Exception) as ex:
            self.plant.planting(worker, "A")
        self.assertEqual("Worker with name Prokopi is not hired!", ex.exception.args[0])

    def test_planting_full_plantation(self):
        plant = Plantation(0)
        plant.hire_worker("Prokopi")
        with self.assertRaises(Exception) as ex:
            plant.planting("Prokopi", "A")
        self.assertEqual("The plantation is full!", ex.exception.args[0])

    def test_planting_first_plant(self):
        self.plant.hire_worker("Prokopi")
        self.assertEqual("Prokopi planted it's first lily.", self.plant.planting("Prokopi", "lily"))
        self.assertEqual({"Prokopi": ["lily"]}, self.plant.plants)

    def test_planting_second_plant(self):
        self.plant.hire_worker("Prokopi")
        self.assertEqual("Prokopi planted it's first lily.", self.plant.planting("Prokopi", "lily"))
        self.assertEqual("Prokopi planted daffodil.", self.plant.planting("Prokopi", "daffodil"))
        self.assertEqual({"Prokopi": ["lily", "daffodil"]}, self.plant.plants)

    def test_str(self):
        self.plant.hire_worker("Prokopi")
        self.assertEqual("Prokopi planted it's first lily.", self.plant.planting("Prokopi", "lily"))
        self.assertEqual("Prokopi planted daffodil.", self.plant.planting("Prokopi", "daffodil"))
        self.assertEqual({"Prokopi": ["lily", "daffodil"]}, self.plant.plants)
        self.assertEqual("Plantation size: 2\nProkopi\nProkopi planted: lily, daffodil", self.plant.__str__())

    def test_repr(self):
        self.plant.hire_worker("Prokopi")
        self.assertEqual("Size: 2\nWorkers: Prokopi", self.plant.__repr__())


if __name__ == "__main__":
    unittest.main()
