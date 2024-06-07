# Class for the Black Knight

class bKnight:

    #Variables
    material = -3 #Value of material
    value = -3 #Fluid value of the piece
    char = 'n' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Piece-Square map multiplier (used in isolated evaluation of pieces)
    opening = {
        56: -0.55, 57: -0.15, 58: -0.15, 59: -0.25, 60: -0.25, 61: -0.15, 62: -0.20, 63: -0.55,
        48: -0.30, 49: -0.25, 50: -0.15, 51: 0.05, 52: 0.05, 53: -0.15, 54: -0.25, 55: -0.30,
        40: -0.25, 41: 0.10, 42: 0.25, 43: 0.00, 44: 0.00, 45: 0.25, 46: 0.10, 47: -0.25,
        32: -0.25, 33: 0.15, 34: 0.20, 35: 0.15, 36: 0.15, 37: 0.20, 38: 0.15, 39: -0.25,
        24: -0.25, 25: 0.15, 26: 0.20, 27: 0.20, 28: 0.20, 29: 0.20, 30: 0.15, 31: -0.25,
        16: -0.25, 17: 0.15, 18: 0.20, 19: 0.20, 20: 0.20, 21: 0.20, 22: 0.15, 23: -0.25,
        8: -0.25, 9: 0.05, 10: 0.10, 11: 0.10, 12: 0.10, 13: 0.10, 14: 0.05, 15: -0.25,
        0: -0.55, 1: -0.15, 2: -0.15, 3: -0.25, 4: -0.25, 5: -0.15, 6: -0.20, 7: -0.55
    }

    middle_game = {
        56: -0.55, 57: -0.20, 58: -0.20, 59: -0.20, 60: -0.20, 61: -0.20, 62: -0.20, 63: -0.55,
        48: -0.35, 49: -0.20, 50: -0.15, 51: -0.10, 52: -0.10, 53: -0.15, 54: -0.20, 55: -0.35,
        40: -0.25, 41: 0.05, 42: 0.20, 43: 0.25, 44: 0.25, 45: 0.20, 46: 0.05, 47: -0.25,
        32: -0.25, 33: 0.10, 34: 0.25, 35: 0.25, 36: 0.25, 37: 0.25, 38: 0.10, 39: -0.25,
        24: -0.25, 25: 0.15, 26: 0.25, 27: 0.35, 28: 0.35, 29: 0.25, 30: 0.15, 31: -0.25,
        16: -0.25, 17: 0.15, 18: 0.30, 19: 0.35, 20: 0.35, 21: 0.30, 22: 0.15, 23: -0.25,
        8: -0.25, 9: 0.05, 10: 0.20, 11: 0.25, 12: 0.25, 13: 0.20, 14: 0.05, 15: -0.25,
        0: -0.35, 1: -0.20, 2: -0.15, 3: -0.10, 4: -0.10, 5: -0.15, 6: -0.20, 7: -0.35
    }

    endgame = {
        56: -0.50, 57: -0.40, 58: -0.25, 59: -0.10, 60: -0.10, 61: -0.25, 62: -0.40, 63: -0.50,
        48: -0.40, 49: -0.25, 50: -0.10, 51: 0.00, 52: 0.00, 53: -0.10, 54: -0.25, 55: -0.40,
        40: -0.25, 41: -0.10, 42: 0.00, 43: 0.10, 44: 0.10, 45: 0.00, 46: -0.10, 47: -0.25,
        32: -0.10, 33: 0.00, 34: 0.10, 35: 0.20, 36: 0.20, 37: 0.10, 38: 0.00, 39: -0.10,
        24: -0.10, 25: 0.00, 26: 0.10, 27: 0.20, 28: 0.20, 29: 0.10, 30: 0.00, 31: -0.10,
        16: -0.25, 17: -0.10, 18: 0.00, 19: 0.10, 20: 0.10, 21: 0.00, 22: -0.10, 23: -0.25,
        8: -0.40, 9: -0.25, 10: -0.10, 11: 0.00, 12: 0.00, 13: -0.10, 14: -0.25, 15: -0.40,
        0: -0.50, 1: -0.40, 2: -0.25, 3: -0.10, 4: -0.10, 5: -0.25, 6: -0.40, 7: -0.50
    }


    #Return the pieces character
    def GetChar(self):
        return self.char

    #Method to get an isolated eval of this piece
    def getEval(self, row, col, phase_of_game):
        if phase_of_game == 'middle_game':
            return (self.middle_game[(row*8)+col] * -1) - 3
        elif phase_of_game == 'endgame':
            return (self.endgame[(row*8)+col] * -1) - 3
        return (self.opening[(row*8)+col] * -1) - 3

    #Get Moves method
    def getMoves(self, board, cRow, cCol):
        moves = []
        if cRow+2 <= 7:
            #Check up-right
            if not (cCol+1 > 7 or board[cRow+2][cCol+1].material < 0):
                target = cRow + cCol*10 + (cRow+2)*100 + (cCol+1)*1000
                moves.append(target)
            #Check up-left
            if not (cCol-1 < 0 or board[cRow+2][cCol-1].material < 0):
                target = cRow + cCol*10 + (cRow+2)*100 + (cCol-1)*1000
                moves.append(target)
        if cCol+2 <= 7:
            #Check right-up
            if not (cRow+1 > 7 or board[cRow+1][cCol+2].material < 0):
                target = cRow + cCol*10 + (cRow+1)*100 + (cCol+2)*1000
                moves.append(target)
            #Check right-down
            if not (cRow-1 < 0 or board[cRow-1][cCol+2].material < 0):
                target = cRow + cCol*10 + (cRow-1)*100 + (cCol+2)*1000
                moves.append(target)
        if cCol-2 >= 0:
            #Check left-up
            if not (cRow+1 > 7 or board[cRow+1][cCol-2].material < 0):
                target = cRow + cCol*10 + (cRow+1)*100 + (cCol-2)*1000
                moves.append(target)
            #Check left-down
            if not (cRow-1 < 0 or board[cRow-1][cCol-2].material < 0):
                target = cRow + cCol*10 + (cRow-1)*100 + (cCol-2)*1000
                moves.append(target)
        if cRow-2 >= 0:
            #Check down-right
            if not (cCol+1 > 7 or board[cRow-2][cCol+1].material < 0):
                target = cRow + cCol*10 + (cRow-2)*100 + (cCol+1)*1000
                moves.append(target)
            #Check down-left
            if not (cCol-1 < 0 or board[cRow-2][cCol-1].material < 0):
                target = cRow + cCol*10 + (cRow-2)*100 + (cCol-1)*1000
                moves.append(target)
        return moves
