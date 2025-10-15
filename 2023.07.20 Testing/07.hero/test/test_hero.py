import unittest
from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("A", 1, 20, 3)

    def test_initialization(self):
        self.assertEqual("A", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(20, self.hero.health)
        self.assertEqual(3, self.hero.damage)

    def test_battle_self(self):
        enemy = Hero("A", 4, 5, 6)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception.args[0]))

    def test_self_zero_health(self):
        hero = Hero("A", 1, 0, 2)
        enemy = Hero("B", 4, 5, 6)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception.args[0]))

    def test_enemy_zero_health(self):
        enemy = Hero("B", 4, 0, 6)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(ex.exception.args[0]))

    def test_battle(self):
        enemy = Hero("B", 1, 20, 3)
        self.assertEqual("You lose", self.hero.battle(enemy))
        self.assertEqual(17, self.hero.health)
        self.assertEqual(2, enemy.level)
        self.assertEqual(22, enemy.health)
        self.assertEqual(8, enemy.damage)

    def test_draw(self):
        hero = Hero("A", 1, 1, 2)
        enemy = Hero("B", 1, 1, 2)
        self.assertEqual("Draw", hero.battle(enemy))

    def test_win(self):
        hero = Hero("A", 10, 100, 20)
        enemy = Hero("B", 1, 10, 2)
        self.assertEqual("You win", hero.battle(enemy))
        self.assertEqual(11, hero.level)
        self.assertEqual(103, hero.health)
        self.assertEqual(25, hero.damage)

    def test_str(self):
        self.assertEqual(f"Hero {self.hero.username}: {self.hero.level} lvl\nHealth: {self.hero.health}\nDamage:"
                         f" {self.hero.damage}\n", self.hero.__str__())


if __name__ == "__main__":
    unittest.main()
