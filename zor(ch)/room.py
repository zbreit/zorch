from item import Item, ItemList, Weapon
import sys

class Room(object):
    'A class to represent the locations to which the player can travel'
    def __init__(self, name, description, possibleDirections, itemList):
        self.name               = name                # The name of the room
        self.description        = description         # A description of the room
        self.possibleDirections = possibleDirections  # A list of possible directions the player go from this room
        self.itemList           = itemList            # A list of all of the items in the room
        
    def examineRoom(self):
        print(self.description)
        i = 1
        if(len(self.itemList) != 0):
            sys.stdout.write("There is also ")
            for item in self.itemList:
                if(i < len(self.itemList)):
                    sys.stdout.write("a " + item.name + ", ")
                elif(i == len(self.itemList)):
                    if(i != 1):
                        sys.stdout.write("and ")
                    sys.stdout.write("a " + item.name)
                i += 1
            print(" in the " + self.name + ".")
        
            
            
openingRoom = Room(name = "shack",
                   description = "A dingy shack with glass windows leading out the back. A ladder leads up to the attic.",
                   possibleDirections = ["east", "west", "up"],
                   itemList = [ Weapon(damage = 20, 
                                       durability = 10, 
                                       name = "Long Sword", 
                                       description = "A sharp and heavy sword. Only for the experienced fighter.", 
                                       size = 20)])

openingRoom.examineRoom()