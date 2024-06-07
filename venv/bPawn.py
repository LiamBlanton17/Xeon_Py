# Class for the Black Pawn

class bPawn:

    #Variables
    material = -1 #Value of material
    value = -1 #Fluid value of the piece
    char = 'p' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Piece-Square map multiplier (used in isolated evaluation of pieces)
    opening = {
        56: +0.00, 57: +0.00, 58: +0.00, 59: +0.00, 60: +0.00, 61: +0.00, 62: +0.00, 63: +0.00,
        48: +0.00, 49: +0.00, 50: -0.05, 51: -0.25, 52: -0.25, 53: +0.10, 54: +0.05, 55: +0.00,
        40: +0.05, 41: +0.05, 42: +0.10, 43: +0.10, 44: +0.10, 45: -0.15, 46: +0.00, 47: +0.05,
        32: +0.05, 33: +0.05, 34: +0.20, 35: +0.25, 36: +0.25, 37: -0.05, 38: -0.05, 39: -0.05,
        24: +0.10, 25: +0.05, 26: +0.25, 27: +0.30, 28: +0.30, 29: +0.00, 30: -0.05, 31: +0.00,
        16: +0.00, 17: +0.05, 18: +0.20, 19: +0.25, 20: +0.25, 21: +0.15, 22: +0.05, 23: +0.00,
        8: +0.10, 9: +0.15, 10: +0.30, 11: +0.30, 12: +0.30, 13: +0.25, 14: +0.15, 15: +0.15,
        0: +5.00, 1: +5.00, 2: +5.00, 3: +5.00, 4: +5.00, 5: +5.00, 6: +5.00, 7: +5.00
    }

    middle_game = {
        56: +0.00, 57: +0.00, 58: +0.00, 59: +0.00, 60: +0.00, 61: +0.00, 62: +0.00, 63: +0.00,
        48: +0.00, 49: +0.00, 50: -0.05, 51: -0.35, 52: -0.35, 53: +0.10, 54: +0.10, 55: +0.05,
        40: +0.00, 41: +0.00, 42: +0.05, 43: +0.15, 44: +0.15, 45: -0.15, 46: +0.10, 47: +0.10,
        32: +0.05, 33: +0.05, 34: +0.15, 35: +0.25, 36: +0.25, 37: +0.00, 38: +0.00, 39: +0.05,
        24: +0.15, 25: +0.15, 26: +0.20, 27: +0.30, 28: +0.30, 29: +0.05, 30: +0.00, 31: +0.10,
        16: +0.20, 17: +0.20, 18: +0.25, 19: +0.35, 20: +0.35, 21: +0.10, 22: +0.10, 23: +0.15,
        8: +0.30, 9: +0.30, 10: +0.35, 11: +0.45, 12: +0.45, 13: +0.25, 14: +0.25, 15: +0.25,
        0: +5.00, 1: +5.00, 2: +5.00, 3: +5.00, 4: +5.00, 5: +5.00, 6: +5.00, 7: +5.00
    }

    endgame = {
        56: +0.00, 57: +0.00, 58: +0.00, 59: +0.00, 60: +0.00, 61: +0.00, 62: +0.00, 63: +0.00,
        48: -0.05, 49: -0.05, 50: -0.05, 51: -0.05, 52: -0.05, 53: -0.05, 54: -0.05, 55: -0.05,
        40: +0.00, 41: +0.00, 42: +0.00, 43: +0.00, 44: +0.00, 45: +0.00, 46: +0.00, 47: +0.00,
        32: +0.10, 33: +0.10, 34: +0.05, 35: +0.05, 36: +0.05, 37: +0.05, 38: +0.10, 39: +0.10,
        24: +0.20, 25: +0.20, 26: +0.10, 27: +0.10, 28: +0.10, 29: +0.10, 30: +0.20, 31: +0.20,
        16: +0.30, 17: +0.30, 18: +0.20, 19: +0.20, 20: +0.20, 21: +0.20, 22: +0.30, 23: +0.30,
        8: +0.55, 9: +0.55, 10: +0.40, 11: +0.40, 12: +0.40, 13: +0.40, 14: +0.55, 15: +0.55,
        0: +5.00, 1: +5.00, 2: +5.00, 3: +5.00, 4: +5.00, 5: +5.00, 6: +5.00, 7: +5.00
    }

    #Return the pieces character
    def GetChar(self):
        return self.char

    #Method to get an isolated eval of this piece
    def getEval(self, row, col, phase_of_game):
        if phase_of_game == 'middle_game':
            return (self.middle_game[(row*8)+col] * -1) - 1
        elif phase_of_game == 'endgame':
            return (self.endgame[(row*8)+col] * -1) - 1
        return (self.opening[(row*8)+col] * -1) - 1

    #Get Moves method
    def getMoves(self, board, cRow, cCol):
        moves = []

        #If on starting row, add a double move, if possible
        if cRow == 6:
            if board[5][cCol].material == 0 and board[4][cCol].material == 0:
                moves.append(cRow + cCol*10 + (cRow-2)*100 + cCol*1000)

        if cRow-1 >= 0:
            rowA = cRow-1
            rowABoard = board[rowA]
            #Add single move
            if rowABoard[cCol].material == 0:
                moves.append(cRow + cCol*10 + (rowA)*100 + cCol*1000)

            #Capture right
            if cCol+1 <= 7 and rowABoard[cCol+1].material > 0:
                moves.append(cRow + cCol*10 + (rowA)*100 + (cCol+1)*1000)

            #Capture left
            if cCol-1 >= 0 and rowABoard[cCol-1].material > 0:
                moves.append(cRow + cCol*10 + (rowA)*100 + (cCol-1)*1000)

        return moves

    #Enpassent (same code in moves as a normal move)
    def enpassent(self, board, cRow, cCol, bHLength, previousBoard):
        #Skip if this is the first move of the game (to avoid index exceptions)
        if bHLength == 0:
            return []
        #Check if a pawn of the opposite color is beside you to the left
        if cCol-1 >= 0 and cRow == 3:
            if board[cRow][cCol-1].material == 1 and board[cRow-2][cCol-1].material == 0:
                #Check if there was a pawn on the 2nd row
                if previousBoard[cRow-2][cCol-1].material == 1:
                    return [cRow + cCol*10 + (cRow-1)*100 + (cCol-1)*1000]
        #Check if a pawn of the opposite color is beside you to the left
        if cCol+1 <= 7 and cRow == 3:
            if board[cRow][cCol+1].material == 1 and board[cRow-2][cCol+1].material == 0:
                #Check if there was a pawn on the 2nd row
                if previousBoard[cRow-2][cCol+1].material == 1:
                    return [cRow + cCol*10 + (cRow-1)*100 + (cCol+1)*1000]
        return []
