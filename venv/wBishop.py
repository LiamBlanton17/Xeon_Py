# Class for the White Bishop

class wBishop:

    #Variables
    material = 3 #Value of material
    value = 3 #Fluid value of the piece
    char = 'B' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Piece-Square map multiplier (used in isolated evaluation of pieces)
    PSM = {
        0: 2.85,
        1: 2.85,
        2: 2.9,
        3: 2.85,
        4: 2.85,
        5: 2.9,
        6: 2.85,
        7: 2.85,
        8: 2.9,
        9: 3.05,
        10: 2.95,
        11: 2.95,
        12: 2.95,
        13: 2.95,
        14: 3.05,
        15: 2.9,
        16: 2.95,
        17: 3,
        18: 3,
        19: 2.9,
        20: 2.9,
        21: 3,
        22: 3,
        23: 2.95,
        24: 3,
        25: 3.05,
        26: 3.15,
        27: 2.95,
        28: 2.95,
        29: 3.15,
        30: 3.05,
        31: 3,
        32: 3,
        33: 3.1,
        34: 3.05,
        35: 3,
        36: 3,
        37: 3.05,
        38: 3.1,
        39: 3,
        40: 3,
        41: 3.05,
        42: 3.05,
        43: 3.05,
        44: 3.05,
        45: 3.05,
        46: 3.05,
        47: 3,
        48: 2.95,
        49: 3,
        50: 3,
        51: 2.9,
        52: 2.9,
        53: 3,
        54: 3,
        55: 2.95,
        56: 2.85,
        57: 2.85,
        58: 2.9,
        59: 2.85,
        60: 2.85,
        61: 2.9,
        62: 2.85,
        63: 2.85
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
        return moves
