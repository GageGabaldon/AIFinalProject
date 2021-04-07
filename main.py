from Board import Board
from GUI import GUI
from Player import Player
from Computer import Computer

class Main:

    # get the information from the user such as boardsisze, timelimit, which player moves first etc etc
    def __init__(self, size, timeLimit, whatSide):
        self.size = size
        self.timeLimit = timeLimit
        self.whatSide = whatSide

    def main(self):

            # initialize the board, gui and player
            board = Board(self.size, self.timeLimit, self.whatSide)
            gui = GUI(board)
            player = Player(board, gui, self.whatSide)
            computer = Computer(board, gui, self.whatSide)

            # main run function
            while not board.gameWon:
                # move the player that is green first
                if(player.whatSide == "green"):
                    piece = player.getPiece()
                    while player.avaiableMoves() and not player.turnDone() and board.time():
                        position = player.nextMove()
                        valid = board.isValid(piece, position)
                        if(valid):
                            board.move(piece, position)
                        else:
                            gui.printStatus("Invalid move")
                    gui.printStatus("IM THINKING")
                    computer.move()
                else:
                    gui.printStatus("IM THINKING")
                    computer.move()