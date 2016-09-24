class Command(object):
    'A class to associate terminal input to game commands'
    commandList    = [] # A list of all valid commands
    
    commandHistory = [] # A list of all of the commands just used
    
    def __init__(self, function, spellings):
        
        self.function  = function  # The function that should be executed when this command is entered
        
        self.spellings = spellings # List of spellings/equivalent words that trigger a command (i.e. ["east", "e", "left", "l"]).
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
back  = Command(function  = fillerFunction,
               spellings = ["back", "b"])  
               
# Checks if a user input is a valid spelling of any command. If yes, execute that command.               
[command.execute() for command in Command.commandList for spelling in command.spellings if(userInput == spelling)]

        