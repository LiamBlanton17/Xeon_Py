# Class for the White Rook

class wRook:

    #Variables
    material = 5 #Value of material
    value = 5 #Fluid value of the piece
    char = 'R' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Piece-Square map multiplier (used in isolated evaluation of pieces)
    opening = {
        56: -0.25, 57: -0.25, 58: -0.25, 59: -0.25, 60: -0.25, 61: -0.25, 62: -0.25, 63: -0.25,
        48: -0.25, 49: -0.25, 50: -0.25, 51: -0.25, 52: -0.25, 53: -0.25, 54: -0.25, 55: -0.25,
        40: -0.35, 41: -0.35, 42: -0.35, 43: -0.35, 44: -0.35, 45: -0.35, 46: -0.35, 47: -0.35,
        32: -0.35, 33: -0.35, 34: -0.35, 35: -0.35, 36: -0.35, 37: -0.35, 38: -0.35, 39: -0.35,
        24: -0.35, 25: -0.35, 26: -0.35, 27: -0.35, 28: -0.35, 29: -0.35, 30: -0.35, 31: -0.35,
        16: -0.25, 17: -0.25, 18: -0.25, 19: -0.25, 20: -0.25, 21: -0.25, 22: -0.25, 23: -0.25,
        8: -0.15, 9: -0.15, 10: -0.10, 11: -0.10, 12: -0.10, 13: -0.10, 14: -0.15, 15: -0.15,
        0: 0.00, 1: 0.00, 2: 0.10, 3: 0.15, 4: 0.15, 5: -0.15, 6: -0.10, 7: -0.05
    }

    middle_game = {
        56: 0.00, 57: 0.10, 58: 0.15, 59: 0.15, 60: 0.15, 61: 0.15, 62: 0.10, 63: 0.00,
        48: 0.05, 49: 0.15, 50: 0.20, 51: 0.20, 52: 0.20, 53: 0.20, 54: 0.15, 55: 0.05,
        40: -0.20, 41: -0.20, 42: -0.20, 43: -0.20, 44: -0.20, 45: -0.20, 46: -0.20, 47: -0.20,
        32: -0.20, 33: -0.20, 34: -0.20, 35: -0.20, 36: -0.20, 37: -0.20, 38: -0.20, 39: -0.20,
        24: -0.20, 25: -0.20, 26: -0.20, 27: -0.20, 28: -0.20, 29: -0.20, 30: -0.20, 31: -0.20,
        16: -0.15, 17: -0.10, 18: -0.05, 19: 0.00, 20: 0.00, 21: -0.05, 22: -0.10, 23: -0.15,
        8: -0.10, 9: -0.05, 10: 0.05, 11: 0.10, 12: 0.10, 13: 0.05, 14: -0.05, 15: -0.10,
        0: -0.05, 1: 0.05, 2: 0.15, 3: 0.25, 4: 0.25, 5: 0.15, 6: 0.05, 7: -0.05
    }

    endgame = {
        56: 0.00, 57: 0.10, 58: 0.20, 59: 0.20, 60: 0.20, 61: 0.20, 62: 0.10, 63: 0.00,
        48: 0.05, 49: 0.15, 50: 0.25, 51: 0.25, 52: 0.25, 53: 0.25, 54: 0.15, 55: 0.05,
        40: -0.05, 41: 0.05, 42: 0.15, 43: 0.15, 44: 0.15, 45: 0.15, 46: 0.05, 47: -0.05,
        32: -0.05, 33: 0.05, 34: 0.15, 35: 0.15, 36: 0.15, 37: 0.15, 38: 0.05, 39: -0.05,
        24: -0.05, 25: 0.05, 26: 0.15, 27: 0.15, 28: 0.15, 29: 0.15, 30: 0.05, 31: -0.05,
        16: -0.05, 17: 0.05, 18: 0.15, 19: 0.15, 20: 0.15, 21: 0.15, 22: 0.05, 23: -0.05,
        8: -0.05, 9: 0.05, 10: 0.15, 11: 0.15, 12: 0.15, 13: 0.15, 14: 0.05, 15: -0.05,
        0: -0.05, 1: 0.05, 2: 0.15, 3: 0.25, 4: 0.25, 5: 0.15, 6: 0.05, 7: -0.05
    }


#Return the pieces character
    def GetChar(self):
        return self.char

    #Method to get an isolated eval of this piece
    def getEval(self, row, col, phase_of_game):
        if phase_of_game == 'middle_game':
            return self.middle_game[(row*8)+col] + 5
        elif phase_of_game == 'endgame':
            return self.endgame[(row*8)+col] + 5
        return self.opening[(row*8)+col] + 5

    #Method to get all moves by the piece
    def getMoves(self, board, cRow, cCol):
        moves = []
        #Check Up
        for i in range(1,8):
            #Break if at end of board or running into friendly piece
            if cRow+i > 7 or board[cRow+i][cCol].material > 0:
                break
            #If at enemy piece, add move and break
            if board[cRow+i][cCol].material < 0:
                target = cRow + cCol*10 + (cRow+i)*100 + cCol*1000
                moves.append(target)
                break
            target = cRow + cCol*10 + (cRow+i)*100 + cCol*1000
            moves.append(target)
        #Check Down
        for i in range(1,8):
            #Break if at end of board or running into friendly piece
            if cRow-i < 0 or board[cRow-i][cCol].material > 0:
                break
            #If at enemy piece, add move and break
            if board[cRow-i][cCol].material < 0:
                target = cRow + cCol*10 + (cRow-i)*100 + cCol*1000
                moves.append(target)
                break
            target = cRow + cCol*10 + (cRow-i)*100 + cCol*1000
            moves.append(target)
        #Check Right
        for i in range(1,8):
            #Break if at end of board or running into friendly piece
            if cCol+i > 7 or board[cRow][cCol+i].material > 0:
                break
            #If at enemy piece, add move and break
            if board[cRow][cCol+i].material < 0:
                target = cRow + cCol*10 + cRow*100 + (cCol+i)*1000
                moves.append(target)
                break
            target = cRow + cCol*10 + cRow*100 + (cCol+i)*1000
            moves.append(target)
        #Check Left
        for i in range(1,8):
            #Break if at end of board or running into friendly piece
            if cCol-i < 0 or board[cRow][cCol-i].material > 0:
                break
            #If at enemy piece, add move and break
            if board[cRow][cCol-i].material < 0:
                target = cRow + cCol*10 + cRow*100 + (cCol-i)*1000
                moves.append(target)
                break
            target = cRow + cCol*10 + cRow*100 + (cCol-i)*1000
            moves.append(target)
        return moves
