from classes.items import Item, Weapon, Healing
import random


class Character:
    def __init__(self, name: str, max_hp: int, weapon: Weapon, healing: Healing):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.inventory = []
        self.weapon = weapon
        self.healing = healing

    def attack(self, enemy) -> str:
        if random.randint(0,5) == 0:
            return f"{self.name} tried to attack {enemy.name} but missed!"
        else:
            enemy.hp -= self.weapon.damage
            return f"{self.name} deals {self.weapon.damage} damage to {enemy.name}"

    def heal(self) -> str:
        self.hp += self.healing.healing_points
        self.healing.quantity -= 1

        if self.hp > self.max_hp:
            self.hp = self.max_hp

        return f"{self.name} heals himself (+{self.healing.healing_points}HP)"


class Player(Character):
    def player_choice(self, enemy):
        print("1. Attack")
        print("2. Heal")
        print("3. Escape")
        action = int(input("> "))

        if action == 1:
            print(self.attack(enemy))
        elif action == 2:
            if self.healing.quantity > 0:
                print(self.heal())
            else:
                print("You don't have any healing!")
        else:
            print("You have been escaped!")
            return 0


class Enemy(Character):
    def make_choice(self, enemy) -> str:
        if self.hp < self.max_hp/2:
            if enemy.hp <= self.weapon.damage or self.healing.quantity == 0:
                return self.attack(enemy)
            else:
                return self.heal()
        else:
            return self.attack(enemy)
