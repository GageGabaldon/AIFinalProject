from tkinter import *
import tkinter as tk
from Board import Board
from PIL import Image, ImageTk

class HalmaGame:
    
    def __init__(self, board):
        # file names for button images
        self.redp_whites = "images/redpiece_whitesquare.JPG"
        self.redp_tans = "images/redpiece_tansquare.JPG"
        self.redp_greys = "images/redpiece_greysquare.JPG"

        self.greenp_whites = "images/greenpiece_whitesquare.JPG"
        self.greenp_tans = "images/greenpiece_tansquare.JPG"
        self.greenp_greys = "images/greenpiece_greysquare.JPG"

        self.blank_whites = "images/blank_whitesquare.JPG"
        self.blank_tans = "images/blank_tansquare.JPG"
        self.blank_greys = "images/blank_greysquare.JPG"
        self.board = board


        # command line arguments given by main
        self.bSize = board.bSize
        self.tLimit = board.timeLimit
        self.hPlayer = board.whatSide
        self.filename = None
        self.boardArray = []

        # keep track of previously clicked buttons (since two spaces need to be clicked for move)
        self.firstClicked = False
        self.firstButton = None

        # call a window creator class
        self.root = tk.Tk() # main window
        self.root.geometry("1000x1000")
        self.root.title("Halma Game") # window name

        # create blank board using getGameArray return
        gameArray = board.boardArray
        self.createBoard(gameArray)

    
    def createBoard(self, gameArray):
        # CREATE EMPTY BOARD
        self.board = tk.Frame(self.root, bg = "black", width = 600, height = 600) # frame holding nxn board
        self.board.pack()

        for row in range(0, self.bSize):
            for column in range(0, self.bSize):
                # calls button clicked and passes in the button object
                button = None
                # position info for current row/column location
                posInfo = gameArray[row][column] # boardPos, piece, color, goal
                
                image = None
                # grey squares
                if ((row % 2 == 0) and (column % 2 != 0)) or ((row % 2 != 0 and column % 2 == 0)):
                    if posInfo.piece == True and posInfo.color == "red":
                        image = Image.open(self.redp_greys)
                    elif posInfo.piece == True and posInfo.color == "green":
                        image = Image.open(self.greenp_greys)
                    else:
                        image = Image.open(self.blank_greys)
                # tan squares
                # white squares
                else: 
                    image = None
                    # find color of piece or if blank square
                    if posInfo.piece == True and posInfo.color == "red":
                        image = Image.open(self.redp_whites)
                    elif posInfo.piece == True and posInfo.color == "green":
                        image = Image.open(self.greenp_whites)
                    else:
                        image = Image.open(self.blank_whites)

                # image now properly set, configure 
                image.resize((10,10), Image.ANTIALIAS)
                buttonImage = ImageTk.PhotoImage(image)
                button = tk.Button(self.board,
                                    command=lambda c = (row, column): self.buttonClicked(c[0], c[1]),
                                    #text = "b", 
                                    image = buttonImage)
                button.image = buttonImage
                button.configure(height = 40, width = 40)
                self.boardArray.append(button)
                button.grid(row=row, column=column)
        
    """
        button.config(relief = solid)
        # if first_clicked == True, this means this button is the second clicked element
        if self.first_clicked:
            verify(self.firstButton, self.thisButton)
        # reset whether the game move was successful or not
        self.firstButton.config(relief = raised)
        self.firstButton = None
        self.thisButton.config(relief = raised.)
        self.firstClicked = None
    """

    def buttonClicked(self, row, column):
        print(str(row), str(column))
        self.firstClicked = (row, column)


    def lastClicked(self):
        return self.firstClicked

    # Display messages from program outlining what is going on
    def statusString(self):
        pass

    # sets the status string to be displayed to the user
    def setStatusString(self):
        pass

    # updates the board based on what pieces have been moved at what coordinate and to what coordinate
    def update(self):
        pass

    # returns the pos of the click
    def getClicked(self):
        pass

def main():
    size = 8
    time = 1
    whatSide = "green"
    board = Board(size, time, whatSide)
    board.updateBoard((4, 0), (0, 0))
    board.getBoardInfo()

    game = HalmaGame(board)
    game.root.mainloop()

if __name__ == "__main__":
    main()


# make buttons stay highlighted when clicked 
# unhighlight when clicked again