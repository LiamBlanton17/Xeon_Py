# Class for the Black Bishop

class bBishop:

    #Variables
    material = -3 #Value of material
    value = -3 #Fluid value of the piece
    char = 'b' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Piece-Square map multiplier (used in isolated evaluation of pieces)
    PSM = {
        0: -2.85,
        1: -2.85,
        2: -2.9,
        3: -2.85,
        4: -2.85,
        5: -2.9,
        6: -2.85,
        7: -2.85,
        8: -2.95,
        9: -3,
        10: -3,
        11: -2.9,
        12: -2.9,
        13: -3,
        14: -3,
        15: -2.95,
        16: -3,
        17: -3.05,
        18: -3.05,
        19: -3.05,
        20: -3.05,
        21: -3.05,
        22: -3.05,
        23: -3,
        24: -3,
        25: -3.1,
        26: -3.05,
        27: -3,
        28: -3,
        29: -3.05,
        30: -3.1,
        31: -3,
        32: -3,
        33: -3.05,
        34: -3.15,
        35: -2.95,
        36: -2.95,
        37: -3.15,
        38: -3.05,
        39: -3,
        40: -2.95,
        41: -3,
        42: -3,
        43: -2.9,
        44: -2.9,
        45: -3,
        46: -3,
        47: -2.95,
        48: -2.9,
        49: -3.05,
        50: -2.95,
        51: -2.95,
        52: -2.95,
        53: -2.95,
        54: -3.05,
        55: -2.9,
        56: -2.85,
        57: -2.85,
        58: -2.9,
        59: -2.85,
        60: -2.85,
        61: -2.9,
        62: -2.85,
        63: -2.85
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
        return moves
