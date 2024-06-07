# Class for the White Queen

class wQueen:

    #Variables
    material = 9 #Value of material
    value = 9 #Fluid value of the piece
    char = 'Q' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Piece-Square map multiplier (used in isolated evaluation of pieces)
    opening = {
        56: -0.30, 57: -0.30, 58: -0.30, 59: -0.30, 60: -0.30, 61: -0.30, 62: -0.30, 63: -0.30,
        48: -0.25, 49: -0.25, 50: -0.30, 51: -0.35, 52: -0.35, 53: -0.35, 54: -0.25, 55: -0.25,
        40: -0.20, 41: -0.25, 42: -0.30, 43: -0.35, 44: -0.35, 45: -0.35, 46: -0.25, 47: -0.20,
        32: -0.10, 33: -0.20, 34: -0.25, 35: -0.30, 36: -0.30, 37: -0.25, 38: -0.20, 39: -0.10,
        24: -0.05, 25: -0.10, 26: -0.20, 27: -0.25, 28: -0.25, 29: -0.25, 30: -0.15, 31: -0.10,
        16: -0.05, 17: 0.00, 18: 0.00, 19: 0.00, 20: 0.00, 21: 0.00, 22: 0.00, 23: -0.10,
        8: -0.15, 9: -0.05, 10: 0.00, 11: 0.00, 12: 0.00, 13: -0.05, 14: -0.15, 15: -0.20,
        0: -0.30, 1: -0.20, 2: -0.10, 3: 0.00, 4: 0.00, 5: -0.15, 6: -0.25, 7: -0.35
    }

    middle_game = {
        56: 0.10, 57: 0.25, 58: 0.25, 59: 0.10, 60: 0.10, 61: 0.25, 62: 0.25, 63: 0.10,
        48: 0.10, 49: 0.25, 50: 0.25, 51: 0.10, 52: 0.10, 53: 0.25, 54: 0.25, 55: 0.10,
        40: 0.10, 41: 0.25, 42: 0.25, 43: 0.10, 44: 0.10, 45: 0.25, 46: 0.25, 47: 0.10,
        32: 0.05, 33: 0.15, 34: 0.15, 35: 0.05, 36: 0.05, 37: 0.15, 38: 0.15, 39: 0.05,
        24: 0.00, 25: 0.05, 26: 0.10, 27: 0.05, 28: 0.05, 29: 0.10, 30: 0.10, 31: 0.00,
        16: -0.20, 17: 0.05, 18: 0.05, 19: 0.00, 20: 0.00, 21: 0.05, 22: 0.05, 23: -0.20,
        8: -0.30, 9: -0.20, 10: 0.00, 11: 0.00, 12: 0.00, 13: -0.10, 14: -0.15, 15: -0.35,
        0: -0.40, 1: -0.30, 2: -0.20, 3: -0.05, 4: -0.15, 5: -0.25, 6: -0.35, 7: -0.45
    }

    endgame = {
        56: -0.45, 57: -0.35, 58: -0.25, 59: -0.10, 60: -0.10, 61: -0.25, 62: -0.35, 63: -0.45,
        48: -0.35, 49: -0.20, 50: -0.05, 51: 0.05, 52: 0.05, 53: -0.05, 54: -0.20, 55: -0.35,
        40: -0.25, 41: -0.05, 42: 0.05, 43: 0.15, 44: 0.15, 45: 0.05, 46: -0.05, 47: -0.25,
        32: -0.10, 33: 0.05, 34: 0.15, 35: 0.25, 36: 0.25, 37: 0.15, 38: 0.05, 39: -0.10,
        24: -0.10, 25: 0.05, 26: 0.15, 27: 0.25, 28: 0.25, 29: 0.15, 30: 0.05, 31: -0.10,
        16: -0.25, 17: -0.05, 18: 0.05, 19: 0.15, 20: 0.15, 21: 0.05, 22: -0.05, 23: -0.25,
        8: -0.35, 9: -0.20, 10: -0.05, 11: 0.05, 12: 0.05, 13: -0.05, 14: -0.20, 15: -0.35,
        0: -0.45
    }

    #Return the pieces character
    def GetChar(self):
        return self.char

    #Method to get an isolated eval of this piece
    def getEval(self, row, col, phase_of_game):
        if phase_of_game == 'middle_game':
            return self.middle_game[(row*8)+col] + 9
        elif phase_of_game == 'endgame':
            return self.endgame[(row*8)+col] + 9
        return self.opening[(row*8)+col] + 9

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
