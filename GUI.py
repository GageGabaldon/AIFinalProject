from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
class GUI:

    def __init__(self):
        # find square images
        self.redp_whites = "images/redpiece_whitesquare.JPG"
        self.redp_tans = "images/redpiece_tansquare.JPG"
        self.redp_greys = "images/redpiece_greysquare.JPG"

        self.greenp_whites = "images/greenpiece_whitesquare.JPG"
        self.greenp_tans = "images/greenpiece_tansquare.JPG"
        self.greenp_greys = "images/greenpiece_greysquare.JPG"

        self.blank_whites = "images/blank_whitesquare.JPG"
        self.blank_tans = "images/blank_tansquare.JPG"
        self.blank_greys = "images/blank_greysquare.JPG"

        # call a window creator class
        self.root = tk.Tk() # main window
        self.root.geometry("1000x1000")
        self.root.title("Halma Game") # window name
        self.mainWindow = tk.Frame(self.root, bg = "black", width = 800, height = 800) # frame holding nxn board
        self.mainWindow.pack()

        # create timer above board
        self.clock = StringVar()
        self.timer = tk.Label(self.mainWindow, textvariable = self.clock, justify = "center")
        self.clock.set("0:00:00")
        self.timer.columnconfigure(0)
        self.timer.pack()

        # create board frame
        self.board = tk.Frame(self.mainWindow, bg = "black", width = 600, height = 600) # frame holding nxn board
        self.board.columnconfigure(1)
        self.board.pack()

        # create status label below board
        self.statusString = StringVar()
        self.statusLabel = tk.Label(self.mainWindow, textvariable = self.statusString, justify = "center")
        self.statusString.set("Game Start!")
        self.statusLabel.columnconfigure(2)
        self.statusLabel.pack()

    def createBoard(self, halmaGame, gameArray):
        # CREATE EMPTY BOARD
        self.board = self.board
        self.board.pack()

        for row in range(0, halmaGame.bSize):
            for column in range(0, halmaGame.bSize):
                # calls button clicked and passes in the button object
                button = None
                # position info for current row/column location
                posInfo = gameArray[row][column] # boardPos, piece, color, goal
                
                image = None
                # grey squares
                if posInfo.goal == "grey":
                    image = Image.open(self.blank_greys)
                # white squares
                elif posInfo.goal == "white":
                    image = Image.open(self.blank_whites)
                # goal squares
                else: 
                    if posInfo.color == "green":
                        image = Image.open(self.greenp_tans)
                    else:
                        image = Image.open(self.redp_tans)
        
                # image now properly set, configure 
                image.resize((10,10), Image.ANTIALIAS)
                buttonImage = ImageTk.PhotoImage(image)
                button = tk.Button(self.board,
                                    command = lambda c = (row, column): halmaGame.buttonClicked(c[0], c[1]), 
                                    #text = "b", 
                                    image = buttonImage)
                button.image = buttonImage
                button.configure(height = 40, width = 40)
                halmaGame.boardArray.append(button)
                button.grid(row=row, column=column)    

    def resetTimer(self, halmaGame):
        pass

    def setStatusString(self, string):
        self.statusString.set(string)
