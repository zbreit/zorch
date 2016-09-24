import pdb

class Item(object):
    'A base class for all objects that your character can pick up'
    
    def __init__(self, name, description, size):
        self.name        = name         # The name of the object
        self.description = description  # The description of the object
        self.size        = size         # Size delimits the space that an item takes up in the inventory
        
    def __str__(self):
        return self.name
        

class Weapon(Item):
    'Any damage dealing item'
    
    def __init__(self, damage, durability, **kwargs):
        super(Weapon, self).__init__(**kwargs) # Set the other attributes
        
        self.damage     = damage      # Amount of damage this weapon does to enemies
        self.durability = durability  # Number of times you can use the item (questionable feature)
        
        
class ItemList(object):
    'A container for items'
    
    def __init__(self, contents):
        self.contents = contents # A list containing all of the current items in an itemList
        
    def add(self, *items):
        [self.contents.append(item) for item in items]
            
        
        
class Inventory(ItemList):
    'An itemlist of all of the things the player is holding'
    
    def add(self, items):
        for currentItem in items:
            # If the used up space plus the objects size do not exceed capacity...
            if(self.usedSpace + currentItem.size < self.capacity):
                # Add the item to the contents and modify the used size
                self.usedSpace += currentItem.size
                self.contents.append(currentItem)
                
            else:
                self.handleItemError(currentItem)
                
    def __init__(self, capacity, currentContents = []):
        self.contents = []
        self.capacity = capacity
        self.usedSpace = 0
        self.add(currentContents)
        

    def handleItemError(self, item1):
        print("Your can't hold the " + item1.name + ". You have to leave something behind.")
        

sword = Weapon(damage = 20, durability = 10, name = "Long Sword", description = "A sharp and heavy sword. Only for the experienced fighter.", size = 20)
fireStaff = Weapon(damage = 50, durability = 5, name = "Fire Staff", description = "A staff infused with the fiery essence of Merlin in it's crystal tip.", size = 20)
soup = Item(name = "Soup", description = "Famous homemade soup, can I get another bowl?", size = 2)

playerInv = Inventory(capacity = 100, currentContents = [sword, fireStaff, soup])

# print([str(x) for x in playerInv.contents])