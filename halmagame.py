from tkinter import *
import tkinter as tk
from Board import Board
from GUI import GUI
from Player import Player 
import sys

class HalmaGame:
    def __init__(self, board):
        pass

    def __init__(self, board, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = board

        # command line arguments given by main
        self.bSize = board.bSize
        self.tLimit = board.timeLimit
        self.hPlayer = board.whatSide
        self.filename = None
        self.boardArray = []


        # call a window creator class
        # create GUI (main window, configured columns/ frames, etc..)
        self.gui = GUI()
        self.root = self.gui.root

        # create blank board using getGameArray return
        gameArray = board.boardArray
        self.gui.createBoard(self, gameArray)
        self.gui.update_clock()

    def buttonClicked(self, row, column):
        print(str(row) + ", " + str(column))

        if self.player1.turn:

            if self.player1.gotPiece:
                if self.player1.isValid((row, column)):
                    self.board.updateBoard(self.player1.piece, (row, column))
                    gui.updateUI()

                    if not self.player1.turn:
                        self.player1.endTurn()

                    # call the computer
                else:
                    self.setStatusString("Invalid move")
            else:
                if self.player1.isValidPiece((row, column)):
                    self.player1.moveGenerator((row, column))
                    self.player1.piece = (row, column)
                else:
                    self.gui.setStatusString("Invalid move please select a valid piece")

        # player two logic
        else:
            pass

        if(self.board.gameWon):
            self.setStatusString("you won")


    # updates the board based on what pieces have been moved at what coordinate and to what coordinate
    def update(self):
        pass


def main():
    size = 16
    time = 1
    whatSide = "green"
    board = Board(size, time, whatSide)
    board.getBoardInfo()
    player1 = Player(board, whatSide, myTurn = True)
    player2 = Player(board, whatSide = "green", myTurn = False)
    game = HalmaGame(board, player1, player2)
    game.root.mainloop()

if __name__ == "__main__":
    main()

# make buttons stay highlighted when clicked 
# unhighlight when clicked again