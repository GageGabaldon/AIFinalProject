class Board:

    def __init__(self, boardSize, timeLimit, whatSide):
        self.gameWon = False
        self.timeLimit = timeLimit
        self.bSize = boardSize
        self.redGoal = []
        self.greenGoal = []
        self.boardArray = self.getGameArray()
        self.whatSide = whatSide

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

    def getBoardInfo(self):
        for col in range(0, self.bSize):
            for row in range(0, self.bSize):
                self.boardArray[col][row].displayInfo()

    # assume input is valid
    def updateBoard(self, piece, newPos):
        pos1 = self.boardArray[piece[0]][piece[1]]
        pos2 = self.boardArray[newPos[0]][newPos[1]]
        color = pos1.color

        pos1.updatePos("none")
        pos2.updatePos(color)



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
        print(str(self.boardPos) + " " + str(self.color) + " " + str(self.goal))
class Board:
    def __init__(self, boardSize, timeLimit, whatSide):
        self.gameWon = False
        self.timeLimit = timeLimit
        self.bSize = boardSize
        self.redGoal = []
        self.greenGoal = []
        self.boardArray = self.getGameArray()
        self.whatSide = whatSide

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
            whiteSquare = [(0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2), (2, 4), (3, 1), (3, 3), (3, 5),
                            (4, 2), (4, 4), (4, 6), (5, 3), (5, 5), (5, 7), (6, 4), (6, 6), (7, 5), (7, 7)]
            greySquare = [(0, 1), (0, 3), (1, 0), (1, 2), (1, 4), (2, 1), (2, 3), (2, 5), (3, 0), (3, 2),
                            (3, 4), (3, 6), (4, 1), (4, 3), (4, 5), (4, 7), (5, 2), (5, 4), (5, 6), (6, 3)
                            (6, 3), (6, 5), (6, 7), (7, 4), (7, 6)]
        elif(self.bSize == 10):
            return 1
        else:
            return 2

        for col in range(0, self.bSize):
            rowArray = []
            for row in range(0, self.bSize):
                if (row, col) in redgoal:
                    boardInfo = PosInfo((row, col), True, "red", "goal", "green")
                    rowArray.append(boardInfo)
                    self.greenGoal.append(boardInfo)
                elif (row, col) in greenGoal:
                    boardInfo = PosInfo((row, col), True, "green", "goal", "red")
                    rowArray.append(boardInfo)
                    self.redGoal.append(boardInfo)
                else:
                    if (row, col) in whiteSquare:
                        boardInfo = PosInfo((row, col), False, "white", , "none")
                        rowArray.append(boardInfo)
                    else:
                        boardInfo = PosInfo((row, col), False, "grey", , "none")
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
