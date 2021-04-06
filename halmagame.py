from tkinter import *
import tkinter as tk
import sys
class HalmaGame:
    
    def __init__(self):
        # command line arguments
        self.bSize = 8 #sys.argv[1]
        #self.tLimit = sys.argv[2]
        #self.hPlayer = sys.argv[3]
        #self.filename = None

        self.boardArray = []
        self.playerPieces = {}
        self.computerPieces = {}

        self.root = tk.Tk() # main window
        self.root.geometry("1000x1000")
        self.root.title("Halma Game") # window name
        self.createBoard() # create player & computer boards gui

    # builds GUI window
    def __init__gui(self):
        pass
    
    def createBoard(self):
        # CREATE EMPTY BOARD
        self.board = Frame(self.root, bg = "black", width = 600, height = 600) # frame holding nxn board
        self.board.pack()
        for row in range(0, self.bSize):
            for column in range(0, self.bSize):
                # calls button clicked and passes in the button object
                button = None
                if (row % 2 == 0) and (column % 2 != 0):
                    button = tk.Button(self.board, 
                                    command=self.buttonClicked, 
                                    #text = "b", 
                                    bg = "red")
                else: 
                    button = tk.Button(self.board, 
                                    command=self.buttonClicked, 
                                    #text = "b",
                                    bg = "green")
                button.configure(height = 5, width = 5)
                self.boardArray.append(button)
                button.grid(row=row, column=column)
        

    def buttonClicked(self):
        print("You pressed me")


    # Display messages from program outlining what is going on
    def statusString():
        pass


def main():
    game = HalmaGame()
    game.root.mainloop()

if __name__ == "__main__":
    main()
