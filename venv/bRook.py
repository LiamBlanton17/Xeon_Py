# Class for the Black Rook

class bRook:

    #Variables
    material = -5 #Value of material
    value = -5 #Fluid value of the piece
    char = 'r' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Piece-Square map multiplier (used in isolated evaluation of pieces)
    opening = {
        56: 0.00, 57: 0.00, 58: 0.10, 59: 0.15, 60: 0.15, 61: -0.15, 62: -0.10, 63: -0.05,
        48: -0.15, 49: -0.15, 50: -0.10, 51: -0.10, 52: -0.10, 53: -0.10, 54: -0.15, 55: -0.15,
        40: -0.25, 41: -0.25, 42: -0.25, 43: -0.25, 44: -0.25, 45: -0.25, 46: -0.25, 47: -0.25,
        32: -0.35, 33: -0.35, 34: -0.35, 35: -0.35, 36: -0.35, 37: -0.35, 38: -0.35, 39: -0.35,
        24: -0.35, 25: -0.35, 26: -0.35, 27: -0.35, 28: -0.35, 29: -0.35, 30: -0.35, 31: -0.35,
        16: -0.35, 17: -0.35, 18: -0.35, 19: -0.35, 20: -0.35, 21: -0.35, 22: -0.35, 23: -0.35,
        8: -0.25, 9: -0.25, 10: -0.25, 11: -0.25, 12: -0.25, 13: -0.25, 14: -0.25, 15: -0.25,
        0: -0.25, 1: -0.25, 2: -0.25, 3: -0.25, 4: -0.25, 5: -0.25, 6: -0.25, 7: -0.25
    }

    middle_game = {
        56: -0.05, 57: 0.05, 58: 0.15, 59: 0.25, 60: 0.25, 61: 0.15, 62: 0.05, 63: -0.05,
        48: -0.10, 49: -0.05, 50: 0.05, 51: 0.10, 52: 0.10, 53: 0.05, 54: -0.05, 55: -0.10,
        40: -0.15, 41: -0.10, 42: -0.05, 43: 0.00, 44: 0.00, 45: -0.05, 46: -0.10, 47: -0.15,
        32: -0.20, 33: -0.20, 34: -0.20, 35: -0.20, 36: -0.20, 37: -0.20, 38: -0.20, 39: -0.20,
        24: -0.20, 25: -0.20, 26: -0.20, 27: -0.20, 28: -0.20, 29: -0.20, 30: -0.20, 31: -0.20,
        16: -0.20, 17: -0.20, 18: -0.20, 19: -0.20, 20: -0.20, 21: -0.20, 22: -0.20, 23: -0.20,
        8: 0.05, 9: 0.15, 10: 0.20, 11: 0.20, 12: 0.20, 13: 0.20, 14: 0.15, 15: 0.05,
        0: 0.00, 1: 0.10, 2: 0.15, 3: 0.15, 4: 0.15, 5: 0.15, 6: 0.10, 7: 0.00
    }

    endgame = {
        56: -0.05, 57: 0.05, 58: 0.15, 59: 0.15, 60: 0.15, 61: 0.15, 62: 0.05, 63: -0.05,
        48: -0.05, 49: 0.05, 50: 0.15, 51: 0.15, 52: 0.15, 53: 0.15, 54: 0.05, 55: -0.05,
        40: -0.05, 41: 0.05, 42: 0.15, 43: 0.15, 44: 0.15, 45: 0.15, 46: 0.05, 47: -0.05,
        32: -0.05, 33: 0.05, 34: 0.15, 35: 0.15, 36: 0.15, 37: 0.15, 38: 0.05, 39: -0.05,
        24: -0.05, 25: 0.05, 26: 0.15, 27: 0.15, 28: 0.15, 29: 0.15, 30: 0.05, 31: -0.05,
        16: -0.05, 17: 0.05, 18: 0.15, 19: 0.15, 20: 0.15, 21: 0.15, 22: 0.05, 23: -0.05,
        8: 0.05, 9: 0.15, 10: 0.25, 11: 0.25, 12: 0.25, 13: 0.25, 14: 0.15, 15: 0.05,
        0: 0.00, 1: 0.10, 2: 0.20, 3: 0.20, 4: 0.20, 5: 0.20, 6: 0.10, 7: 0.00
    }

#Return the pieces character
    def GetChar(self):
        return self.char

    #Method to get an isolated eval of this piece
    def getEval(self, row, col, phase_of_game):
        if phase_of_game == 'middle_game':
            return (self.middle_game[(row*8)+col] * -1) - 5
        elif phase_of_game == 'endgame':
            return (self.endgame[(row*8)+col] * -1) - 5
        return (self.opening[(row*8)+col] * -1) - 5

    #Method to get all moves by the piece
    def getMoves(self, board, cRow, cCol):
        moves = []
        #Check Up
        for i in range(1,8):
            #Break if at end of board or running into friendly piece
            if cRow+i > 7 or board[cRow+i][cCol].material < 0:
                break
            #If at enemy piece, add move and break
            if board[cRow+i][cCol].material > 0:
                target = cRow + cCol*10 + (cRow+i)*100 + cCol*1000
                moves.append(target)
                break
            target = cRow + cCol*10 + (cRow+i)*100 + cCol*1000
            moves.append(target)
        #Check Down
        for i in range(1,8):
            #Break if at end of board or running into friendly piece
            if cRow-i < 0 or board[cRow-i][cCol].material < 0:
                break
            #If at enemy piece, add move and break
            if board[cRow-i][cCol].material > 0:
                target = cRow + cCol*10 + (cRow-i)*100 + cCol*1000
                moves.append(target)
                break
            target = cRow + cCol*10 + (cRow-i)*100 + cCol*1000
            moves.append(target)
        #Check Right
        for i in range(1,8):
            #Break if at end of board or running into friendly piece
            if cCol+i > 7 or board[cRow][cCol+i].material < 0:
                break
            #If at enemy piece, add move and break
            if board[cRow][cCol+i].material > 0:
                target = cRow + cCol*10 + cRow*100 + (cCol+i)*1000
                moves.append(target)
                break
            target = cRow + cCol*10 + cRow*100 + (cCol+i)*1000
            moves.append(target)
        #Check Left
        for i in range(1,8):
            #Break if at end of board or running into friendly piece
            if cCol-i < 0 or board[cRow][cCol-i].material < 0:
                break
            #If at enemy piece, add move and break
            if board[cRow][cCol-i].material > 0:
                target = cRow + cCol*10 + cRow*100 + (cCol-i)*1000
                moves.append(target)
                break
            target = cRow + cCol*10 + cRow*100 + (cCol-i)*1000
            moves.append(target)
        return moves
