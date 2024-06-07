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
        self.board = board  # Setting the board of the object (2d array of pieces)
        self.touchMoves()
        #Update material
        # self.setMaterial()
        if genMoves:
            self.moves = self.generateMoves(boardHistory, False, False)  # Generate moves from current board

    def testFunction(self, boardHistory):
        self.generateMoves(boardHistory, False, False)

    # Method to get the board
    def GetBoard(self):
        return self.board

    # Method to print the board to the console
    # TO DO: Swap which way it prints depending on who's move it is
    def PrintBoard(self):
        if self.turn == 'white':
            for row in range(7, -1, -1):
                print(row+1, end=" ")
                for col in range(8):
                    print(self.board[row][col].char, end=" ")
                print()
            print("  A B C D E F G H")
        else:
            for row in range(8):
                print(row+1, end=" ")
                for col in range(8):
                    print(self.board[row][col].char, end=" ")
                print()
            print("  A B C D E F G H")
        print()

    # Method to get material of the board
    def getMaterial(self):
        return self.material

    def setMaterial(self):
        self.material = 0
        for row in range(8):
            for col in range(8):
                self.material += self.board[row][col].material

    # Method to get evaluation of the board
    def getEval(self, move_number):
        phase_of_game = 'opening'
        if move_number > 10:
            phase_of_game = 'middle_game'
        if self.getNumPieces() <= 12:
            phase_of_game = 'endgame'
        eval = 0
        # col by row search (to search row by col inverse row and col
        for row in range(8):
            # These are all per FILE (ie col)
            wPawns = 0
            bPawns= 0
            wRooks = 0
            bRooks = 0
            wKing = 0
            bKing = 0
            wQueen = 0
            bQueen = 0
            for col in range(8):
                pieceByFile = self.board[col][row].char  # Get char of piece of current square (inverted)
                eval += self.board[row][col].getEval(row, col, phase_of_game)  # Isolated piece evaluation based on PSTs
                eval += self.board[row][col].material  # Basic material evaluation
                # Use below if/elifs to get profile of the file (we got piece by inverting row/col)
                if pieceByFile == '-':
                    pass
                elif pieceByFile == 'P':
                    wPawns += 1
                elif pieceByFile == 'p':
                    bPawns += 1
                elif pieceByFile == 'R':
                    wRooks += 1
                elif pieceByFile == 'r':
                    bRooks += 1
                elif pieceByFile == 'K':
                    wKing += 1
                elif pieceByFile == 'k':
                    bKing += 1
                elif pieceByFile == 'Q':
                    wQueen += 1
                elif pieceByFile == 'q':
                    bQueen += 1
            # We have profiled the file, now compute logic
            if wPawns > 1:  # If doubled white pawns, change eval by -0.35
                eval += -0.35
            if bPawns > 1:  # If doubled black pawns, change eval by 0.35
                eval += 0.35
            if wPawns + bPawns == 0:  # If the file is open (no pawns)
                eval += (wRooks - bRooks) * 0.35  # Every unmatched rook on open file is change of 0.35
                if bKing == 1 and wRooks > 0:  # If white rooks on open file and bKing, massive bonus to white
                    eval += 0.85
                if wKing == 1 and bRooks > 0:  # If black rooks on open file and wKing, massive bonus to black
                    eval += -0.85
                if bQueen == 1 and wRooks > 0:  # If white rooks on open file and bQueen, massive bonus to white
                    eval += 0.6
                if wQueen == 1 and bRooks > 0:  # If black rooks on open file and wQueen, massive bonus to black
                    eval += -0.6
            elif wPawns + bPawns == 1:  # If file is semi-open (only one pawn)
                eval += (wRooks - bRooks) * 0.15  # Every unmatched rook on open file is change of 0.15
                if bKing == 1 and wRooks > 0:  # If white rooks on semi-open file and bKing, strong bonus to white
                    eval += 0.35
                if wKing == 1 and bRooks > 0:  # If black rooks on semi-open file and wKing, strong bonus to black
                    eval += -0.35
                if bQueen == 1 and wRooks > 0:  # If white rooks on semi-open file and bQueen, strong bonus to white
                    eval += 0.15
                if wQueen == 1 and bRooks > 0:  # If black rooks on semi-open file and wQueen, strong bonus to black
                    eval += -0.15

        # Loop through central 16 squares, count pawns, give +/- 0.18 for difference, 1.65 per pawn in center 4
        centerPawns = 0
        for row in range(2, 6):
            for col in range(2, 6):
                if self.board[row][col].char == 'P':
                    centerPawns += 1
                    if 2 < row < 6 and 2 < col < 6:
                        centerPawns += 0.65
                if self.board[row][col].char == 'p':
                    centerPawns -= 1
                    if 2 < row < 6 and 2 < col < 6:
                        centerPawns -= 0.65
        eval += centerPawns * 0.18
        # Some more eval ideas
        # Pieces of both colors around both kings
        # Slight penalty for undefended minor pieces
        # Piece mobility
        # Pawn mobility
        # Decrease value of knight as pawns disappear, increase value of bishop/rook
        return eval

    # Method to generate move, children board pairs
    def generateMoves(self, bHistory, killCastleCheck, onlyCaptures):
        moves = []

        #Loop over each piece in the board
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                #Make sure it is current players turn
                if (self.turn == 'white' and piece.material < 0) or (self.turn == 'black' and piece.material > 0) or piece.material == 0:
                    continue
                moves.extend(piece.getMoves(self.board, row, col))
                #Pawn Enpassant
                if (piece.char == 'P' or self.board[row][col].char == 'p') and len(bHistory) > 0 and (row == 3 or row == 4):
                    moves.extend(piece.enpassent(self.board, row, col, len(bHistory), DeHashBoard(bHistory[len(bHistory)-1])))

        #Only keep captures if wanted
        if onlyCaptures:
            w = 0
            for move in moves:
                tmove = move // 100
                trow = tmove % 10
                tmove //= 10
                tcol = tmove
                if not (0 <= tcol <= 7 and 0 <= trow <= 7):
                    continue
                if self.turn == 'white' and self.board[trow][tcol].material < 0:
                    continue
                elif self.turn == 'black' and self.board[trow][tcol].material > 0:
                    continue
                else:
                    moves[w] = 0
                w += 1
            moves = [i for i in moves if i != 0]

        #Check for castling
        if not killCastleCheck:
            # Create a testB with deep copys of the original board position, hash the current board
            hashedBoard = HashBoard(self)
            testB = Board(DeHashBoard(hashedBoard), self.turn, self.castlingRights, bHistory, False)
            if self.turn == 'white' and ((self.castlingRights[0] == '1' and self.board[0][5].material == 0 and self.board[0][6].material == 0) or (self.castlingRights[1] == '1' and self.board[0][3].material == 0 and self.board[0][2].material == 0 and self.board[0][1].material == 0)):
                # Test is opponent checks the king or attacks the squares
                testB.turn = 'black'  # Set this copy to the opponent
                opponentMoves = testB.generateMoves(bHistory, True, False)  # See where opponents pieces can move it
                #Loop through and parse out the moves to only get the target square
                #Determine if the king will move through check
                kingSideIllegal = False
                queenSideIllegal = False
                opponentMoves = [i for i in opponentMoves if i % 10 == 0]
                for move in opponentMoves:
                    move //= 100
                    if move == 40 or move == 50 or move == 60:
                        kingSideIllegal = True
                    if move == 40 or move == 30 or move == 20:
                        queenSideIllegal = True
                    if kingSideIllegal and queenSideIllegal:
                        break
                #White short
                if self.castlingRights[0] == '1' and self.board[0][5].material == 0 and self.board[0][6].material == 0 and not kingSideIllegal:
                    moves.extend([8880])
                #White Long
                if self.castlingRights[1] == '1' and self.board[0][3].material == 0 and self.board[0][2].material == 0 and self.board[0][1].material == 0 and not queenSideIllegal:
                    moves.extend([8881])
            if self.turn == 'black' and ((self.castlingRights[2] == '1' and self.board[7][5].material == 0 and self.board[7][6].material == 0) or (self.castlingRights[3] == '1' and self.board[7][3].material == 0 and self.board[7][2].material == 0 and self.board[7][1].material == 0)):
                # Test is opponent checks the king or attacks the squares
                #Below should check to see if the king is in or moving through check
                testB.board = DeHashBoard(hashedBoard)  # Reset testB
                testB.turn = 'white'  # Set this copy to the opponent
                opponentMoves = testB.generateMoves(bHistory, True, False)  # See where opponents pieces can move it
                #Loop through and parse out the moves to only get the target square
                #Determine if the king will move through check
                kingSideIllegal = False
                queenSideIllegal = False
                opponentMoves = [i for i in opponentMoves if i % 10 == 7]
                for move in opponentMoves:
                    move //= 100
                    if move == 47 or move == 57 or move == 67:
                        kingSideIllegal = True
                        break
                    if move == 47 or move == 37 or move == 27:
                        queenSideIllegal = True
                    if kingSideIllegal and queenSideIllegal:
                        break
                #Black short
                if self.castlingRights[2] == '1' and self.board[7][5].material == 0 and self.board[7][6].material == 0 and not kingSideIllegal:
                    moves.extend([9990])
                #Black Long
                if self.castlingRights[3] == '1' and self.board[7][3].material == 0 and self.board[7][2].material == 0 and self.board[7][1].material == 0 and not queenSideIllegal:
                    moves.extend([9991])
            #See if king is in check after a move, and prune it
            # Loop through the current moves, create a new board object for each
            i = 0
            for move in moves:
                testB.board = DeHashBoard(hashedBoard)  # Reset testB
                testB.turn = self.turn
                testB.updateBoard(move, bHistory, False, False)
                nextMoves = testB.generateMoves(bHistory, True, False)
                moves[i] = self.isKingInCheck(testB, move, nextMoves)
                i += 1

            #List compression, remove all the 0s
            moves = [i for i in moves if i != 0]

        return moves

    # Check if the king is in check
    def isKingInCheck(self, testB, move, nextMoves):
        for nmove in nextMoves:
            nmove //= 100
            row = nmove % 10
            nmove //= 10
            col = nmove
            if (testB.board[row][col].char == "K" and testB.turn == 'black') or (testB.board[row][col].char == "k" and testB.turn == 'white'):
                return 0
        return move

    # Method used in seeing if the king is in check, all it does is create a moves list variable
    # This avoids recursion errors
    def touchMoves(self):
        self.moves = []

    # Method to update the board
    def updateBoard(self, move, bHistory, generateMoves, updateBHistory):
        #Add the previous board to board history
        if updateBHistory:
            bHistory.append(HashBoard(self))

        #Get the current material
        currentMaterial = self.getMaterial()
        nRow = 0  # Needed for references
        nCol = 0  # Needed for references

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

        #Update material
        if updateBHistory:
            self.setMaterial()

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
        if len(bHistory) > 3 and updateBHistory:
            matches = 1
            for i in range(len(bHistory)):
                matches += Board.CompareBoards(DeHashBoard(bHistory[i]), self.board)
            if matches == 3:
                self.moves.clear()

        # Check for promotion
        if nRow == 7:
            if self.board[nRow][nCol].material == 1:  # White
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
        if nRow == 0:
            if self.board[nRow][nCol].material == -1:  # Black
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

    # Return a list of hashed children boards
    def GetChildren(self, bHistory, K1, K2, K3, coMoves, pcoMoves, capture_depth):
        cutoff_moves = coMoves | pcoMoves
        Children = []
        hashedBoard = HashBoard(self)
        testB = Board(DeHashBoard(hashedBoard), self.turn, self.castlingRights, bHistory, False)
        holdTurn = self.turn
        # Sort the moves, right now only sorts captures to top and killer moves, put pawn moves at back
        moves = self.moves
        if capture_depth == 0:
            i = 0
            for j in range(len(moves)):
                if moves[j] == K1:
                    moves[i], moves[j] = moves[j], moves[i]
                    i += 1
                    continue
                if moves[j] == K2:
                    moves[i], moves[j] = moves[j], moves[i]
                    i += 1
                    continue
                if moves[j] == K3:
                    moves[i], moves[j] = moves[j], moves[i]
                    i += 1
                    continue
                tmove = moves[j] // 100
                trow = tmove % 10
                tmove //= 10
                tcol = tmove
                if not (0 <= tcol <= 7 and 0 <= trow <= 7):
                    continue
                if self.turn == 'white' and self.board[trow][tcol].material < 0:
                    moves[i], moves[j] = moves[j], moves[i]
                    i += 1
                elif self.turn == 'black' and self.board[trow][tcol].material > 0:
                    moves[i], moves[j] = moves[j], moves[i]
                    i += 1
            # For non-captures and non-killers, order by cutoffs if possible
            ogi = i  # Hold original i value
            for k in range(i, len(moves)):
                if moves[k] in cutoff_moves:
                    moves[i], moves[k] = moves[k], moves[i]
                    for j in range(i, ogi, -1):  # Order moves by cutoff value
                        if cutoff_moves[moves[j]] > cutoff_moves[moves[j-1]]:
                            moves[j-1], moves[j] = moves[j], moves[j-1]
                        else:
                            break
                    i += 1
                    continue
            # Look at castling next
            for k in range(i, len(moves)):
                if moves[k] == 8880 or moves[k] == 8881 or moves[k] == 9990 or moves[k] == 9991:
                    moves[i], moves[k] = moves[k], moves[i]
                    i += 1
        for move in moves:
            testB.board = DeHashBoard(hashedBoard)  # Reset testB
            testB.turn = holdTurn
            testB.updateBoard(move, bHistory, False, False)
            Children.append([HashBoard(testB), move])
        return Children

    # Return a list of hashed children boards, plus the resulting move
    # Old get children method, not in use anymore
    def GetMainChildren(self, bHistory):
        Children = []
        hashedBoard = HashBoard(self)
        testB = Board(DeHashBoard(hashedBoard), self.turn, self.castlingRights, bHistory, False)
        holdTurn = self.turn
        # Sort the moves, right now only sorts captures to top
        moves = self.moves
        i = 0
        for j in range(len(moves)):
            tmove = moves[j] // 100
            trow = tmove % 10
            tmove //= 10
            tcol = tmove
            if not (0 <= tcol <= 7 and 0 <= trow <= 7):
                continue
            if self.turn == 'white' and self.board[trow][tcol].material < 0:
                moves[i], moves[j] = moves[j], moves[i]
                i += 1
            elif self.turn == 'black' and self.board[trow][tcol].material > 0:
                moves[i], moves[j] = moves[j], moves[i]
                i += 1
        for move in moves:
            testB.board = DeHashBoard(hashedBoard)  # Reset testB
            testB.turn = holdTurn
            testB.updateBoard(move, bHistory, False, False)
            Children.append([HashBoard(testB), move])
        return Children

    def getNumPieces(self):
        count = 0
        for row in range(8):
            for col in range(8):
                if self.board[row][col].char != '-':
                    count += 1
        return count
