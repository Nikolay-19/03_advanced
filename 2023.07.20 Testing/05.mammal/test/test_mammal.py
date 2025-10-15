import unittest
from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.animal = Mammal("A", "B", "C")

    def test_initialization(self):
        self.assertEqual("A", self.animal.name)
        self.assertEqual("B", self.animal.type)
        self.assertEqual("C", self.animal.sound)
        self.assertEqual("animals", self.animal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual("A", self.animal.name)
        self.assertEqual("C", self.animal.sound)
        self.assertEqual(f"{self.animal.name} makes {self.animal.sound}", self.animal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.animal.get_kingdom())

    def test_info(self):
        self.assertEqual(f"{self.animal.name} is of type {self.animal.type}", self.animal.info())


if __name__ == "__main__":
    unittest.main()
