# Class for the White Pawn

class wPawn:

    #Variables
    material = 1 #Value of material
    value = 1 #Fluid value of the piece
    char = 'P' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Piece-Square map multiplier (used in isolated evaluation of pieces)
    opening = {
        56: +5.00, 57: +5.00, 58: +5.00, 59: +5.00, 60: +5.00, 61: +5.00, 62: +5.00, 63: +5.00,
        48: +0.10, 49: +0.15, 50: +0.30, 51: +0.30, 52: +0.30, 53: +0.25, 54: +0.15, 55: +0.15,
        40: +0.00, 41: +0.05, 42: +0.20, 43: +0.25, 44: +0.25, 45: +0.15, 46: +0.05, 47: +0.00,
        32: +0.10, 33: +0.05, 34: +0.25, 35: +0.30, 36: +0.30, 37: +0.00, 38: -0.05, 39: +0.00,
        24: +0.05, 25: +0.05, 26: +0.20, 27: +0.25, 28: +0.25, 29: -0.05, 30: -0.05, 31: -0.05,
        16: +0.05, 17: +0.05, 18: +0.10, 19: +0.10, 20: +0.10, 21: -0.15, 22: +0.00, 23: +0.05,
        8: +0.00, 9: +0.00, 10: -0.05, 11: -0.25, 12: -0.25, 13: +0.10, 14: +0.05, 15: +0.00,
        0: +0.00, 1: +0.00, 2: +0.00, 3: +0.00, 4: +0.00, 5: +0.00, 6: +0.00, 7: +0.00
    }

    middle_game = {
        56: +5.00, 57: +5.00, 58: +5.00, 59: +5.00, 60: +5.00, 61: +5.00, 62: +5.00, 63: +5.00,
        48: +0.30, 49: +0.30, 50: +0.35, 51: +0.45, 52: +0.45, 53: +0.25, 54: +0.25, 55: +0.25,
        40: +0.20, 41: +0.20, 42: +0.25, 43: +0.35, 44: +0.35, 45: +0.10, 46: +0.10, 47: +0.15,
        32: +0.15, 33: +0.15, 34: +0.20, 35: +0.30, 36: +0.30, 37: +0.05, 38: +0.00, 39: +0.10,
        24: +0.05, 25: +0.05, 26: +0.15, 27: +0.25, 28: +0.25, 29: +0.00, 30: +0.00, 31: +0.05,
        16: +0.00, 17: +0.00, 18: +0.05, 19: +0.15, 20: +0.15, 21: -0.15, 22: +0.10, 23: +0.10,
        8: -0.05, 9: -0.05, 10: -0.05, 11: -0.35, 12: -0.35, 13: +0.10, 14: +0.10, 15: +0.05,
        0: +0.00, 1: +0.00, 2: +0.00, 3: +0.00, 4: +0.00, 5: +0.00, 6: +0.00, 7: +0.00
    }

    endgame = {
        56: +5.00, 57: +5.00, 58: +5.00, 59: +5.00, 60: +5.00, 61: +5.00, 62: +5.00, 63: +5.00,
        48: +0.55, 49: +0.55, 50: +0.40, 51: +0.40, 52: +0.40, 53: +0.40, 54: +0.55, 55: +0.55,
        40: +0.30, 41: +0.30, 42: +0.20, 43: +0.20, 44: +0.20, 45: +0.20, 46: +0.30, 47: +0.30,
        32: +0.20, 33: +0.20, 34: +0.10, 35: +0.10, 36: +0.10, 37: +0.10, 38: +0.20, 39: +0.20,
        24: +0.10, 25: +0.10, 26: +0.05, 27: +0.05, 28: +0.05, 29: +0.05, 30: +0.10, 31: +0.10,
        16: +0.00, 17: +0.00, 18: +0.00, 19: +0.00, 20: +0.00, 21: +0.00, 22: +0.00, 23: +0.00,
        8: -0.05, 9: -0.05, 10: -0.05, 11: -0.05, 12: -0.05, 13: -0.05, 14: -0.05, 15: -0.05,
        0: +0.00, 1: +0.00, 2: +0.00, 3: +0.00, 4: +0.00, 5: +0.00, 6: +0.00, 7: +0.00
    }

    #Return the pieces character
    def GetChar(self):
        return self.char

    #Method to get an isolated eval of this piece
    def getEval(self, row, col, phase_of_game):
        if phase_of_game == 'middle_game':
            return self.middle_game[(row*8)+col] + 1
        elif phase_of_game == 'endgame':
            return self.endgame[(row*8)+col] + 1
        return self.opening[(row*8)+col] + 1

    #Get Moves method
    def getMoves(self, board, cRow, cCol):
        moves = []

        #If on starting row, add a double move, if possible
        if cRow == 1:
            if board[2][cCol].material == 0 and board[3][cCol].material == 0:
                moves.append(cRow + cCol*10 + (cRow+2)*100 + cCol*1000)

        if cRow+1 <= 7:
            #Add single move
            if board[cRow+1][cCol].material == 0:
                moves.append(cRow + cCol*10 + (cRow+1)*100 + cCol*1000)

            #Capture right
            if cCol+1 <= 7 and board[cRow+1][cCol+1].material < 0:
                moves.append(cRow + cCol*10 + (cRow+1)*100 + (cCol+1)*1000)

            #Capture left
            if cCol-1 >= 0 and board[cRow+1][cCol-1].material < 0:
                moves.append(cRow + cCol*10 + (cRow+1)*100 + (cCol-1)*1000)

        return moves

    # Enpassent (same code in moves as a normal move)
    def enpassent(self, board, cRow, cCol, bHLength, previousBoard):
        #Skip if this is the first move of the game (to avoid index exceptions)
        if bHLength == 0:
            return []
        #Check if a pawn of the opposite color is beside you to the left
        if cCol-1 >= 0 and cRow == 4:
            if board[cRow][cCol-1].material == -1 and board[cRow+2][cCol-1].material == 0:
                #Check if there was a pawn on the 2nd row
                if previousBoard[cRow+2][cCol-1].material == -1:
                    return [cRow + cCol*10 + (cRow+1)*100 + (cCol-1)*1000]
        #Check if a pawn of the opposite color is beside you to the left
        if cCol+1 <= 7 and cRow == 4:
            if board[cRow][cCol+1].material == -1 and board[cRow+2][cCol+1].material == 0:
                #Check if there was a pawn on the 2nd row
                if previousBoard[cRow+2][cCol+1].material == -1:
                    return [cRow + cCol*10 + (cRow+1)*100 + (cCol+1)*1000]
        return []
