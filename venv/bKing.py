# Class for the Black King

class bKing:

    #Variables
    material = -1000 #Value of material
    value = -1000 #Fluid value of the piece
    char = 'k' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Return the pieces character
    def GetChar(self):
        return self.char

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
