# Board Class
import copy

# Import all other classes
import Empty
from Empty import *

# Class
class Board:

    # Variables
    eval = 0  # Evaluation of board
    material = 0  # Material on the board

    # Constructor
    def __init__(self, board, turn):
        self.turn = turn  # Who's turn is it
        self.board = board.copy()  # Setting the board of the object (2d array of pieces)
        self.moves = self.generateMoves()  # Generate moves from current board

    # Method to print the board to the console
    # TO DO: Swap which way it prints depending on who's move it is
    def PrintBoard(self):
        for row in range(7, -1, -1):
            print(row+1, end=" ")
            for col in range(8):
                print(self.board[row][col].char, end=" ")
            print()
        print("  A B C D E F G H")
        print()

    # Method to get material of the board
    def getMaterial(self):
        val = 0
        for row in range(8):
            for col in range(8):
                val += self.board[row][col].material
        return val

    # Method to get evaluation of the board
    def getEval(self):
        val = 0
        for row in range(8):
            for col in range(8):
                val += self.board[row][col].value
        return val

    # Method to generate move, children board pairs
    def generateMoves(self):
        moves = []
        #Loop over each piece in the board
        for row in range(8):
            for col in range(8):
                #Make sure it is current players turn
                if (self.turn == 'white' and self.board[row][col].material < 0) or (self.turn == 'black' and self.board[row][col].material > 0):
                    continue
                moves.extend(self.board[row][col].getMoves(self.board, row, col))
        #Remove moves resulting in check
        #Check for 3fold, check for 50move
        #Check for mate
        return moves

    # Method to update the board
    def updateBoard(self, move, bHistory):

        #Add the previous board to board history
        bHistory.append(copy.deepcopy(self))

        #Parse out the move input
        sRow = move % 10
        move //= 10
        sCol = move % 10
        move //= 10
        nRow = move % 10
        move //= 10
        nCol = move

        #Make the move
        self.board[nRow][nCol] = self.board[sRow][sCol]
        self.board[sRow][sCol] = Empty()

        #Set turn to opposite of current turn
        if self.turn == 'white':
            self.turn = 'black'
        else:
            self.turn = 'white'

        #Clear all the moves, and generate the next moves
        self.moves.clear()
        self.moves = self.generateMoves()
