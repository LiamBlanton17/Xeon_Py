# Class for the Empty Square

class Empty:

    #Variables
    material = 0 #Value of material
    value = 0 #Fluid value of the piece
    char = '-' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Return the pieces character
    def GetChar(self):
        return self.char

    #Method to get an isolated eval of this piece
    def getEval(self, row, col):
        return 0

    #Empty function for get moves
    def getMoves(self, board, cRow, cCol):
        return []
