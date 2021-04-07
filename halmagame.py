from tkinter import *
import tkinter as tk
import sys
from PIL import Image, ImageTk

class HalmaGame:
    
    def __init__(self, boardSize, timeLimit, whatSide):
        # file names for button images
        self.redp_whites = "redpiece_whitesquare.JPG"
        self.redp_tans = "redpiece_tansquare.JPG"
        self.redp_greys = "redpiece_greysquare.JPG"

        self.greenp_whites = "greenpiece_whitesquare.JPG"
        self.greenp_tans = "greenpiece_tansquare.JPG"
        self.greenp_greys = "greenpiece_greysquare.JPG"

        self.blank_whites = "blank_whitesquare.JPG"
        self.blank_tans = "blank_tansquare.JPG"
        self.blank_greys = "blank_greysquare.JPG"

        # command line arguments given by main
        self.bSize = boardSize
        self.tLimit = timeLimit
        self.hPlayer = whatSide
        self.filename = None

        # keep track of previously clicked buttons (since two spaces need to be clicked for move)
        self.firstClicked = False
        self.firstButton = None

        # call a window creator class
        self.root = tk.Tk() # main window
        self.root.geometry("1000x1000")
        self.root.title("Halma Game") # window name

        # create blank board using getGameArray return
        gameArray = self.getGameArray()
        self.createBoard(gameArray)

    # builds GUI window
    def getGameArray():
        columnArray = []
        rowArray = []
        goalStates = []
        if(self.bSize == 8):
            redgoal = [(0, 7), (0, 6), (0, 5), (0, 4), (1, 5), (1, 6), (1, 7), (2, 6), (2, 7), (3, 7)]
            greenGoal = [(4, 0), (5, 0), (6, 0), (7, 0), (5, 1), (6, 1), (7, 1), (6, 2), (7, 2), (7, 3)]
        elif(self.bSize == 10):
            return 1 # temporary
        else:
            return 2 # temporary

        for col in range(0, self.bSize):
            rowArray = []
            for row in range(0, self.bSize):
                if (row, col) in redgoal:
                    boardInfo = PosInfo((row, col), True, "red", True)
                    rowArray.append(boardInfo)

                elif (row, col) in greenGoal:
                    boardInfo = PosInfo((row, col), True, "green", True)
                    rowArray.append(boardInfo)

                else:
                    boardInfo = PosInfo((row, col), False, "none", False)
                    rowArray.append(boardInfo)

            columnArray.append(rowArray)

        return columnArray
    
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
                elif

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
                                    command=lambda : self.buttonClicked(row, column), 
                                    #text = "b", 
                                    image = buttonImage)
                    button.image = buttonImage
                button.configure(height = 40, width = 40)
                self.boardArray.append(button)
                button.grid(row=row, column=column)
        

    def buttonClicked(self, thisButton, row, column):
        button.config(relief = solid)
        # if first_clicked == True, this means this button is the second clicked element
        if self.first_clicked:
            verify(self.firstButton, self.thisButton)
        # reset whether the game move was successful or not
        self.firstButton.config(relief = raised)
        self.firstButton = None
        self.thisButton.config(relief = raised.)
        self.firstClicked = None



    # Display messages from program outlining what is going on
    def statusString():
        pass

class PosInfo:
    def __init__(self, boardPos, piece, color, goal):
        self.boardPos = boardPos
        self.piece = piece
        self.color = color
        self.goal = goal

    def getPos(self):
        return self.boardPos

    def hasPiece(self):
        return self.piece

    def pieceColor(self):
        return self.color

    def goal(self):
        return self.goal


def main():
    game = HalmaGame()
    game.root.mainloop()

if __name__ == "__main__":
    main()


# make buttons stay highlighted when clicked 
# unhighlight when clicked again