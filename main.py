from classes.characters import Character, Player, Enemy
from classes.items import Item, Weapon, Healing


class Game:
    def __init__(self, player: Player):
        self.player = player

    def check_death(self, character: Character):
        if character.hp <= 0:
            print(f"{character.name} died!")
            return True
        else:
            return False

    def fight(self, enemy: Enemy):
        while True:
            if self.player.player_choice(enemy) == 0:
                break

            if self.check_death(enemy):
                break

            print(enemy.make_choice(self.player))
            if self.check_death(self.player):
                break

            print("--------------------")
            print(f"{self.player.name} has {self.player.hp} HP")
            print(f"{enemy.name} has {enemy.hp} HP")
            print()


sword = Weapon(1, "Sword", "common", 20, "none")
spear = Weapon(2, "Spear", "common", 15, "none")

healing1 = Healing(3, "Healing potion", "common", 15, 2)
healing2 = Healing(3, "Healing potion", "common", 15, 2)

player = Player("Player", 50, sword, healing1)
goblin = Enemy("Goblin", 100, spear, healing2)

game = Game(player)

game.fight(goblin)
