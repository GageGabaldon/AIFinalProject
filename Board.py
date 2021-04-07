class Board:
    def __init__(self, boardSize, timeLimit, whatSide):
        self.gameWon = False
        self.timeLimit = timeLimit
        self.bSize = boardSize
        self.boardArray = self.getGameArray()
        self.playerPieces = whatSide
        self.redGoal = []
        self.greenGoal = []
        if(whatSide == "green"):
            self.computerPieces = "red"
        else:
            self.computerPieces = "green"

    def getGameArray(self):
        columnArray = []
        rowArray = []
        goalStates = []
        if(self.bSize == 8):
            redgoal = [(0, 7), (0, 6), (0, 5), (0, 4), (1, 5), (1, 6), (1, 7), (2, 6), (2, 7), (3, 7)]
            greenGoal = [(4, 0), (5, 0), (6, 0), (7, 0), (5, 1), (6, 1), (7, 1), (6, 2), (7, 2), (7, 3)]
        elif(self.bSize == 10):
            return 1
        else:
            return 2

        for col in range(0, self.bSize):
            rowArray = []
            for row in range(0, self.bSize):
                if (row, col) in redgoal:
                    boardInfo = PosInfo((row, col), True, "red", True, "green")
                    rowArray.append(boardInfo)
                    self.greenGoal.append(boardInfo)

                elif (row, col) in greenGoal:
                    boardInfo = PosInfo((row, col), True, "green", True, "red")
                    rowArray.append(boardInfo)
                    self.redGoal.append(boardInfo)
                else:
                    boardInfo = PosInfo((row, col), False, "none", False, "none")
                    rowArray.append(boardInfo)

            columnArray.append(rowArray)

        return columnArray

    def winCondition(self, color):
        redWin = False
        greenWin = False

        redCounter = 0
        numberOfRedGoals = len(self.redGoal)
        for state in self.redGoal:
            if state.goal():
                redCounter += 1

        greenCounter = 0
        numberOfGreenGoals = len(self.greenGoal)
        for state in self.greenGoal:
            if state.goal():
                greenCounter += 1

        if(greenCounter == numberOfGreenGoals):
            greenWin = True

        if(redCounter == numberOfRedGoals):
            redWin = True

        if color == "green":
            return greenWin
        else:
            return redWin

class PosInfo:
    def __init__(self, boardPos, piece, color, goal, colorGoal):
        self.boardPos = boardPos
        self.piece = piece
        self.color = color
        self.goal = goal
        self.colorGoal = colorGoal

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