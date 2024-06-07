# Main Class
import copy
import sys
import time
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

testBoard = [[wRook(), wKnight(), wBishop(), wQueen(), wKing(), wBishop(), Empty(), wRook()],
             [wPawn(), wPawn(), wPawn(), wPawn(), Empty(), wPawn(), wPawn(), wPawn()],
             [Empty(), Empty(), Empty(), Empty(), Empty(), wKnight(), Empty(), Empty()],
             [Empty(), Empty(), Empty(), Empty(), wPawn(), Empty(), Empty(), Empty()],
             [Empty(), Empty(), Empty(), Empty(), bPawn(), Empty(), Empty(), Empty()],
             [Empty(), Empty(), bKnight(), Empty(), Empty(), Empty(), Empty(), Empty()],
             [bPawn(), bPawn(), bPawn(), bPawn(), bPawn(), bPawn(), bPawn(), bPawn()],
             [bRook(), Empty(), bBishop(), bQueen(), bKing(), bBishop(), bKnight(), bRook()]]


#Board history list
boardHistory = []

#Create the main Board object
mainBoard = Board(startingBoard, 'white', '1111', boardHistory, True)

import cProfile
# Loop
def mainLoop():
    xeonEval = 0
    playerTurn = input("Which color would you like? ('white' or 'black' or 'AI' or 'USER'): ")
    while (500 > mainBoard.getMaterial() > -500) and len(mainBoard.moves) > 0:
        for i in range(25):  # Used to format the game loop
            print()
        print("-------------------------------------- ")
        mainBoard.PrintBoard()
        print("EVAL: ", xeonEval)
        # print("MOVES: ", mainBoard.moves)
        print("--------------------------------------")
        if playerTurn == 'AI':
            time.sleep(3)
        if mainBoard.turn == playerTurn or playerTurn == 'USER':
            move = takeUIn(mainBoard, mainBoard.turn)
        else:
            #move = takeUIn(mainBoard)
            results = XeonMove(mainBoard, boardHistory)
            move = results[0]
            xeonEval = results[1]
        if move == 9999:  # Debugging statement, code 9999 to draw game
            break
        mainBoard.updateBoard(move, boardHistory, True, True)

    print("GG")

from pympler.tracker import SummaryTracker
tracker = SummaryTracker()
cProfile.run("mainLoop()")
tracker.print_diff()

#mainLoop()
