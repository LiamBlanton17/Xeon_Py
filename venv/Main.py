# Main Class
import copy

# Import all other classes
import Board, wKing, wQueen, wRook, wBishop, wKnight, wPawn, bKing, bQueen, bRook, bBishop, bKnight, bPawn, Empty
from Board import *
from wKing import *
from wQueen import *
from wRook import *
from wBishop import *
from wKnight import *
from wPawn import *
from bKing import *
from bQueen import *
from bRook import *
from bBishop import *
from bKnight import *
from bPawn import *
from Empty import *

#Starting conditions
startingBoard = [[wRook(), wKnight(), wBishop(), wQueen(), wKing(), wBishop(), wKnight(), wRook()],
                 [wPawn(), wPawn(), wPawn(), wPawn(), wPawn(), wPawn(), wPawn(), wPawn()],
                 [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                 [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                 [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                 [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                 [bPawn(), bPawn(), bPawn(), bPawn(), bPawn(), bPawn(), bPawn(), bPawn()],
                 [bRook(), bKnight(), bBishop(), bQueen(), bKing(), bBishop(), bKnight(), bRook()]]

#Create the main Board object
mainBoard = Board(startingBoard)

#Board history list
boardHistory = [copy.deepcopy(mainBoard)]

#Userinput Items
uInParse = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    '1': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7
}  # Dictionary to parse user input
#Function to take and convert user input (returns a move that can be used to make a legal move on the mainBoard)
#Function contains a lof of messy conversions
def takeUIn():
    #Get the move
    uIn = list(input("Enter your move: "))
    #Loop through and parse the move, check if the move is right length, and throw error if not a valid row/col
    for i in range(4):
        if len(uIn) != 4:
            break
        try:
            uIn[i] = uInParse[uIn[i]]
        except KeyError:
            uIn[i] = 9
    #Convert to be able to check against mainBoard.moves
    if len(uIn) == 4:
        temp = uIn[0]
        uIn[0] = uIn[2]
        uIn[2] = temp
        temp = uIn[1]
        uIn[1] = uIn[3]
        uIn[3] = temp
        uIn = int(''.join(str(digit) for digit in uIn))
    #Rerun if not in list of mainBoard.moves
    if not mainBoard.moves.__contains__(uIn):
        print("Enter a valid move")
        return takeUIn()
    return uIn


#Loop
mainBoard.PrintBoard()
print(mainBoard.moves)
print(len(mainBoard.moves))

move = takeUIn()

print(move)
