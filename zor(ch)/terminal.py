class Command(object):
    'A class to associate terminal input to game commands'
    commandList = []
    # A list of all of the commands
    commandHistory = []
    
    def __init__(self, function, spellings):
        # The function that should be executed when this command is entered
        self.function = function
        # List of possible spellings for a command (i.e. ["east", "e"] or ["take", "t"]).
        # Can also include other equivalent words (i.e. ["east", "e", "left", "l")
        self.spellings = spellings
        Command.commandList.append(self)
        
    def execute(self, *args):
        self.function(*args)




userInput = input("Which direction would you like to go? ").lower()

def fillerFunction():
    pass

# Directional Commands
north = Command(function  = fillerFunction,
               spellings = ["north", "n"])
south = Command(function  = fillerFunction,
               spellings = ["south", "s"])
east  = Command(function  = fillerFunction,
               spellings = ["east", "e", "right", "r"])               
west  = Command(function  = fillerFunction,
               spellings = ["west", "w", "left", "l"])
up    = Command(function  = fillerFunction,
               spellings = ["up", "u"])
down  = Command(function  = fillerFunction,
               spellings = ["down", "d"])
               
               
[command.execute() for command in Command.commandList for spelling in command.spellings if(userInput == spelling)]

        