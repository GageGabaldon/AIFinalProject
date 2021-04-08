class Player:

    def __init__(self, board,  whatSide, myTurn):
        self.board = board
        self.whatSide = whatSide
        self.turn = myTurn
        self.gotPiece = False
        self.validMoves = []

    def nextMove(self):
        nextMove = self.gui.nextMove()
        return nextMove

    def validMoves(self, coord):
        if coord in self.validMoves:
            return True
        else:
            return False



