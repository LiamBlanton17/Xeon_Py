# Class for the White Queen

class wQueen:

    #Variables
    material = 9 #Value of material
    value = 9 #Fluid value of the piece
    char = 'Q' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Piece-Square map multiplier (used in isolated evaluation of pieces)
    PSM = {
        0: 8.5,
        1: 8.5,
        2: 8.75,
        3: 8.95,
        4: 8.95,
        5: 8.75,
        6: 8.5,
        7: 8.5,
        8: 8.5,
        9: 8.95,
        10: 8.95,
        11: 8.95,
        12: 8.95,
        13: 8.95,
        14: 8.95,
        15: 8.5,
        16: 8.75,
        17: 9,
        18: 9,
        19: 9,
        20: 9,
        21: 9,
        22: 9,
        23: 8.75,
        24: 9,
        25: 9.2,
        26: 9.2,
        27: 9.05,
        28: 9.05,
        29: 9.2,
        30: 9.2,
        31: 9.05,
        32: 9,
        33: 9.05,
        34: 9.05,
        35: 9.05,
        36: 9.05,
        37: 9.05,
        38: 9.05,
        39: 9,
        40: 8.75,
        41: 9,
        42: 9,
        43: 9,
        44: 9,
        45: 9,
        46: 9,
        47: 8.75,
        48: 8.75,
        49: 9,
        50: 9,
        51: 9,
        52: 9,
        53: 9,
        54: 9,
        55: 8.75,
        56: 8.75,
        57: 9,
        58: 9,
        59: 9,
        60: 9,
        61: 9,
        62: 9,
        63: 8.75
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
