class Player:

    def __init__(self, board, whatSide, myTurn):
        self.board = board
        self.whatSide = whatSide
        self.turn = myTurn
        self.gotPiece = False
        self.piece = (-1, -1)
        self.validMoves = []

    def nextMove(self):
        nextMove = self.gui.nextMove()
        return nextMove

    def validMoves(self, coord):
        if coord in self.validMoves:
            return True
        else:
            return False

    def isValidPiece(self, cord):
        pos = self.board.boardArray[cord[0]][cord[1]]
        if(pos.piece):
            return True

        return False

    def endTurn(self):
        self.turn = False
        self.piece = (-1, -1)
        self.gotPiece = False
        self.validMoves = []

    # do move generator logic and save into valid moves for later
    def moveGenerator(self, cord):
        pass





