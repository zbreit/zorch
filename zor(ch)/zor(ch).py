from player import Player
from time import sleep
import sys

def delayPrint(printMessage):
    for letter in printMessage:
        sys.stdout.write(letter)
        sys.stdout.flush()
        if(letter == "." or letter == "–"):
            sleep(0.35)
        elif(letter == ","):
            sleep(0.2)
        else:
            sleep(0.075)
    sleep(0.45)
    sys.stdout.write('\n')
    

def setTheScene():
    delayPrint("You wake up to the sound of rain hitting against the glass window of your prison cell.")
    delayPrint("A faint mutter is recognizable, ")
    
setTheScene()
player = Player()
gameIsOngoing = False

while gameIsOngoing:
    pass