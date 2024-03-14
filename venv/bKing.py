# Class for the Black King

class bKing:

    #Variables
    material = -1000 #Value of material
    value = -1000 #Fluid value of the piece
    char = 'k' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Piece-Square map multiplier (used in isolated evaluation of pieces)
    PSM = {
        0: 3,
        1: 3,
        2: 3,
        3: 3,
        4: 3,
        5: 3,
        6: 3,
        7: 3,
        8: 3,
        9: 3,
        10: 3,
        11: 3,
        12: 3,
        13: 3,
        14: 3,
        15: 3,
        16: 3,
        17: 3,
        18: 3,
        19: 3,
        20: 3,
        21: 3,
        22: 3,
        23: 3,
        24: 3,
        25: 3,
        26: 3,
        27: 3,
        28: 3,
        29: 3,
        30: 3,
        31: 3,
        32: 0.35,
        33: 0.55,
        34: 0.55,
        35: 1,
        36: 1,
        37: 0.55,
        38: 0.55,
        39: 0.35,
        40: 0.15,
        41: 0.25,
        42: 0.25,
        43: 0.45,
        44: 0.45,
        45: 0.25,
        46: 0.25,
        47: 0.15,
        48: 0,
        49: 0,
        50: 0,
        51: 0.35,
        52: 0.35,
        53: 0,
        54: 0,
        55: 0,
        56: -0.25,
        57: -0.4,
        58: -0.25,
        59: 0.35,
        60: 0,
        61: -0.05,
        62: -0.45,
        63: -0.30
    }

    #Return the pieces character
    def GetChar(self):
        return self.char

    #Method to get an isolated eval of this piece
    def getEval(self, row, col):
        return self.PSM[(row*8)+col] - 1000

    #Get Moves method
    def getMoves(self, board, cRow, cCol):
        moves = []

        # Loop to generate moves
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                #Continue if 0,0
                if i == 0 and j == 0:
                    continue
                #Continue if square doesn't exist or occupied by friendly
                if cRow+i > 7 or cRow+i < 0 or cCol+j > 7 or cCol+j < 0 or board[cRow+i][cCol+j].material < 0:
                    continue
                target = cRow + cCol*10 + (cRow+i)*100 + (cCol+j)*1000
                moves.append(target)

        return moves
