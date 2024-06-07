# Class for the Black Queen

class bQueen:

    #Variables
    material = -9 #Value of material
    value = -9 #Fluid value of the piece
    char = 'q' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Piece-Square map multiplier (used in isolated evaluation of pieces)
    opening = {
        56: -0.30, 57: -0.20, 58: -0.10, 59: 0.00, 60: 0.00, 61: -0.15, 62: -0.25, 63: -0.35,
        48: -0.15, 49: -0.05, 50: 0.00, 51: 0.00, 52: 0.00, 53: -0.05, 54: -0.15, 55: -0.20,
        40: -0.05, 41: 0.00, 42: 0.00, 43: 0.00, 44: 0.00, 45: 0.00, 46: 0.00, 47: -0.10,
        32: -0.05, 33: -0.10, 34: -0.20, 35: -0.25, 36: -0.25, 37: -0.25, 38: -0.15, 39: -0.10,
        24: -0.10, 25: -0.20, 26: -0.25, 27: -0.30, 28: -0.30, 29: -0.25, 30: -0.20, 31: -0.10,
        16: -0.20, 17: -0.25, 18: -0.30, 19: -0.35, 20: -0.35, 21: -0.35, 22: -0.25, 23: -0.20,
        8: -0.25, 9: -0.25, 10: -0.30, 11: -0.35, 12: -0.35, 13: -0.35, 14: -0.25, 15: -0.25,
        0: -0.30, 1: -0.30, 2: -0.30, 3: -0.30, 4: -0.30, 5: -0.30, 6: -0.30, 7: -0.30
    }

    middle_game = {
        56: -0.40, 57: -0.30, 58: -0.20, 59: -0.05, 60: -0.15, 61: -0.25, 62: -0.35, 63: -0.45,
        48: -0.30, 49: -0.20, 50: 0.00, 51: 0.00, 52: 0.00, 53: -0.10, 54: -0.15, 55: -0.35,
        40: -0.20, 41: 0.05, 42: 0.05, 43: 0.00, 44: 0.00, 45: 0.05, 46: 0.05, 47: -0.20,
        32: 0.00, 33: 0.05, 34: 0.10, 35: 0.05, 36: 0.05, 37: 0.10, 38: 0.10, 39: 0.00,
        24: 0.05, 25: 0.15, 26: 0.15, 27: 0.05, 28: 0.05, 29: 0.15, 30: 0.15, 31: 0.05,
        16: 0.10, 17: 0.25, 18: 0.25, 19: 0.10, 20: 0.10, 21: 0.25, 22: 0.25, 23: 0.10,
        8: 0.10, 9: 0.25, 10: 0.25, 11: 0.10, 12: 0.10, 13: 0.25, 14: 0.25, 15: 0.10,
        0: 0.10, 1: 0.25, 2: 0.25, 3: 0.10, 4: 0.10, 5: 0.25, 6: 0.25, 7: 0.10
    }

    endgame = {
        56: -0.45, 57: -0.35, 58: -0.25, 59: -0.10, 60: -0.10, 61: -0.25, 62: -0.35, 63: -0.45,
        48: -0.35, 49: -0.20, 50: -0.05, 51: 0.05, 52: 0.05, 53: -0.05, 54: -0.20, 55: -0.35,
        40: -0.25, 41: -0.05, 42: 0.05, 43: 0.15, 44: 0.15, 45: 0.05, 46: -0.05, 47: -0.25,
        32: -0.10, 33: 0.05, 34: 0.15, 35: 0.25, 36: 0.25, 37: 0.15, 38: 0.05, 39: -0.10,
        24: -0.10, 25: 0.05, 26: 0.15, 27: 0.25, 28: 0.25, 29: 0.15, 30: 0.05, 31: -0.10,
        16: -0.25, 17: -0.05, 18: 0.05, 19: 0.15, 20: 0.15, 21: 0.05, 22: -0.05, 23: -0.25,
        8: -0.35, 9: -0.20, 10: -0.05, 11: 0.05, 12: 0.05, 13: -0.05, 14: -0.20, 15: -0.35,
        0: -0.45, 1: -0.35, 2: -0.25, 3: -0.10, 4: -0.10, 5: -0.25, 6: -0.35, 7: -0.45,
    }


#Return the pieces character
    def GetChar(self):
        return self.char

    #Method to get an isolated eval of this piece
    def getEval(self, row, col, phase_of_game):
        if phase_of_game == 'middle_game':
            return (self.middle_game[(row*8)+col] * -1) - 9
        elif phase_of_game == 'endgame':
            return (self.endgame[(row*8)+col] * -1) - 9
        return (self.opening[(row*8)+col] * -1) - 9

    #Method to get all moves by the piece
    def getMoves(self, board, cRow, cCol):
        moves = []
        #Check up and right
        for i in range(1,8):

            #Break if at end of board or running into friendly piece
            if cRow+i > 7 or cCol+i > 7 or board[cRow+i][cCol+i].material < 0:
                break

            #If at enemy piece, add move and break
            if board[cRow+i][cCol+i].material > 0:
                target = cRow + cCol*10 + (cRow+i)*100 + (cCol+i)*1000
                moves.append(target)
                break

            target = cRow + cCol*10 + (cRow+i)*100 + (cCol+i)*1000
            moves.append(target)
        #Check up and left
        for i in range(1,8):
            #Break if at end of board or running into friendly piece
            if cRow+i > 7 or cCol-i < 0 or board[cRow+i][cCol-i].material < 0:
                break

            #If at enemy piece, add move and break
            if board[cRow+i][cCol-i].material > 0:
                target = cRow + cCol*10 + (cRow+i)*100 + (cCol-i)*1000
                moves.append(target)
                break

            target = cRow + cCol*10 + (cRow+i)*100 + (cCol-i)*1000
            moves.append(target)
        #Check down and right
        for i in range(1,8):
            #Break if at end of board or running into friendly piece
            if cRow-i < 0 or cCol+i > 7 or board[cRow-i][cCol+i].material < 0:
                break

            #If at enemy piece, add move and break
            if board[cRow-i][cCol+i].material > 0:
                target = cRow + cCol*10 + (cRow-i)*100 + (cCol+i)*1000
                moves.append(target)
                break

            target = cRow + cCol*10 + (cRow-i)*100 + (cCol+i)*1000
            moves.append(target)
        #Check down and left
        for i in range(1,8):
            #Break if at end of board or running into friendly piece
            if cRow-i < 0 or cCol-i < 0 or board[cRow-i][cCol-i].material < 0:
                break

            #If at enemy piece, add move and break
            if board[cRow-i][cCol-i].material > 0:
                target = cRow + cCol*10 + (cRow-i)*100 + (cCol-i)*1000
                moves.append(target)
                break

            target = cRow + cCol*10 + (cRow-i)*100 + (cCol-i)*1000
            moves.append(target)
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
