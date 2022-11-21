import unittest
from game import Tank

class TestTank(unittest.TestCase):
    def test_shoot(self):
        tank1 = Tank(model="T-34", armor=10, min_damage=10, max_damage=20, health=100)
        tank2 = Tank(model="Tiger", armor=10, min_damage=10, max_damage=20, health=1)
        expected = f"Экипаж танка {tank2.model} уничтожен"

        actual = tank1.shoot(tank2)
        self.assertEqual(actual, expected)

        tank2 = Tank(model="Tiger", armor=10, min_damage=10, max_damage=20, health=100)

        actual = tank1.shoot(tank2)
        expected = f"{tank1.model}: Точно в цель, у противника {tank2.model} осталось {tank2.health:.2f} единиц здоровья"
        self.assertEqual(actual, expected)
