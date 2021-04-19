from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import time

class GUI:

    def __init__(self, time, board, halmaGame):
        # find square images
        self.redp_whites = "images/redpiece_whitesquare.jpg"
        self.redp_tans = "images/redpiece_tansquare.jpg"
        self.redp_greys = "images/redpiece_greysquare.jpg"

        self.greenp_whites = "images/greenpiece_whitesquare.jpg"
        self.greenp_tans = "images/greenpiece_tansquare.jpg"
        self.greenp_greys = "images/greenpiece_greysquare.jpg"

        self.blank_whites = "images/blank_whitesquare.JPG"
        self.blank_tans = "images/blank_tansquare.JPG"
        self.blank_greys = "images/blank_greysquare.JPG"

        self.fadeGreenHex = "#92CA91"
        self.fadeRedHex = "#FF6961"
        self.defaultHex = "#F0F0F0"

        self.halmaGame = halmaGame
        self.boardObject = board
        self.buttonArray = []

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

        # create status string above board
        self.statusString = StringVar()
        self.statusLabel = tk.Label(self.mainWindow, textvariable = self.statusString, justify = "center")
        self.statusString.set("Game Start!")
        self.statusLabel.columnconfigure(1)
        self.statusLabel.pack()

        # create board frame
        self.boardOuter = tk.Frame(self.mainWindow, width = 1000, height = 1000) # frame holding nxn board
        self.boardOuter.columnconfigure(12)
        self.boardOuter.pack()

        self.board = tk.Frame(self.boardOuter)
        self.board.grid(row = 1, column = 1)

        # create whos turn label below board
        self.playerString = StringVar()
        self.playerLabel = tk.Label(self.mainWindow, textvariable = self.playerString, justify = "center")
        self.playerString.set("It is green's turn!")
        self.playerLabel.columnconfigure(3)
        self.playerLabel.pack()

        # create end turn button below status label
        self.endTurnButton = tk.Button(self.mainWindow, text = "End Turn", command = self.endTurnClicked)
        self.endTurnButton.columnconfigure(4)
        self.endTurnButton.pack()

        # start the timer
        self.timer.after(1000, self.update_clock)
        self.timeLimit = time
        self.update_clock()

        # variable that flips every time end turn is triggered to display whose turn it is
        self.whosTurn = "green"

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
                                    image = buttonImage,
                                    borderwidth = 3,
                                    bg = self.defaultHex)# default button color
                button.image = buttonImage
                button.configure(height = 40, width = 40)
                tempArray.append(button)
                button.grid(row=row, column=column)

            halmaGame.boardArray.append(tempArray)
            self.buttonArray.append(tempArray) 
        self.createBoardLabels(halmaGame.bSize)

    def resetTimer(self, halmaGame):
        pass

    def highlight(self, button, highlight, playerColor):
        if highlight == "highlight":
            # button.configure(relief = "solid")
            button.configure(bg = playerColor) # dark player color
        elif highlight == "fade":
            if playerColor == "green":
                print("set to faded greenhex")
                button.configure(bg = self.fadeGreenHex) # light green
            else:
                button.configure(bg = self.fadeRedHex) # light red
        # else unhighlight
        else:
            button.configure(bg = self.defaultHex) # default border color

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.timer.configure(text=now)
        self.timer.after(1000, self.update_clock)

    # the goal states are getting deleted and the piece is getting deleted
    def updateGUI(self, board, piece, newPos, buttonArray):
        print("Pieces: " + str(piece[0]) +  ", " + str(piece[1]))
        pos1Info = board.boardArray[piece[0]][piece[1]]
        pos2Info = board.boardArray[newPos[0]][newPos[1]]

        pos1Button = buttonArray[pos1Info.boardPos[0]][pos1Info.boardPos[1]]
        pos2Button = buttonArray[pos2Info.boardPos[0]][pos2Info.boardPos[1]]

        for posInfo in [pos1Info, pos2Info]:
            image = None
            #blank squares
            if posInfo.goal == "grey" and posInfo.color == "none":
                image = ImageTk.PhotoImage(Image.open(self.blank_greys))
            elif posInfo.goal == "white" and posInfo.color == "none":
                image = ImageTk.PhotoImage(Image.open(self.blank_whites))
            elif posInfo.goal == "goal" and posInfo.color == "none":
                image = ImageTk.PhotoImage(Image.open(self.blank_tans))
            # green piece squares
            elif posInfo.goal == "white" and posInfo.color == "green":
                image = ImageTk.PhotoImage(Image.open(self.greenp_whites))
            elif posInfo.goal == "grey" and posInfo.color == "green":
                image = ImageTk.PhotoImage(Image.open(self.greenp_greys))
            elif posInfo.goal == "goal" and posInfo.color == "green":
                image = ImageTk.PhotoImage(Image.open(self.greenp_tans))
            # red squares
            elif posInfo.goal == "white" and posInfo.color == "red":
                image = ImageTk.PhotoImage(Image.open(self.redp_whites))
            elif posInfo.goal == "grey" and posInfo.color == "red":
                image = ImageTk.PhotoImage(Image.open(self.redp_greys))
            else:
                image = ImageTk.PhotoImage(Image.open(self.redp_tans)) #changed redp_goals to redp_tans

            if posInfo == pos1Info:
                pos1Button.configure(image = image)
                pos1Button.image = image
            else:
                pos2Button.configure(image = image)
                pos2Button.image = image

    # disables buttons if computer's turn, enables when player's turn
    def enableButtons(self, enable):
        if enable:
            for row in self.buttonArray:
                for button in row:
                    button.configure(state = "disabled")
        else:
            for button in self.buttonArray:
                button.configure(state = "normal")

    def endTurnClicked(self):
        if self.boardObject.gameWon:
            self.setPlayerString("")
            return

        # loop to look through all buttons and find appropiate
        for row in self.buttonArray:
            for button in row:
                if self.whosTurn == "green": # if green is ending their turn, fade their move and unhighlight red
                    if button.cget("bg") == "green":
                        self.highlight(button, "fade", "green")
                    elif (button.cget("bg") == "red") or (button.cget("bg") == self.fadeRedHex):
                        self.highlight(button, "unhighlight", "red")
                else: # if red is ending their turn, fade their move and unhighlight green
                    if button.cget("bg") == "red":
                        self.highlight(button, "fade", "red")
                    elif (button.cget("bg") == "green") or (button.cget("bg") == self.fadeGreenHex):
                        self.highlight(button, "unhighlight", "green")
        if self.whosTurn == "green":                
            self.setPlayerString("It is now red's turn")
            self.whosTurn = "red"
        else:
            self.setPlayerString("It is now green's turn")
            self.whosTurn = "green"
        
        self.boardObject.endTurnHappened = True
        self.halmaGame.checkForComputer()

    def setPlayerString(self, string):
        self.playerString.set(string)

    def setStatusString(self, string):
        print(string)
        self.statusString.set(string)