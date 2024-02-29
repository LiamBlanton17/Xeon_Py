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

        return moves

    #Enpassent (same code in moves as a normal move)
    def enpassent(self, board, cRow, cCol, bHistory):
        #Skip if this is the first move of the game (to avoid index exceptions)
        if len(bHistory) == 0:
            return []
        #Check if a pawn of the opposite color is beside you to the left
        if cCol-1 >= 0 and cRow == 4:
            if board[cRow][cCol-1].material == -1 and board[cRow+2][cCol-1].material == 0:
                #Check if there was a pawn on the 2nd row
                if bHistory[len(bHistory)-1].GetBoard()[cRow+2][cCol-1].material == -1:
                    return [cRow + cCol*10 + (cRow+1)*100 + (cCol-1)*1000]
        #Check if a pawn of the opposite color is beside you to the left
        if cCol+1 <= 7 and cRow == 4:
            if board[cRow][cCol+1].material == -1 and board[cRow+2][cCol+1].material == 0:
                #Check if there was a pawn on the 2nd row
                if bHistory[len(bHistory)-1].GetBoard()[cRow+2][cCol+1].material == -1:
                    return [cRow + cCol*10 + (cRow+1)*100 + (cCol+1)*1000]
        return []
