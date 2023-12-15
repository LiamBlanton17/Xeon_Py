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
    castlingRights = 1111 #Castleing rights, WShort, WLong, BShort, BLong

    # Constructor
    def __init__(self, board, turn, castlingRights, boardHistory):
        self.turn = turn  # Who's turn is it
        self.castlingRights = list(castlingRights)
        self.board = board.copy()  # Setting the board of the object (2d array of pieces)
        self.moves = self.generateMoves(boardHistory, False)  # Generate moves from current board

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
    def generateMoves(self, bHistory, killCastle):
        moves = []
        #Loop over each piece in the board
        for row in range(8):
            for col in range(8):
                #Make sure it is current players turn
                if (self.turn == 'white' and self.board[row][col].material < 0) or (self.turn == 'black' and self.board[row][col].material > 0):
                    continue
                moves.extend(self.board[row][col].getMoves(self.board, row, col))
        #Check for castling
        if not killCastle:
            if self.turn == 'white':
                #White short
                if self.castlingRights[0] == '1' and self.board[0][5].material == 0 and self.board[0][6].material == 0:
                    #Below should check to see if the king is in or moving through check
                    testB = copy.deepcopy(self)  # Create a copy of the current board
                    testB.turn = 'black'  # Set this copy to the opponent
                    opponentMoves = testB.generateMoves(bHistory, True)  # See where opponents pieces can move it
                    #Loop through and parse out the moves to only get the target square
                    i = 0
                    for move in opponentMoves:
                        move //= 100
                        opponentMoves[i] = move
                        i += 1
                    #Determine if the king will move through check
                    moveThroughCheck = False
                    for move in opponentMoves:
                        if move == 40 or move == 50 or move == 60:
                            moveThroughCheck = True
                    if not moveThroughCheck:
                        moves.extend([8880])
                #White Long
                if self.castlingRights[1] == '1' and self.board[0][3].material == 0 and self.board[0][2].material == 0 and self.board[0][1] == 0:
                    #Below should check to see if the king is in or moving through check
                    testB = copy.deepcopy(self)  # Create a copy of the current board
                    testB.turn = 'black'  # Set this copy to the opponent
                    opponentMoves = testB.generateMoves(bHistory, True)  # See where opponents pieces can move it
                    #Loop through and parse out the moves to only get the target square
                    i = 0
                    for move in opponentMoves:
                        move //= 100
                        opponentMoves[i] = move
                        i += 1
                    #Determine if the king will move through check
                    moveThroughCheck = False
                    for move in opponentMoves:
                        if move == 40 or move == 30 or move == 20:
                            moveThroughCheck = True
                    if not moveThroughCheck:
                        moves.extend([8881])
            if self.turn == 'black':
                #Black short
                if self.castlingRights[2] == '1' and self.board[7][5].material == 0 and self.board[7][6].material == 0:
                    #Below should check to see if the king is in or moving through check
                    testB = copy.deepcopy(self)  # Create a copy of the current board
                    testB.turn = 'white'  # Set this copy to the opponent
                    opponentMoves = testB.generateMoves(bHistory, True)  # See where opponents pieces can move it
                    #Loop through and parse out the moves to only get the target square
                    i = 0
                    for move in opponentMoves:
                        move //= 100
                        opponentMoves[i] = move
                        i += 1
                    #Determine if the king will move through check
                    moveThroughCheck = False
                    for move in opponentMoves:
                        if move == 47 or move == 57 or move == 67:
                            moveThroughCheck = True
                    if not moveThroughCheck:
                        moves.extend([9990])
                #Black Long
                if self.castlingRights[3] == '1' and self.board[7][3].material == 0 and self.board[7][2].material == 0 and self.board[7][1] == 0:
                    #Below should check to see if the king is in or moving through check
                    testB = copy.deepcopy(self)  # Create a copy of the current board
                    testB.turn = 'white'  # Set this copy to the opponent
                    opponentMoves = testB.generateMoves(bHistory, True)  # See where opponents pieces can move it
                    #Loop through and parse out the moves to only get the target square
                    i = 0
                    for move in opponentMoves:
                        move //= 100
                        opponentMoves[i] = move
                        i += 1
                    #Determine if the king will move through check
                    moveThroughCheck = False
                    for move in opponentMoves:
                        if move == 47 or move == 37 or move == 27:
                            moveThroughCheck = True
                    if not moveThroughCheck:
                        moves.extend([9991])

        #Remove moves resulting in check
        #Check for 3fold, check for 50move
        #Check for mate
        return moves

    # Method to update the board
    def updateBoard(self, move, bHistory):

        #Add the previous board to board history
        bHistory.append(copy.deepcopy(self))

        #If it's a special move
        if move == 8880:  # White, Short Castle
            self.board[0][6] = self.board[0][4]
            self.board[0][5] = self.board[0][7]
            self.board[0][4] = Empty()
            self.board[0][7] = Empty()
        elif move == 8881:  # White, Long Castle
            self.board[0][2] = self.board[0][4]
            self.board[0][3] = self.board[0][0]
            self.board[0][4] = Empty()
            self.board[0][0] = Empty()
        elif move == 9990:  # Black, Short Castle
            self.board[7][6] = self.board[7][4]
            self.board[7][5] = self.board[7][7]
            self.board[7][4] = Empty()
            self.board[7][7] = Empty()
        elif move == 9991:  # Black, Long Castle
            self.board[7][2] = self.board[7][4]
            self.board[7][3] = self.board[7][0]
            self.board[7][4] = Empty()
            self.board[7][0] = Empty()
        else:
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

        #Update castling rights
        if self.board[0][4].char != 'K':
            self.castlingRights[0] = 0
            self.castlingRights[1] = 0
        if self.board[0][0].char != 'R':
            self.castlingRights[1] = 0
        if self.board[0][7].char != 'R':
            self.castlingRights[0] = 0
        if self.board[7][4].char != 'k':
            self.castlingRights[2] = 0
            self.castlingRights[3] = 0
        if self.board[7][0].char != 'r':
            self.castlingRights[3] = 0
        if self.board[7][7].char != 'r':
            self.castlingRights[2] = 0


        #Clear all the moves, and generate the next moves
        self.moves.clear()
        self.moves = self.generateMoves(bHistory, False)
