# Class for the Black Pawn

class bPawn:

    #Variables
    material = -1 #Value of material
    value = -1 #Fluid value of the piece
    char = 'p' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Piece-Square map multiplier (used in isolated evaluation of pieces)
    PSM = {
        0: -5,
        1: -5,
        2: -5,
        3: -5,
        4: -5,
        5: -5,
        6: -5,
        7: -5,
        8: -1.07,
        9: -1.07,
        10: -1.15,
        11: -1.2,
        12: -1.2,
        13: -1.07,
        14: -1.07,
        15: -1.07,
        16: -1.05,
        17: -1.05,
        18: -1.12,
        19: -1.17,
        20: -1.17,
        21: -1.05,
        22: -1.05,
        23: -1.05,
        24: -1,
        25: -1,
        26: -1.1,
        27: -1.15,
        28: -1.15,
        29: -1,
        30: -1,
        31: -1,
        32: -1,
        33: -1,
        34: -1.05,
        35: -1.1,
        36: -1.1,
        37: -0.95,
        38: -0.95,
        39: -0.95,
        40: -1.05,
        41: -1.05,
        42: -1.05,
        43: -1.05,
        44: -1.05,
        45: -0.95,
        46: -1,
        47: -1.05,
        48: -1,
        49: -1,
        50: -1,
        51: -1,
        52: -1,
        53: -1,
        54: -1,
        55: -1,
        56: 0,
        57: 0,
        58: 0,
        59: 0,
        60: 0,
        61: 0,
        62: 0,
        63: 0
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

        #If on starting row, add a double move, if possible
        if cRow == 6:
            if board[5][cCol].material == 0 and board[4][cCol].material == 0:
                moves.append(cRow + cCol*10 + (cRow-2)*100 + cCol*1000)

        if cRow-1 >= 0:
            #Add single move
            if board[cRow-1][cCol].material == 0:
                moves.append(cRow + cCol*10 + (cRow-1)*100 + cCol*1000)

            #Capture right
            if cCol+1 <= 7 and board[cRow-1][cCol+1].material > 0:
                moves.append(cRow + cCol*10 + (cRow-1)*100 + (cCol+1)*1000)

            #Capture left
            if cCol-1 >= 0 and board[cRow-1][cCol-1].material > 0:
                moves.append(cRow + cCol*10 + (cRow-1)*100 + (cCol-1)*1000)

        return moves

    #Enpassent (same code in moves as a normal move)
    def enpassent(self, board, cRow, cCol, bHLength, previousBoard):
        #Skip if this is the first move of the game (to avoid index exceptions)
        if bHLength == 0:
            return []
        #Check if a pawn of the opposite color is beside you to the left
        if cCol-1 >= 0 and cRow == 3:
            if board[cRow][cCol-1].material == 1 and board[cRow-2][cCol-1].material == 0:
                #Check if there was a pawn on the 2nd row
                if previousBoard[cRow-2][cCol-1].material == 1:
                    return [cRow + cCol*10 + (cRow-1)*100 + (cCol-1)*1000]
        #Check if a pawn of the opposite color is beside you to the left
        if cCol+1 <= 7 and cRow == 3:
            if board[cRow][cCol+1].material == 1 and board[cRow-2][cCol+1].material == 0:
                #Check if there was a pawn on the 2nd row
                if previousBoard[cRow-2][cCol+1].material == 1:
                    return [cRow + cCol*10 + (cRow-1)*100 + (cCol+1)*1000]
        return []
