# Class for the White Pawn

class wPawn:

    #Variables
    material = 1 #Value of material
    value = 1 #Fluid value of the piece
    char = 'P' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Get Moves method
    def getMoves(self, board, cRow, cCol):
        moves = []

        #If on starting row, add a double move, if possible
        if cRow == 1:
            if board[2][cCol].material == 0 and board[3][cCol].material == 0:
                target = cRow + cCol*10 + (cRow+2)*100 + cCol*1000
                moves.append(target)

        #Add single move
        if cRow+1 <= 7 and board[cRow+1][cCol].material == 0:
            target = cRow + cCol*10 + (cRow+1)*100 + cCol*1000
            moves.append(target)

        #Capture right
        if cRow+1 <= 7 and cCol+1 <= 7 and board[cRow+1][cCol+1].material < 0:
            target = cRow + cCol*10 + (cRow+1)*100 + (cCol+1)*1000
            moves.append(target)

        #Capture left
        if cRow+1 <= 7 and cCol-1 >= 0 and board[cRow+1][cCol-1].material < 0:
            target = cRow + cCol*10 + (cRow+1)*100 + (cCol-1)*1000
            moves.append(target)

        #Create Enpassant

        #CREATE PROMOTION

        return moves