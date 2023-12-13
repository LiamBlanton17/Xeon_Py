# Board Class

# Import all other classes

# Class
class Board:

    # Variables
    eval = 0  # Evaluation of board
    material = 0  # Material on the board

    # Constructor
    def __init__(self, board):
        self.board = board.copy()  # Setting the board of the object (2d array of pieces)
        self.moves = self.generateMoves()  # Generate moves from current board


    # Methods

    # Method to print the board to the console
    # TO DO: Swap which way it prints depending on who's move it is
    def PrintBoard(self):
        for row in range(7, -1, -1):
            print(row+1, end=" ")
            for col in range(8):
                print(self.board[row][col].char, end=" ")
            print()
        print("  A B C D E F G H")
        print()

    # Method to get material of the board

    # Method to get evaluation of the board

    # Method to generate move, children board pairs
    def generateMoves(self):
        moves = []
        #Loop over each piece in the board
        for row in range(8):
            for col in range(8):
                moves.extend(self.board[row][col].getMoves(self.board, row, col))
        #Remove moves resulting in check
        #Check for 3fold, check for 50move
        #Check for mate
        return moves
