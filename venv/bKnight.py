# Class for the Black Knight

class bKnight:

    #Variables
    material = -3 #Value of material
    value = -3 #Fluid value of the piece
    char = 'n' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Return the pieces character
    def GetChar(self):
        return self.char

    #Get Moves method
    def getMoves(self, board, cRow, cCol):
        moves = []
        #Check up-right
        if not (cRow+2 > 7 or cCol+1 > 7 or board[cRow+2][cCol+1].material < 0):
            target = cRow + cCol*10 + (cRow+2)*100 + (cCol+1)*1000
            moves.append(target)
        #Check up-left
        if not (cRow+2 > 7 or cCol-1 < 0 or board[cRow+2][cCol-1].material < 0):
            target = cRow + cCol*10 + (cRow+2)*100 + (cCol-1)*1000
            moves.append(target)
        #Check right-up
        if not (cRow+1 > 7 or cCol+2 > 7 or board[cRow+1][cCol+2].material < 0):
            target = cRow + cCol*10 + (cRow+1)*100 + (cCol+2)*1000
            moves.append(target)
        #Check right-down
        if not (cRow-1 < 0 or cCol+2 > 7 or board[cRow-1][cCol+2].material < 0):
            target = cRow + cCol*10 + (cRow-1)*100 + (cCol+2)*1000
            moves.append(target)
        #Check left-up
        if not (cRow+1 > 7 or cCol-2 < 0 or board[cRow+1][cCol-2].material < 0):
            target = cRow + cCol*10 + (cRow+1)*100 + (cCol-2)*1000
            moves.append(target)
        #Check left-down
        if not (cRow-1 < 0 or cCol-2 < 0 or board[cRow-1][cCol-2].material < 0):
            target = cRow + cCol*10 + (cRow-1)*100 + (cCol-2)*1000
            moves.append(target)
        #Check down-right
        if not (cRow-2 < 0 or cCol+1 > 7 or board[cRow-2][cCol+1].material < 0):
            target = cRow + cCol*10 + (cRow-2)*100 + (cCol+1)*1000
            moves.append(target)
        #Check down-left
        if not (cRow-2 < 0 or cCol-1 < 0 or board[cRow-2][cCol-1].material < 0):
            target = cRow + cCol*10 + (cRow-2)*100 + (cCol-1)*1000
            moves.append(target)
        return moves
