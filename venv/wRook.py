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
    PSM = {
        0: 5.05,
        1: 5.05,
        2: 5.1,
        3: 5.15,
        4: 5.15,
        5: 5.1,
        6: 5.05,
        7: 5.05,
        8: 5,
        9: 5,
        10: 5,
        11: 5,
        12: 5,
        13: 5,
        14: 5,
        15: 5,
        16: 4.9,
        17: 4.9,
        18: 4.9,
        19: 4.9,
        20: 4.9,
        21: 4.9,
        22: 4.9,
        23: 4.9,
        24: 4.9,
        25: 4.9,
        26: 4.9,
        27: 4.9,
        28: 4.9,
        29: 4.9,
        30: 4.9,
        31: 4.9,
        32: 4.9,
        33: 4.9,
        34: 4.9,
        35: 4.9,
        36: 4.9,
        37: 4.9,
        38: 4.9,
        39: 4.9,
        40: 4.9,
        41: 4.9,
        42: 4.9,
        43: 4.9,
        44: 4.9,
        45: 4.9,
        46: 4.9,
        47: 4.9,
        48: 5.05,
        49: 5.05,
        50: 5.05,
        51: 5.05,
        52: 5.05,
        53: 5.05,
        54: 5.05,
        55: 5.05,
        56: 5,
        57: 5,
        58: 5,
        59: 5,
        60: 5,
        61: 5,
        62: 5,
        63: 5
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
