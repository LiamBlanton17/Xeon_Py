# Main Class
import copy
import sys

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
from Input import *

#Starting conditions
startingBoard = [[wRook(), wKnight(), wBishop(), wQueen(), wKing(), wBishop(), wKnight(), wRook()],
                 [wPawn(), wPawn(), wPawn(), wPawn(), wPawn(), wPawn(), wPawn(), wPawn()],
                 [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                 [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                 [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                 [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                 [bPawn(), bPawn(), bPawn(), bPawn(), bPawn(), bPawn(), bPawn(), bPawn()],
                 [bRook(), bKnight(), bBishop(), bQueen(), bKing(), bBishop(), bKnight(), bRook()]]
testingBoard = [[Empty(), wKing(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                [Empty(), Empty(), wPawn(), wPawn(), Empty(), Empty(), Empty(), Empty()],
                [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                [Empty(), Empty(), Empty(), Empty(), bPawn(), Empty(), Empty(), Empty()],
                [Empty(), Empty(), Empty(), bPawn(), Empty(), Empty(), Empty(), Empty()],
                [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                [Empty(), Empty(), bKing(), Empty(), Empty(), Empty(), Empty(), Empty()]]

#Board history list
boardHistory = []

#Create the main Board object
mainBoard = Board(startingBoard, 'white', '1111', boardHistory, True)

# Loop
while (500 > mainBoard.eval > -500) and len(mainBoard.moves) > 0:
    print("MAIN BOARD ------------------- ")
    mainBoard.PrintBoard()
    print(mainBoard.getEval())
    print("MAIN BOARD ------------------- ")
    move = takeUIn(mainBoard)
    if move == 9999:  # Debugging statement, code 9999 to draw game
        break
    mainBoard.updateBoard(move, boardHistory, True)

print("GG")


