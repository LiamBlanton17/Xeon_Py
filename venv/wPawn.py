# Class for the White Pawn

class wPawn:

    #Variables
    material = 1 #Value of material
    value = 1 #Fluid value of the piece
    char = 'P' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Piece-Square map multiplier (used in isolated evaluation of pieces)
    PSM = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 1,
        9: 1,
        10: 1,
        11: 1,
        12: 1,
        13: 1,
        14: 1,
        15: 1,
        16: 1.05,
        17: 1.05,
        18: 1.05,
        19: 1.15,
        20: 1.15,
        21: 0.85,
        22: 1,
        23: 1.05,
        24: 1,
        25: 1,
        26: 1.15,
        27: 1.21,
        28: 1.21,
        29: 0.85,
        30: 0.95,
        31: 0.95,
        32: 1,
        33: 1,
        34: 1.1,
        35: 1.15,
        36: 1.15,
        37: 1,
        38: 1,
        39: 1,
        40: 1.05,
        41: 1.05,
        42: 1.12,
        43: 1.17,
        44: 1.17,
        45: 1.05,
        46: 1.05,
        47: 1.05,
        48: 1.07,
        49: 1.07,
        50: 1.15,
        51: 1.2,
        52: 1.2,
        53: 1.07,
        54: 1.07,
        55: 1.07,
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

    #Get Moves method
    def getMoves(self, board, cRow, cCol):
        moves = []

        #If on starting row, add a double move, if possible
        if cRow == 1:
            if board[2][cCol].material == 0 and board[3][cCol].material == 0:
                moves.append(cRow + cCol*10 + (cRow+2)*100 + cCol*1000)

        if cRow+1 <= 7:
            #Add single move
            if board[cRow+1][cCol].material == 0:
                moves.append(cRow + cCol*10 + (cRow+1)*100 + cCol*1000)

            #Capture right
            if cCol+1 <= 7 and board[cRow+1][cCol+1].material < 0:
                moves.append(cRow + cCol*10 + (cRow+1)*100 + (cCol+1)*1000)

            #Capture left
            if cCol-1 >= 0 and board[cRow+1][cCol-1].material < 0:
                moves.append(cRow + cCol*10 + (cRow+1)*100 + (cCol-1)*1000)

        return moves

    # Enpassent (same code in moves as a normal move)
    def enpassent(self, board, cRow, cCol, bHLength, previousBoard):
        #Skip if this is the first move of the game (to avoid index exceptions)
        if bHLength == 0:
            return []
        #Check if a pawn of the opposite color is beside you to the left
        if cCol-1 >= 0 and cRow == 4:
            if board[cRow][cCol-1].material == -1 and board[cRow+2][cCol-1].material == 0:
                #Check if there was a pawn on the 2nd row
                if previousBoard[cRow+2][cCol-1].material == -1:
                    return [cRow + cCol*10 + (cRow+1)*100 + (cCol-1)*1000]
        #Check if a pawn of the opposite color is beside you to the left
        if cCol+1 <= 7 and cRow == 4:
            if board[cRow][cCol+1].material == -1 and board[cRow+2][cCol+1].material == 0:
                #Check if there was a pawn on the 2nd row
                if previousBoard[cRow+2][cCol+1].material == -1:
                    return [cRow + cCol*10 + (cRow+1)*100 + (cCol+1)*1000]
        return []
