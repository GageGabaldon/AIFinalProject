
class Board:
    def __init__(self, boardSize, timeLimit, whatSide):
        self.gameWon = False
        self.timeLimit = timeLimit
        self.bSize = boardSize
        self.boardArray = getGameArray()
        self.playerPieces = whatSide
        if(whatSide == "green"):
            self.computerPieces = "red"
        else:
            self.computerPieces = "green"

    def getGameArray(self):
        return None




