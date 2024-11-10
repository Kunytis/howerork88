# этот проект я еще не делала по этому тут будет видно что я писала!!

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def atk(self):
        raise ImplError("erroer")

class Hero(Character):
    def __init__(self, name, health, sword):
        ult(). __init__(name, health)
        self.sword = sword

    def attack(self):
        print(f"{self.name} fights with {self.sword}!!!11!!!1!1")


class Enemy():
    def __init__(self, name, health, damage):
        ult().__init__(health, name)
        self.damage = damage

    def attack(self):
        print(f"{self.name} deals {self.damage} damage!")


hero = Hero("kn", 100, "sword")
enemy = Enemy("monst", 50, 10)

hero.attack()
enemy.attack()