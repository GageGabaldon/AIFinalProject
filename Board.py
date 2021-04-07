
class Board:
    def __init__(self, boardSize, timeLimit, whatSide):
        self.gameWon = False
        self.timeLimit = timeLimit
        self.bSize = boardSize
        self.boardArray = self.getGameArray()
        self.playerPieces = whatSide
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
