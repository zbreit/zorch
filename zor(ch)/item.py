class Item(object):
    'A base class for all objects that your character can pick up'
    
    def __init__(self, name, description, size):
        self.name = name
        self.description = description
        # Size delimits the space that an item takes up in the inventory
        self.size = size
        
    def __str__(self):
        return self.name
        

class Weapon(Item):
    'Any damage dealing item'
    
    def __init__(self, damage, durability, **kwargs):
        super(Weapon, self).__init__(**kwargs)
        self.damage = damage
        # Number of times you can use the item (questionable feature)
        self.durability = durability
        
        
class ItemList(object):
    'A container for items'
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.usedSpace = 0
        self.contents = []
        
    def add(self, *items):
        for currentItem in items:
            if self.usedSpace + currentItem.size < self.capacity:
                self.usedSpace += currentItem.size
                self.contents.append(currentItem)
            else:
                self.handleItemError(currentItem)
            
    def handleItemError(self, item1):
        print("Your can't hold the " + item1.name + ". You have to leave some items behind.")
        

sword = Weapon(damage = 20, durability = 10, name = "Long Sword", description = "A sharp and heavy sword. Only for the experienced fighter.", size = 20)
fireStaff = Weapon(damage = 50, durability = 5, name = "Fire Staff", description = "A staff infused with the fiery essence of Merlin in it's crystal tip.", size = 20)
soup = Item(name = "Soup", description = "Famous homemade soup, can I get another bowl?", size = 2)

playerInv = ItemList(capacity = 100)
playerInv.add(sword, fireStaff, soup)

print([str(x) for x in playerInv.contents])