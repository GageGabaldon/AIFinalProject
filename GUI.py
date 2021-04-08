from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import time

class GUI:

    def __init__(self, time, board):
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

        self.boardObject = board

        # call a window creator class
        self.root = tk.Tk() # main window
        self.root.geometry("1000x1000")
        self.root.title("Halma Game") # window name
        self.root.after(1000, self.update_clock)

        self.mainWindow = tk.Frame(self.root, width = 800, height = 800) # frame holding nxn board
        self.mainWindow.pack()

        # create timer above board
        self.clock = StringVar()
        self.timer = tk.Label(self.mainWindow, text = self.clock, justify = "center")
        self.clock.set("0:00:00")
        self.timer.columnconfigure(0)
        self.timer.pack()

        # create board frame
        self.boardOuter = tk.Frame(self.mainWindow, width = 1000, height = 1000) # frame holding nxn board
        self.boardOuter.columnconfigure(1)
        self.boardOuter.pack()

        self.board = tk.Frame(self.boardOuter)
        self.board.grid(row = 1, column = 1)

        # create status label below board
        self.statusString = StringVar()
        self.statusLabel = tk.Label(self.mainWindow, textvariable = self.statusString, justify = "center")
        self.statusString.set("Game Start!")
        self.statusLabel.columnconfigure(2)
        self.statusLabel.pack()

        # create end turn button below status label
        self.endTurnButton = tk.Button(self.mainWindow, text = "End Turn", command = self.endTurnButton)
        self.endTurnButton.columnconfigure(3)  
        self.endTurnButton.pack()

        # start the timer
        self.timer.after(1000, self.update_clock)
        self.timeLimit = time
        self.update_clock()

    def createBoardLabels(self, bSize):
        # create label frames
        leftLabels = tk.Frame(self.boardOuter)
        leftLabels.grid(row = 1, column = 0)
        topLabels = tk.Frame(self.boardOuter)
        topLabels.grid(row = 0, column = 1)

        # loop create left 1-bSize labels in column
        for x in range(1, bSize + 1):
            label = tk.Label(leftLabels, text = str(x), width = 1, height = 3)
            label.grid(row = x, column = 0)

        # loop create top a-bSize letter labels in row
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]
        boardAlphabet = alphabet[0 : bSize]
        for letter in boardAlphabet:
            label = tk.Label(topLabels, text = letter, width = 6, height = 1)
            label.grid(row = 0, column = alphabet.index(letter))
        

    def createBoard(self, halmaGame, gameArray):
        self.board.width = halmaGame.bSize * 40
        self.board.height = halmaGame.bSize * 40
        tempArray = []

        # loop through game array for posInfo
        for row in range(0, halmaGame.bSize):
            tempArray = []
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
                tempArray.append(button)
                button.grid(row=row, column=column)

            halmaGame.boardArray.append(tempArray)
        self.createBoardLabels(halmaGame.bSize)

    def resetTimer(self, halmaGame):
        pass

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.timer.configure(text=now)
        self.timer.after(1000, self.update_clock)

    def updateGUI(self, board, piece, newPos, buttonArray):
        pos1Info = board.boardArray[piece[0]][piece[1]]
        pos2Info = board.boardArray[newPos[0]][newPos[1]]

        pos1Button = buttonArray[pos1Info.boardPos[0]][pos1Info.boardPos[1]]
        pos2Button = buttonArray[pos2Info.boardPos[0]][ pos2Info.boardPos[1]]

        for posInfo in [pos1Info, pos2Info]:
            image = None
            #blank squares
            if posInfo.goal == "grey" and pos1Info.color == "none":
                image = Image.open(self.blank_greys)
            elif posInfo.goal == "white" and pos1Info.color == "none":
                image = Image.open(self.blank_whites)
            elif posInfo.goal == "goal" and pos1Info.color == "none":
                image = Image.open(self.blank_tans)
            # green piece squares
            elif posInfo.goal == "white" and pos1Info.color == "green":
                image = Image.open(self.greenp_whites)
            elif posInfo.goal == "grey" and pos1Info.color == "green":
                image = Image.open(self.greenp_greys)
            elif posInfo.goal == "goal" and pos1Info.color == "green":
                image = Image.open(self.greenp_goals)
            # red squares
            elif posInfo.goal == "white" and pos1Info.color == "red":
                image = Image.open(self.redp_whites)
            elif posInfo.goal == "grey" and pos1Info.color == "red":
                image = Image.open(self.redp_greys)
            else:
                image = Image.open(self.redp_goals)

            if posInfo == pos1Info:
                pos1Button.image = image
            else:
                pos2Button.image = image

    def endTurnButton(self):
        self.boardObject.endTurnHappened = True
        self.setStatusString("Player Ended Turn")

    def setStatusString(self, string):
        print(string)
        self.statusString.set(string)
