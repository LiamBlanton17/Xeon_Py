# Class for the White Knight

class wKnight:

    #Variables
    material = 3 #Value of material
    value = 3 #Fluid value of the piece
    char = 'N' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Piece-Square map multiplier (used in isolated evaluation of pieces)
    PSM = {
        0: 2.5,
        1: 2.75,
        2: 2.75,
        3: 2.75,
        4: 2.75,
        5: 2.75,
        6: 2.75,
        7: 2.5,
        8: 2.5,
        9: 2.75,
        10: 2.95,
        11: 2.95,
        12: 2.95,
        13: 2.95,
        14: 2.75,
        15: 2.5,
        16: 2.5,
        17: 2.95,
        18: 3.2,
        19: 3.15,
        20: 3.15,
        21: 3.2,
        22: 2.95,
        23: 2.5,
        24: 2.75,
        25: 3,
        26: 3.2,
        27: 3.2,
        28: 3.2,
        29: 3.2,
        30: 3,
        31: 2.75,
        32: 2.75,
        33: 3.1,
        34: 3.25,
        35: 3.3,
        36: 3.3,
        37: 3.25,
        38: 3.1,
        39: 2.75,
        40: 2.5,
        41: 3,
        42: 3.2,
        43: 3.2,
        44: 3.2,
        45: 3.2,
        46: 3,
        47: 2.5,
        48: 2.5,
        49: 2.75,
        50: 2.95,
        51: 2.95,
        52: 2.95,
        53: 2.95,
        54: 2.75,
        55: 2.5,
        56: 2.5,
        57: 2.75,
        58: 2.95,
        59: 2.95,
        60: 2.95,
        61: 2.95,
        62: 2.75,
        63: 2.5
    }

    #Return the pieces character
    def GetChar(self):
        return self.char

    #Method to get an isolated eval of this piece
    def getEval(self, row, col):
        return self.PSM[(row*8)+col]

    #Get Moves method
    def getMoves(self, board, cRow, cCol):
        moves = []
        #Check up-right
        if not (cRow+2 > 7 or cCol+1 > 7 or board[cRow+2][cCol+1].material > 0):
            target = cRow + cCol*10 + (cRow+2)*100 + (cCol+1)*1000
            moves.append(target)
        #Check up-left
        if not (cRow+2 > 7 or cCol-1 < 0 or board[cRow+2][cCol-1].material > 0):
            target = cRow + cCol*10 + (cRow+2)*100 + (cCol-1)*1000
            moves.append(target)
        #Check right-up
        if not (cRow+1 > 7 or cCol+2 > 7 or board[cRow+1][cCol+2].material > 0):
            target = cRow + cCol*10 + (cRow+1)*100 + (cCol+2)*1000
            moves.append(target)
        #Check right-down
        if not (cRow-1 < 0 or cCol+2 > 7 or board[cRow-1][cCol+2].material > 0):
            target = cRow + cCol*10 + (cRow-1)*100 + (cCol+2)*1000
            moves.append(target)
        #Check left-up
        if not (cRow+1 > 7 or cCol-2 < 0 or board[cRow+1][cCol-2].material > 0):
            target = cRow + cCol*10 + (cRow+1)*100 + (cCol-2)*1000
            moves.append(target)
        #Check left-down
        if not (cRow-1 < 0 or cCol-2 < 0 or board[cRow-1][cCol-2].material > 0):
            target = cRow + cCol*10 + (cRow-1)*100 + (cCol-2)*1000
            moves.append(target)
        #Check down-right
        if not (cRow-2 < 0 or cCol+1 > 7 or board[cRow-2][cCol+1].material > 0):
            target = cRow + cCol*10 + (cRow-2)*100 + (cCol+1)*1000
            moves.append(target)
        #Check down-left
        if not (cRow-2 < 0 or cCol-1 < 0 or board[cRow-2][cCol-1].material > 0):
            target = cRow + cCol*10 + (cRow-2)*100 + (cCol-1)*1000
            moves.append(target)
        return moves
