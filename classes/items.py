class Item:
    def __init__(self, item_id: int, name: str, rarity: str):
        self.id = item_id
        self.name = name
        self.rarity = rarity


class Weapon(Item):
    def __init__(self, item_id: int, name: str, rarity: str, damage: int, effect: str):
        super().__init__(item_id, name, rarity)
        self.damage = damage
        self.effect = effect


class Healing(Item):
    def __init__(self, item_id: int, name: str, rarity: str, healing_points: int, quantity: int):
        super().__init__(item_id, name, rarity)
        self.healing_points = healing_points
        self.quantity = quantity
