from Board import Board
from GUI import GUI
from Player import Player
from halmagame import HalmaGame
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
            player2 = None
            if(self.whatSide == "green"):
                player2 = Player(board, gui, "red")
            else:
                player2 = Player(board, gui, "green")

            # for later
            #computer = Computer(board, gui, self.whatSide)

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

def main():
    size = 8
    time = 1
    whatSide = "green"
    board = Board(size, time, whatSide)
    player = Player(board, whatSide, True)
    player2 = Player(board, "red", False)
    game = HalmaGame(board, player, player2)
    game.root.mainloop()

main()








