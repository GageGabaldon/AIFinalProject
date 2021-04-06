class Computer:

    def __init__(self, board, gui, whatSide):
        self.board = board
        self.gui = gui
        if(whatSide == "green"):
            self.whatSide = "red"
        else:
            self.whatSide = "green"



