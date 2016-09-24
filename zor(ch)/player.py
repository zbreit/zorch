from item import Item, Weapon, ItemList

class Player:
    'The user'
    def __init__(self):
        self.health = 100
        self.inventory = ItemList(capacity = 100)
        self.equippedWeapon = Weapon(damage      = 20, 
                                     durability  = 10, 
                                     name        = "Long Sword", 
                                     description = "A sharp and heavy sword. Only for the experienced fighter.", 
                                     size        = 20)