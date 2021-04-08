class Player:

    def __init__(self, board,  whatSide, myTurn):
        self.board = board
        self.whatSide = whatSide
        self.turn = myTurn
        self.gotPiece = False

    def nextMove(self):
        nextMove = self.gui.nextMove()
        return nextMove



