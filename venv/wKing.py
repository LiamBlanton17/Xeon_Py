# Class for the White King

class wKing:

    #Variables
    material = 1000 #Value of material
    value = 1000 #Fluid value of the piece
    char = 'K' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Piece-Square map multiplier (used in isolated evaluation of pieces)
    PSM = {
        0: 0.25,
        1: 0.4,
        2: 0.25,
        3: -0.35,
        4: 0,
        5: 0.05,
        6: 0.45,
        7: 0.3,
        8: 0,
        9: 0,
        10: 0,
        11: -0.35,
        12: -0.35,
        13: 0,
        14: 0,
        15: 0,
        16: -0.15,
        17: -0.25,
        18: -0.25,
        19: -0.45,
        20: -0.45,
        21: -0.25,
        22: -0.25,
        23: -0.15,
        24: -0.35,
        25: -0.55,
        26: -0.55,
        27: -1,
        28: -1,
        29: -0.55,
        30: -0.55,
        31: -0.35,
        32: -3,
        33: -3,
        34: -3,
        35: -3,
        36: -3,
        37: -3,
        38: -3,
        39: -3,
        40: -3,
        41: -3,
        42: -3,
        43: -3,
        44: -3,
        45: -3,
        46: -3,
        47: -3,
        48: -3,
        49: -3,
        50: -3,
        51: -3,
        52: -3,
        53: -3,
        54: -3,
        55: -3,
        56: -3,
        57: -3,
        58: -3,
        59: -3,
        60: -3,
        61: -3,
        62: -3,
        63: -3
    }

    #Return the pieces character
    def GetChar(self):
        return self.char

    #Method to get an isolated eval of this piece
    def getEval(self, row, col):
        return self.PSM[(row*8)+col] + 1000

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
                if cRow+i > 7 or cRow+i < 0 or cCol+j > 7 or cCol+j < 0 or board[cRow+i][cCol+j].material > 0:
                    continue
                target = cRow + cCol*10 + (cRow+i)*100 + (cCol+j)*1000
                moves.append(target)

        return moves
