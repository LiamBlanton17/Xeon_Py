# Class for the Empty Square

class Empty:

    #Variables
    material = 0 #Value of material
    value = 0 #Fluid value of the piece
    char = '-' #Char to represent piece

    #Constructor
    def __init__(self):
        pass

    #Empty function for get moves
    def getMoves(self, board, cRow, cCol):
        return []
