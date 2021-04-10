from tkinter import *
import tkinter as tk
from Board import Board
from GUI import GUI
from Player import Player
import sys

"""
TODO: Fix bug where piece disappears if you click a piece after making a move
TODO: Move generator doesnt work on board edges
TODO: Move generator doesnt hop over Piece
TODO: NEED to update the piece after a move and be able to move that piece again if a hop is available
      FOR EXAMPLE a moveGenerator that can change what moves are valid if the piece has moved once
      to only generate valid moves if those move jump an enemy piece

      TLDR: need to be able to move a piece again if it can hop over another pieces
TODO: Timer must start working and time down from the timeLimit to 0 at zero should change board.endTurnHappened
      to true that way the next player starts moving
TODO: Test if the game has been won
TODO: test the rest of the playign of the game.
"""

class HalmaGame:
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
        self.gui = GUI(self.tLimit, self.board)
        self.root = self.gui.root

        # create blank board using getGameArray return
        gameArray = board.boardArray
        self.gui.createBoard(self, gameArray)

    # main function that runs all the game logic on a click by click basis
    def buttonClicked(self, row, column):
        print(str(row) + ", " + str(column))

        # if the end turn button has been clicked reset player and switch turn
        if self.board.endTurnHappened:
            if self.player1.turn:
                self.player1.endTurn()
                self.player2.turn = True
            else:
                self.player2.endTurn()
                self.player1.turn = True
            # set the board end clicked to false
            self.board.endTurnHappened = False

        # check whos turn it is
        if self.player1.turn:
            # check if they got a pice
            if self.player1.gotPiece:
                # check if the move they are currently making is valid
                if self.player1.isValidMoves((row, column)):
                    # update the board object and the ui
                    self.board.updateBoard(self.player1.piece, (row, column))
                    self.gui.updateGUI(self.board, self.player1.piece, (row, column), self.boardArray)
                else:
                    self.gui.setStatusString("Invalid move to move, select again")
            else:
                # check if the click position is a piece to move
                if self.player1.isValidPiece((row, column)):
                    # generate all the moves that piece can move to
                    self.player1.moveGenerator((row, column))
                    self.player1.piece = (row, column)
                    self.player1.gotPiece = True
                else:
                    self.gui.setStatusString("Invalid piece to move. Please select a valid piece")

        # player two logic
        else:
            if self.player2.gotPiece:
                if self.player2.isValidMoves((row, column)):
                    self.board.updateBoard(self.player2.piece, (row, column))
                    self.gui.updateGUI(self.board, self.player2.piece, (row, column), self.boardArray)
                else:
                    self.gui.setStatusString("Invalid move to move to")
            else:
                if self.player2.isValidPiece((row, column)):
                    self.player2.moveGenerator((row, column))
                    self.player2.piece = (row, column)
                    self.player2.gotPiece = True
                else:
                    self.gui.setStatusString("Invalid piece please select a valid piece")

        # check if game won before continuing
        if(self.player1.turn):
            if(self.board.winCondition(self.player1.whatSide)):
                self.setStatusString("Player 1 has won")
        else:
            if(self.board.winCondition(self.player2.whatSide)):
                self.setStatusString("Player 2 has won")

def main():
    size = 8
    time = 1
    whatSide = "green"
    board = Board(size, time, whatSide)
    board.getBoardInfo()
    # move a red piece to a closer green piece with update board just give it two cord and it will update board
    # board.updateBoard((0,7), )
    player1 = Player(board, whatSide, myTurn = True)
    player2 = Player(board, "red", myTurn = False)
    game = HalmaGame(board, player1, player2)
    game.root.mainloop()

if __name__ == "__main__":
    main()

# make buttons stay highlighted when clicked
# unhighlight when clicked again
