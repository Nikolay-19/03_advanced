class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception("Not enough energy.")

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f"{self.name} has saved {self.money} money."


import unittest


class WorkerTests(unittest.TestCase):
    def test_worker_initialization(self):
        worker = Worker("A", 100, 2)
        self.assertEqual("A", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(2, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_energy_increase(self):
        worker = Worker("A", 100, 2)
        self.assertEqual(2, worker.energy)
        worker.rest()
        self.assertEqual(3, worker.energy)

    def test_work_zero_or_negative_energy(self):
        worker = Worker("A", 100, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception.args[0]))

    def test_work_salary_increase(self):
        worker = Worker("A", 100, 2)
        self.assertEqual(0, worker.money)
        worker.work()
        self.assertEqual(100, worker.money)

    def test_work_energy_decrease(self):
        worker = Worker("A", 100, 2)
        self.assertEqual(2, worker.energy)
        worker.work()
        self.assertEqual(1, worker.energy)

    def test_get_info(self):
        worker = Worker("A", 100, 2)
        self.assertEqual(f"{worker.name} has saved {worker.money} money.", worker.get_info())


if __name__ == '__main__':
    unittest.main()
