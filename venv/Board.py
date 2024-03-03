# Board Class
import copy

# Import all other classes
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
from Hash import *

# Class
class Board:

    # Variables
    fiftyMoves = 0  # 50 move counter
    eval = 0  # Evaluation of board
    material = 0  # Material on the board
    castlingRights = 1111  # Castling rights, WShort, WLong, BShort, BLong

    # Constructor
    def __init__(self, board, turn, castlingRights, boardHistory, genMoves):
        self.turn = turn  # Who's turn is it
        self.castlingRights = list(castlingRights)
        self.board = board.copy()  # Setting the board of the object (2d array of pieces)
        self.boardHistory = boardHistory
        self.touchMoves()
        if genMoves:
            self.moves = self.generateMoves(self.boardHistory, False, False)  # Generate moves from current board

    # Method to get the board
    def GetBoard(self):
        return self.board

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
    def generateMoves(self, bHistory, killCastle, killCheck):
        moves = []
        wKPos = 0
        bKPos = 0
        #Loop over each piece in the board
        for row in range(8):
            for col in range(8):
                #Make sure it is current players turn
                if (self.turn == 'white' and self.board[row][col].material < 0) or (self.turn == 'black' and self.board[row][col].material > 0):
                    continue
                moves.extend(self.board[row][col].getMoves(self.board, row, col))
                #Pawn Enpassant
                if (self.board[row][col].char == 'P' or self.board[row][col].char == 'p') and len(bHistory) > 0:
                    moves.extend(self.board[row][col].enpassent(self.board, row, col, len(bHistory), DeHashBoard(bHistory[len(bHistory)-1], bHistory)))
        # Create a testB with deep copys of the original board position
        testB = Board(copy.deepcopy(self.board), copy.deepcopy(self.turn), copy.deepcopy(self.castlingRights), bHistory, False)
        #Check for castling
        if not killCastle:
            if self.turn == 'white':
                #White short
                if self.castlingRights[0] == '1' and self.board[0][5].material == 0 and self.board[0][6].material == 0:
                    #Below should check to see if the king is in or moving through check
                    # testB = copy.deepcopy(self)  # Create a copy of the current board
                    testB.turn = 'black'  # Set this copy to the opponent
                    opponentMoves = testB.generateMoves(bHistory, True, True)  # See where opponents pieces can move it
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
                    testB.board = copy.deepcopy(self.board)  # Create a copy of the current board
                    testB.turn = 'black'  # Set this copy to the opponent
                    opponentMoves = testB.generateMoves(bHistory, True, True)  # See where opponents pieces can move it
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
                    testB.board = copy.deepcopy(self.board)  # Create a copy of the current board
                    testB.turn = 'white'  # Set this copy to the opponent
                    opponentMoves = testB.generateMoves(bHistory, True, True)  # See where opponents pieces can move it
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
                    testB.board = copy.deepcopy(self.board)  # Create a copy of the current board
                    testB.turn = 'white'  # Set this copy to the opponent
                    opponentMoves = testB.generateMoves(bHistory, True, True)  # See where opponents pieces can move it
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
        #See if king is in check after a move, and prune it
        if not killCheck:
            # Loop through the current moves, create a new board object for each
            i = 0
            for move in moves:
                moves[i] = self.isKingInCheck(move, bHistory)
                i += 1

        #List compression, remove all the 0s
        moves = [i for i in moves if i != 0]
        return moves

    # Check if the king is in check
    def isKingInCheck(self, move, bHistory):
        testB = Board(copy.deepcopy(self.board), copy.deepcopy(self.turn), copy.deepcopy(self.castlingRights), bHistory, False)
        testB.updateBoard(move, bHistory, False)
        nextMoves = testB.generateMoves(bHistory, True, True)
        holdTestB = copy.deepcopy(testB)
        for nmove in nextMoves:
            testB = copy.deepcopy(holdTestB)
            testB.updateBoard(nmove, bHistory, False)
            # testB.PrintBoard()
            if not (500 > testB.getEval() > -500):
                return 0
        return move

    # Method used in seeing if the king is in check, all it does is create a moves list variable
    # This avoids recursion errors
    def touchMoves(self):
        self.moves = []

    # Method to update the board
    def updateBoard(self, move, bHistory, generateMoves):
        #Add the previous board to board history
        if generateMoves:
            bHistory.append(HashBoard(self))

        #Get the current material
        currentMaterial = self.getMaterial()
        nRow = 0 # Needed for references
        nCol = 0 # Needed for references

        #If it's a special move
        if move == 8880:  # White, Short Castle
            self.board[0][6] = self.board[0][4]
            self.board[0][5] = self.board[0][7]
            self.board[0][4] = Empty()
            self.board[0][7] = Empty()
            self.fiftyMoves = 0
        elif move == 8881:  # White, Long Castle
            self.board[0][2] = self.board[0][4]
            self.board[0][3] = self.board[0][0]
            self.board[0][4] = Empty()
            self.board[0][0] = Empty()
            self.fiftyMoves = 0
        elif move == 9990:  # Black, Short Castle
            self.board[7][6] = self.board[7][4]
            self.board[7][5] = self.board[7][7]
            self.board[7][4] = Empty()
            self.board[7][7] = Empty()
            self.fiftyMoves = 0
        elif move == 9991:  # Black, Long Castle
            self.board[7][2] = self.board[7][4]
            self.board[7][3] = self.board[7][0]
            self.board[7][4] = Empty()
            self.board[7][0] = Empty()
            self.fiftyMoves = 0
        else:
            #Parse out the move input
            sRow = move % 10
            move //= 10
            sCol = move % 10
            move //= 10
            nRow = move % 10
            move //= 10
            nCol = move
            #Check for 50 move incrementation
            if self.board[sRow][sCol].material == 1 or self.board[sRow][sCol].material == -1:
                self.fiftyMoves = 0
            #Now check for enpassent
            if sCol != nCol and (self.board[sRow][sCol].material == 1 or self.board[sRow][sCol].material == -1):
                if self.board[sRow][sCol].material == 1 and self.board[nRow][nCol].material == 0:  # White
                    self.board[nRow-1][nCol] = Empty()
                if self.board[sRow][sCol].material == -1 and self.board[nRow][nCol].material == 0:  # Black
                    self.board[nRow+1][nCol] = Empty()
            #Make the move
            self.board[nRow][nCol] = self.board[sRow][sCol]
            self.board[sRow][sCol] = Empty()

        #If material is different, then reset 50 moves
        if self.getMaterial() != currentMaterial:
            self.fiftyMoves = 0

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
        if generateMoves:
            self.moves = self.generateMoves(bHistory, False, False)

        #Check for 50 moves
        if self.fiftyMoves >= 50:
            self.moves.clear()

        #Check for 3-Fold repetition
        if len(bHistory) > 3:
            matches = 1
            for i in range(len(bHistory)):
                matches += Board.CompareBoards(DeHashBoard(bHistory[i], bHistory), self.board)
            if matches == 3:
                self.moves.clear()

        # Check for promotion
        for i in range(8):
            if self.board[7][i].material == 1:  # White
                # Promotion
                piece = self.wPromote()
                if piece == "Q":
                    self.board[nRow][nCol] = wQueen()
                if piece == "R":
                    self.board[nRow][nCol] = wRook()
                if piece == "B":
                    self.board[nRow][nCol] = wBishop()
                if piece == "N":
                    self.board[nRow][nCol] = wKnight()
                break
            if self.board[0][i].material == -1:  # Black
                # Promotion
                piece = self.bPromote()
                if piece == "q":
                    self.board[nRow][nCol] = bQueen()
                if piece == "r":
                    self.board[nRow][nCol] = bRook()
                if piece == "b":
                    self.board[nRow][nCol] = bBishop()
                if piece == "n":
                    self.board[nRow][nCol] = bKnight()
                break
        # Increment 50 moves
        self.fiftyMoves += 1

    # White promotion
    def wPromote(self):
        return "Q"  # Temp fix to auto promote to a queen
        uIn = input("[WHITE] Pawn Promotion (Q, R, B, N): ")
        if uIn == "Q" or uIn == "R" or uIn == "B" or uIn == "N":
            return uIn
        print("Not a valid piece.")
        return self.wPromote()

    # Black promotion
    def bPromote(self):
        return "q"  # Temp fix to auto promote to a queen
        uIn = input("[BLACK] Pawn Promotion (q, r, b, n): ")
        if uIn == "q" or uIn == "r" or uIn == "b" or uIn == "n":
            return uIn
        print("Not a valid piece.")
        return self.bPromote()

    # Tests if two boards are equal, returns 0 if they are not and 1 if they are
    def CompareBoards(BoardOne, BoardTwo):
        row = 0
        while row <= 7:
            col = 0
            while col <= 7:
                if not (BoardOne[row][col].char == BoardTwo[row][col].char):
                    return 0
                col += 1
            row += 1
        return 1
