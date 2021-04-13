class Computer:

    def __init__(self, board, whatSide, myTurn):
        self.board = board
        self.whatSide = whatSide
        self.turn = myTurn


    def MakeAMove(self):
        pass

    # this prunes the sub trees of the search space.
    def AlphaPrunning(self):
        pass

    # this just compares every piece to the goal using a distance formula
    def winning(self):
        pass



