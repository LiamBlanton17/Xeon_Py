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
    PSM = {
        0: -2.5,
        1: -2.75,
        2: -2.95,
        3: -2.95,
        4: -2.95,
        5: -2.95,
        6: -2.75,
        7: -2.5,
        8: -2.5,
        9: -2.75,
        10: -2.95,
        11: -2.95,
        12: -2.95,
        13: -2.95,
        14: -2.75,
        15: -2.5,
        16: -2.5,
        17: -3,
        18: -3.2,
        19: -3.2,
        20: -3.2,
        21: -3.2,
        22: -3,
        23: -2.5,
        24: -2.75,
        25: -3.1,
        26: -3.25,
        27: -3.3,
        28: -3.3,
        29: -3.25,
        30: -3.1,
        31: -2.75,
        32: -2.75,
        33: -3,
        34: -3.2,
        35: -3.2,
        36: -3.2,
        37: -3.2,
        38: -3,
        39: -2.75,
        40: -2.5,
        41: -2.95,
        42: -3.2,
        43: -3.15,
        44: -3.15,
        45: -3.2,
        46: -2.95,
        47: -2.5,
        48: -2.5,
        49: -2.75,
        50: -2.95,
        51: -2.95,
        52: -2.95,
        53: -2.95,
        54: -2.75,
        55: -2.5,
        56: -2.5,
        57: -2.75,
        58: -2.75,
        59: -2.75,
        60: -2.75,
        61: -2.75,
        62: -2.75,
        63: -2.5
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
