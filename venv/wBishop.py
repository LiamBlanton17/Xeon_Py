# Class for the White Bishop

class wBishop:

    #Variables
    material = 3 #Value of material
    value = 3 #Fluid value of the piece
    char = 'B' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Piece-Square map multiplier (used in isolated evaluation of pieces)
    opening = {
        56: -0.15, 57: -0.10, 58: -0.05, 59: -0.05, 60: -0.05, 61: -0.05, 62: -0.10, 63: -0.15,
        48: -0.05, 49: 0.00, 50: 0.05, 51: 0.05, 52: 0.05, 53: 0.05, 54: 0.00, 55: -0.05,
        40: 0.00, 41: 0.05, 42: 0.10, 43: 0.10, 44: 0.10, 45: 0.10, 46: 0.05, 47: 0.00,
        32: 0.05, 33: 0.25, 34: 0.05, 35: 0.05, 36: 0.05, 37: 0.05, 38: 0.25, 39: 0.05,
        24: 0.05, 25: 0.05, 26: 0.25, 27: 0.05, 28: 0.05, 29: 0.25, 30: 0.05, 31: 0.05,
        16: -0.20, 17: 0.05, 18: 0.00, 19: 0.00, 20: 0.00, 21: 0.00, 22: 0.05, 23: -0.20,
        8: -0.10, 9: 0.15, 10: 0.00, 11: 0.05, 12: 0.05, 13: -0.10, 14: 0.15, 15: -0.10,
        0: -0.45, 1: -0.35, 2: -0.05, 3: -0.15, 4: -0.15, 5: -0.10, 6: -0.35, 7: -0.45
    }

    middle_game = {
        56: -0.15, 57: -0.10, 58: -0.05, 59: -0.05, 60: -0.05, 61: -0.05, 62: -0.10, 63: -0.15,
        48: -0.05, 49: 0.00, 50: 0.05, 51: 0.05, 52: 0.05, 53: 0.05, 54: 0.00, 55: -0.05,
        40: 0.00, 41: 0.05, 42: 0.10, 43: 0.10, 44: 0.10, 45: 0.10, 46: 0.05, 47: 0.00,
        32: 0.05, 33: 0.30, 34: 0.10, 35: 0.10, 36: 0.10, 37: 0.10, 38: 0.30, 39: 0.05,
        24: 0.05, 25: 0.15, 26: 0.30, 27: 0.15, 28: 0.15, 29: 0.30, 30: 0.15, 31: 0.05,
        16: 0.00, 17: 0.10, 18: 0.15, 19: 0.15, 20: 0.15, 21: 0.00, 22: 0.10, 23: 0.00,
        8: 0.00, 9: 0.30, 10: 0.15, 11: 0.00, 12: 0.00, 13: -0.05, 14: 0.30, 15: 0.00,
        0: -0.45, 1: -0.20, 2: -0.15, 3: -0.15, 4: -0.15, 5: -0.15, 6: -0.20, 7: -0.45
    }

    endgame = {
        56: -0.45, 57: -0.25, 58: -0.10, 59: 0.00, 60: 0.00, 61: -0.10, 62: -0.25, 63: -0.45,
        48: -0.25, 49: -0.10, 50: 0.00, 51: 0.15, 52: 0.15, 53: 0.00, 54: -0.10, 55: -0.25,
        40: -0.10, 41: 0.00, 42: 0.15, 43: 0.25, 44: 0.25, 45: 0.15, 46: 0.00, 47: -0.10,
        32: 0.00, 33: 0.15, 34: 0.25, 35: 0.25, 36: 0.25, 37: 0.25, 38: 0.15, 39: 0.00,
        24: 0.00, 25: 0.15, 26: 0.25, 27: 0.25, 28: 0.25, 29: 0.25, 30: 0.15, 31: 0.00,
        16: -0.10, 17: 0.00, 18: 0.15, 19: 0.25, 20: 0.25, 21: 0.15, 22: 0.00, 23: -0.10,
        8: -0.25, 9: -0.10, 10: 0.00, 11: 0.15, 12: 0.15, 13: 0.00, 14: -0.10, 15: -0.25,
        0: -0.45, 1: -0.25, 2: -0.10, 3: 0.00, 4: 0.00, 5: -0.10, 6: -0.25, 7: -0.45
    }


#Return the pieces character
    def GetChar(self):
        return self.char

    #Method to get an isolated eval of this piece
    def getEval(self, row, col, phase_of_game):
        if phase_of_game == 'middle_game':
            return self.middle_game[(row*8)+col] + 3
        elif phase_of_game == 'endgame':
            return self.endgame[(row*8)+col] + 3
        return self.opening[(row*8)+col] + 3

    #Method to get all moves by the piece
    def getMoves(self, board, cRow, cCol):
        moves = []
        #Check up and right
        for i in range(1,8):
            #Break if at end of board or running into friendly piece
            if cRow+i > 7 or cCol+i > 7 or board[cRow+i][cCol+i].material > 0:
                break

            #If at enemy piece, add move and break
            if board[cRow+i][cCol+i].material < 0:
                target = cRow + cCol*10 + (cRow+i)*100 + (cCol+i)*1000
                moves.append(target)
                break

            target = cRow + cCol*10 + (cRow+i)*100 + (cCol+i)*1000
            moves.append(target)
        #Check up and left
        for i in range(1,8):
            #Break if at end of board or running into friendly piece
            if cRow+i > 7 or cCol-i < 0 or board[cRow+i][cCol-i].material > 0:
                break

            #If at enemy piece, add move and break
            if board[cRow+i][cCol-i].material < 0:
                target = cRow + cCol*10 + (cRow+i)*100 + (cCol-i)*1000
                moves.append(target)
                break

            target = cRow + cCol*10 + (cRow+i)*100 + (cCol-i)*1000
            moves.append(target)
        #Check down and right
        for i in range(1,8):
            #Break if at end of board or running into friendly piece
            if cRow-i < 0 or cCol+i > 7 or board[cRow-i][cCol+i].material > 0:
                break

            #If at enemy piece, add move and break
            if board[cRow-i][cCol+i].material < 0:
                target = cRow + cCol*10 + (cRow-i)*100 + (cCol+i)*1000
                moves.append(target)
                break

            target = cRow + cCol*10 + (cRow-i)*100 + (cCol+i)*1000
            moves.append(target)
        #Check down and left
        for i in range(1,8):
            #Break if at end of board or running into friendly piece
            if cRow-i < 0 or cCol-i < 0 or board[cRow-i][cCol-i].material > 0:
                break

            #If at enemy piece, add move and break
            if board[cRow-i][cCol-i].material < 0:
                target = cRow + cCol*10 + (cRow-i)*100 + (cCol-i)*1000
                moves.append(target)
                break

            target = cRow + cCol*10 + (cRow-i)*100 + (cCol-i)*1000
            moves.append(target)
        return moves
