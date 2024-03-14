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
    PSM = {
        0: -8.75,
        1: -9,
        2: -9,
        3: -9,
        4: -9,
        5: -9,
        6: -9,
        7: -8.75,
        8: -8.75,
        9: -9,
        10: -9,
        11: -9,
        12: -9,
        13: -9,
        14: -9,
        15: -8.75,
        16: -8.75,
        17: -9,
        18: -9,
        19: -9,
        20: -9,
        21: -9,
        22: -9,
        23: -8.75,
        24: -9,
        25: -9.05,
        26: -9.05,
        27: -9.05,
        28: -9.05,
        29: -9.05,
        30: -9.05,
        31: -9,
        32: -9,
        33: -9.2,
        34: -9.2,
        35: -9.05,
        36: -9.05,
        37: -9.2,
        38: -9.2,
        39: -9,
        40: -8.75,
        41: -9,
        42: -9,
        43: -9,
        44: -9,
        45: -9,
        46: -9,
        47: -8.75,
        48: -8.5,
        49: -8.95,
        50: -8.95,
        51: -8.95,
        52: -8.95,
        53: -8.95,
        54: -8.95,
        55: -8.5,
        56: -8.5,
        57: -8.5,
        58: -8.75,
        59: -8.95,
        60: -8.95,
        61: -8.75,
        62: -8.5,
        63: -8.5
    }

    #Return the pieces character
    def GetChar(self):
        return self.char

    #Method to get an isolated eval of this piece
    def getEval(self, row, col):
        return self.PSM[(row*8)+col]

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
