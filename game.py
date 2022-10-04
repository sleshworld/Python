import random


class Tank:
    def __init__(self, model, armor, min_damage, max_damage, health) -> None:
        self.model = model
        self.armor = armor
        self.damage = random.randint(min_damage, max_damage)
        self.health = health

    def print_info(self) -> None:
        print(
            f"{self.model} имеет лобовую броню {self.armor} мм. при здоровье {self.health:.2f} ед. здоровья и урон в {self.damage} единиц"
        )

    def health_down(self, enemy) -> None:
        self.health -= enemy.damage / self.armor
        if self.health > 0:
            print(
                f"{self.model}: Командир, по экипажу {self.model} попали, у нас осталось {self.health:.2f} очков здоровья"
            )

    def shot(self, enemy) -> None:
        enemy.health_down(enemy)
        if enemy.health <= 0:
            print(f"Экипаж танка {enemy.model} уничтожен")
        else:
            print(
                f"{self.model}: Точно в цель, у противника {enemy.model} осталось {enemy.health:.2f} единиц здоровья"
            )


tank1 = Tank("T-34", 23, 10, 20, 100)
tank2 = Tank("Tiger", 23, 10, 10, 1)

tank1.print_info()

tank1.shot(tank2)
