from item import Inventory, Weapon

class Player:
    'The user'
    def __init__(self):
        self.health = 100 
        
        # Object Definitions
        self.inventory      = Inventory(capacity = 100)
        self.equippedWeapon = Weapon(damage      = 5, 
                                     durability  = 1, 
                                     name        = "Shiv", 
                                     description = "A toothbrush with a razor blade attached.", 
                                     size        = 2)
        self.currentRoom    = None 
