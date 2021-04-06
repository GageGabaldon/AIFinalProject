class Player:

    def __init__(self, board, gui, whatSide):
        self.board = board
        self.gui = gui
        self.whatSide = whatSide

    def nextMove(self):
        nextMove = self.gui.nextMove()

        return nextMove


