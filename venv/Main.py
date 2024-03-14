# Main Class
import copy
import sys
import timeit

# Import all other classes
# import Board, wKing, wQueen, wRook, wBishop, wKnight, wPawn, bKing, bQueen, bRook, bBishop, bKnight, bPawn, Empty
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
from Xeon import *

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
def mainLoop():
    while (500 > mainBoard.eval > -500) and len(mainBoard.moves) > 0:
        for i in range(25):  # Used to format the game loop
            print()
        print("-------------------------------------- ")
        mainBoard.PrintBoard()
        print("EVAL: ", mainBoard.getEval())
        print("--------------------------------------")
        # Right now you only play as white
        if mainBoard.turn == "white":
            move = takeUIn(mainBoard)
        else:
            move = XeonMove(mainBoard, boardHistory)
        if move == 9999:  # Debugging statement, code 9999 to draw game
            break
        mainBoard.updateBoard(move, boardHistory, True, True)

    print("GG")

import cProfile
from pympler.tracker import SummaryTracker
#tracker = SummaryTracker()
cProfile.run("mainLoop()")
#mainLoop()
#tracker.print_diff()
