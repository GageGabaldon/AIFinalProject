class Board:
    def __init__(self, boardSize, timeLimit, whatSide):
        self.gameWon = False
        self.timeLimit = timeLimit
        self.bSize = boardSize
        self.redGoal = []
        self.greenGoal = []
        self.boardArray = self.getGameArray()
        self.whatSide = whatSide
        self.endTurnHappened = False

        if whatSide == "green":
            self.computerPieces = "red"
        else:
            self.computerPieces = "green"

    # Finds the white grey squares for displaying
    def findWhiteGrey(self):
        whiteSquares = []
        greySquares = []
        for row in range(0, self.bSize):
            for col in range(0, self.bSize):
                if (row % 2 == 0 and col % 2 != 0) or (row % 2 != 0 and col % 2 == 0):
                    whiteSquares.append((row, col))
                else:
                    greySquares.append((row, col))
        return (whiteSquares, greySquares)

    # generates the goal states to be used.
    def getGoal(self):
        redgoal = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [3, 0]]
        greengoal = [[self.bSize - 1, self.bSize - 1], [self.bSize - 2, self.bSize - 1], [self.bSize - 3, self.bSize - 1],
                     [self.bSize - 4, self.bSize - 1], [self.bSize - 1, self.bSize - 2], [self.bSize - 2, self.bSize - 2],
                     [self.bSize - 3, self.bSize - 2], [self.bSize - 1, self.bSize - 3], [self.bSize - 2, self.bSize - 3],
                     [self.bSize - 1, self .bSize - 4]]

        if self.bSize == 10 or self.bSize == 16:
            redgoal.append([0, 4])
            redgoal.append([1, 3])
            redgoal.append([2, 2])
            redgoal.append([3, 1])
            redgoal.append([4, 0])

            greengoal.append([self.bSize - 5, self.bSize - 1])
            greengoal.append([self.bSize - 4, self.bSize - 2])
            greengoal.append([self.bSize - 3, self.bSize - 3])
            greengoal.append([self.bSize - 2, self.bSize - 4])
            greengoal.append([self.bSize - 1, self.bSize - 5])

            if self.bSize == 16:
                redgoal.append([1, 4])
                redgoal.append([2, 3])
                redgoal.append([3, 2])
                redgoal.append([4, 1])

                greengoal.append([self.bSize - 5, self.bSize - 2])
                greengoal.append([self.bSize - 4, self.bSize - 3])
                greengoal.append([self.bSize - 3, self.bSize - 4])
                greengoal.append([self.bSize - 2, self.bSize - 5])

        return (redgoal, greengoal)

    # generates the game array to be used.
    def getGameArray(self):
        columnArray = []
        rowArray = []
        goalStates = []
        goals = self.getGoal()
        redGoal = goals[0]
        greenGoal = goals[1]

        whiteGrey = self.findWhiteGrey()
        whiteSquare = whiteGrey[0]
        greySquare = whiteGrey[1]

        for row in range(0, self.bSize):
            rowArray = []
            for col in range(0, self.bSize):
                if [row, col] in redGoal:
                    boardInfo = PosInfo((row, col), True, "red", "goal", "green")
                    rowArray.append(boardInfo)
                    self.greenGoal.append(boardInfo)
                elif [row, col] in greenGoal:
                    boardInfo = PosInfo((row, col), True, "green", "goal", "red")
                    rowArray.append(boardInfo)
                    self.redGoal.append(boardInfo)
                else:
                    if (row, col) in whiteSquare:
                        boardInfo = PosInfo((row, col), False, "none", "white", "none")
                        rowArray.append(boardInfo)
                    else:
                        boardInfo = PosInfo((row, col), False, "none", "grey", "none")
                        rowArray.append(boardInfo)

            columnArray.append(rowArray)

        return columnArray

    # checks to see if all the pieces are on the goal states of the opposite corner
    def winCondition(self, color, check):
        redWin = False
        greenWin = False

        redCounter = 0
        numberOfRedGoals = len(self.redGoal)
        for state in self.redGoal:
            if state.colorGoal == state.color:
                redCounter += 1

        greenCounter = 0
        numberOfGreenGoals = len(self.greenGoal)
        for state in self.greenGoal:
            if state.colorGoal == state.color:
                greenCounter += 1

        if(greenCounter == numberOfGreenGoals):
            if not check:
                self.gameWon = True
            greenWin = True

        if(redCounter == numberOfRedGoals):
            if not check:
                self.gameWon = True
            redWin = True

        if color == "green":
            return greenWin
        else:
            return redWin

    # displays the board information to the user
    def getBoardInfo(self):
        string = ""
        for col in range(0, self.bSize):
            string = ""
            for row in range(0, self.bSize):
                string += self.boardArray[col][row].displayGraphically()
            print(string)

    def getGoals(self):
        red = self.redGoal.copy()
        green = self.greenGoal.copy()
        return (red, green)

    def getBoardArray(self):
        return self.boardArray

    # assume input is valid
    def updateBoard(self, piece, newPos):
        pos1 = self.boardArray[piece[0]][piece[1]]
        pos2 = self.boardArray[newPos[0]][newPos[1]]
        color = pos1.color

        pos1.updatePos("none")
        pos2.updatePos(color)

# the board information at any given position
class PosInfo:
    def __init__(self, boardPos, piece, color, goal, colorGoal):
        self.boardPos = boardPos
        self.piece = piece
        self.color = color
        self.goal = goal
        self.colorGoal = colorGoal

    def updatePos(self, piece):
        self.color = piece
        if piece == "none":
            self.piece = False
        else:
            self.piece = True

    def getPos(self):
        return self.boardPos

    def hasPiece(self):
        return self.piece

    def pieceColor(self):
        return self.color

    def goal(self):
        if(self.colorGoal == self.color):
            return True
        else:
            return False

    def displayInfo(self):
        print(str(self.boardPos) + " " + str(self.color) + " " + str(self.colorGoal))

    def displayGraphically(self):
        if self.color == "none":
            return " . "
        elif self.color == "red":
            return " R "
        else:
            return " G "