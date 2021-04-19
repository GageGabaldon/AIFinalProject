from tkinter import *
import tkinter as tk
from Board import Board
from GUI import GUI
from Player import Player
from Computer import Computer
import sys
import time

"""
tieBreaker function that does sLD which we have in Computer class already
   whoever has the lowest sLD wins. if its equal: tie game
"""

class HalmaGame:
    def __init__(self, board, player, player2):
        self.player1 = player
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
        self.gui = GUI(self.tLimit, self.board, self)
        self.root = self.gui.root

        # create blank board using getGameArray return
        gameArray = board.boardArray
        self.gui.createBoard(self, gameArray)


    # main function that runs all the game logic on a click by click basis
    def buttonClicked(self, row, column):
        print(str(row) + ", " + str(column))
        if self.board.gameWon:
            return

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
            #self.gui.enableButtons(True)
            # check if they got a pice
            if self.player1.gotPiece:
                # if the player is clicking an already clicked piece
                if(self.player1.piece[0] == row and self.player1.piece[1] == column):
                    # check if the player has jumped a piece already
                    if(self.player1.hasHopped):
                        # call move generator again.
                        self.player1.moveGenerator((row, column))
                    else:
                        # no more valid moves to move too.
                        self.gui.setStatusString("Invalid move to move to already moved that piece")
                elif self.player1.isValidMoves((row, column)):
                    # update the board object and the ui
                    self.board.updateBoard(self.player1.piece, (row, column))
                    self.gui.updateGUI(self.board, self.player1.piece, (row, column), self.boardArray)
                    self.gui.highlight(self.boardArray[row][column], "highlight", self.player1.whatSide)
                    self.player1.piece = (row, column)
                else:
                    self.gui.setStatusString("Invalid move to move, select again")
            else:
                # check if the click position is a piece to move
                if self.player1.isValidPiece((row, column)):
                    # generate all the moves that piece can move to
                    self.player1.moveGenerator((row, column))
                    self.player1.piece = (row, column)
                    self.player1.gotPiece = True
                    self.gui.highlight(self.boardArray[row][column], "highlight", self.player1.whatSide)

                else:
                    self.gui.setStatusString("Invalid piece to move. Please select a valid piece")

        # check if game won before continuing
        if(self.player1.turn):
            print(f"It is {self.player1.whatSide}'s turn.")
            if(self.board.winCondition(self.player1.whatSide, False)):
                self.gui.setStatusString("Player 1 has won")
        else:
            if(self.board.winCondition(self.player2.whatSide, False)):
                self.gui.setStatusString("Player 2 has won") # CHANGE TO COMPUTER HAS WON

    def checkForComputer(self):
        # check if end turn happened
        if self.board.endTurnHappened:
            if self.player1.turn:
                self.player1.endTurn()
                self.player2.turn = True
            else:
                self.player2.endTurn()
                self.player1.turn = True

            # set the board end clicked to false
            self.board.endTurnHappened = False

        # if it is not player's turn
        if self.player2.turn:
            self.computerMove()

    def computerMove(self):

        computer = self.player2

        bestBoardValue, bestBoardMove, prunes, numMoves = computer.boardStates()

        piece = bestBoardMove[0]
        pieceCoord = piece.boardPos
        moveCoord = bestBoardMove[1]

        self.board.updateBoard(piece.boardPos, moveCoord)
        self.gui.updateGUI(self.board, pieceCoord, moveCoord, self.boardArray)
        # highlight the move made
        self.gui.highlight(self.boardArray[pieceCoord[0]][pieceCoord[1]], "highlight", self.player2.whatSide)
        self.gui.highlight(self.boardArray[moveCoord[0]][moveCoord[1]], "highlight", self.player2.whatSide)
        computer.piece = moveCoord

        if self.player1.turn:
            won = self.board.winCondition(self.player1.whatSide, False)
            print(won)
            if won:
                self.gui.setStatusString("Player 1 has won")
        else:
            won = self.board.winCondition(self.player2.whatSide, False)
            print(won)
            if(won):
                self.gui.setStatusString("Player 2 has won") # CHANGE TO COMPUTER HAS WON

        self.gui.endTurnClicked()

def main():
    size = 8
    time = 4
    whatSide = "green"
    board = Board(size, time, whatSide)
    board.getBoardInfo()
    # move a red piece to a closer green piece with update board just give it two cord and it will update board
    player = Player(board, whatSide, myTurn = True)
    #player2 = Player(board, "red", myTurn = False)
    computer = Computer(size, board, "red", False, time, ab=True)
    """
    board.updateBoard((0, 4), (0, 3))
    value = computer.utility(board, "red")
    print(value)
    board.updateBoard((0, 3), (0, 4))
    board.updateBoard((0, 4), (1, 3))
    value = computer.utility(board, "red")
    print(value)
    board.updateBoard((1, 3), (0, 4))
    board.updateBoard((0, 4), (0,0))
    value = computer.utility(board, "red")
    board.updateBoard((0, 0), (0, 4))
    print(value)
    """
    #game = HalmaGame(board, player, player2)
    game = HalmaGame(board, player, computer)
    game.root.mainloop()

if __name__ == "__main__":
    main()

# make buttons stay highlighted when clicked
# unhighlight when clicked again
