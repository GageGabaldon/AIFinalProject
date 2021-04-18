import time
import math
import copy
from Player import Player

class Computer(Player):

    def __init__(self, bSize, board, whatSide, myTurn, timeLimit, ab=True):
        Player(board, whatSide, myTurn) # subclass of player
        self.bSize = bSize
        self.board = board
        self.whatSide = whatSide
        self.enemyColor = None
        if self.whatSide == "green":
            self.enemyColor = "red"
        else:
            self.enemyColor = "green"
        self.turn = myTurn
        self.time = timeLimit
        self.ab = ab
        self.validMoves = []
        self.validJumpMoves = []
        self.hasHopped = False
        self.startTime = 0

    # calls boardStatesHelper with the starting parameters
    def boardStates(self):
        print("Starting Board State Recursion")
        self.startTime = time.time()
        output = self.boardStatesHelper(self.board, self.whatSide, 999, -999, 0, 0, 3)
        self.startTime = 0
        print(output[0])
        print(output[1])
        print(output[2])
        return output

    # recursively makes moves and returns back path value to find best value/move
    def boardStatesHelper(self, board, whosTurn, bestVal, worstVal, prunes, numMoves, level, a=float("inf"), b=float("-inf")):
        # print(numMoves)
        # check if goal board state found or ran out of time, return current value
        # do NOT set gameWon, just check!!
        howManySeconds = time.time() - self.startTime
        if board.winCondition(whosTurn, True) or howManySeconds > self.time or level <= 0:
            return self.utility(board, whosTurn), None, prunes, numMoves

        # depth += 1 # increment depth
        possibleMoves = self.boardMoves(board, whosTurn)

        # best board value for max would be the lowest sLD or for min it would be the highest sLD
        if self.whatSide == whosTurn:
            bestBoardValue = float("inf")
        else:
            bestBoardValue = float("-inf")

        bestBoardMove = None

        # for each piece in the available moves
        for tupleTriple in possibleMoves:
            piece = tupleTriple[0] # posinfo piece
            pieceCoord = piece.boardPos # posinfo piece coords
            validMoves = tupleTriple[1] # coord to move to
            validJumpMoves = tupleTriple[2] # cord to jump
            for move in validMoves:

                howManySeconds = time.time() - self.startTime
                if howManySeconds > self.time:
                    return bestBoardValue, bestBoardMove, prunes, numMoves

                numMoves += 1 # keep track of number of moves made
                # update the board with a move in order to find next depth board state
                board.updateBoard((pieceCoord[0], pieceCoord[1]), move)

                # recursively call with whose next turn it is (will be flipping between min and max based on playerColor)
                moveValue = None
                movePrunes = None
                moveBoard = None
                if whosTurn != self.whatSide:
                    moveOutput = self.boardStatesHelper(board, self.whatSide, bestVal, worstVal, prunes, numMoves, level - 1, a, b)
                    moveValue = moveOutput[0]
                    movePrunes = moveOutput[2]
                    moveBoard = moveOutput[3]
                else:
                    moveOutput = self.boardStatesHelper(board, self.enemyColor, bestVal, worstVal, prunes, numMoves, level -1, a, b)
                    moveValue = moveOutput[0]
                    movePrunes = moveOutput[2]
                    moveBoard = moveOutput[3]

                # reset original board
                board.updateBoard(move, (pieceCoord[0], pieceCoord[1]))

                # update best value/move based on whos turn it is (if its min or max we are tracking)
                if whosTurn == self.whatSide and moveValue < bestBoardValue:
                    bestBoardValue = moveValue
                    bestBoardMove = (piece, move)
                    a = min(a, moveValue)

                if whosTurn != self.whatSide and moveValue > bestBoardValue:
                    bestBoardValue = moveValue
                    bestBoardMove = (piece, move)
                    b = max(b, moveValue)

                # return and end current loop through moves if bestVal meets or is worse than worstVal
                if self.ab == True and b >= a:
                    return bestBoardValue, bestBoardMove, prunes + 1, numMoves

        # return best first move/value found, number of prunces, and number of states created.
        return bestBoardValue, bestBoardMove, prunes, numMoves

    # calculates possible moves for every piece of playerColor
    def boardMoves(self, board, playerColor):
        board = board.getBoardArray()
        moves = []
        for row in range(self.bSize):
            for col in range(self.bSize):
                if board[row][col].color == playerColor: # find player color piece
                    piece = board[row][col]
                    self.moveGenerator((row, col)) # calculate possible moves of that piece
                    validMoves, jumpMoves = self.getValidMoves()
                    moves.append((piece, validMoves, jumpMoves)) # append as tuple pairs
        return moves

    # only currently uses straight line distance formula. bare bones.
    def utility(self, board, color):
        # find goal states of enemy color
        goalSpaces = board.getGoals()
        goals = None
        if color == "green":
            goals = goalSpaces[0]
        else:
            goals = goalSpaces[1]

        for goal in goals:
            if goal.pieceColor() == color:
                goals.remove(goal)

        # remove already occupied goal spaces
        # add up sLD to nearest unoccupied goal
        boardArray = board.getBoardArray()
        totalValue = 0
        for row in range(self.bSize):
            for col in range(self.bSize):
                spaceInfo = boardArray[row][col]

                # find each space with parameter color piece
                if spaceInfo.piece and spaceInfo.pieceColor() == color:
                    shortestDistance = -999 # placeholder unti first number entered

                    x, y = spaceInfo.boardPos
                    for goal in goals:
                        # sLD from current piece to current goal square
                        sLD = self.pointDistance(goal.boardPos[0], goal.boardPos[1], x,  y)
                        if sLD < shortestDistance or shortestDistance == -999:
                            shortestDistance = sLD

                    # add to total value for board
                    totalValue += shortestDistance
        print(totalValue)
        return totalValue

    def pointDistance(self, p1x, p1y, p2x, p2y):
        distx = (p1x - p2x) * (p1x - p2x)
        disty = (p1y - p2y) * (p1y - p2y)

        return math.sqrt(distx + disty)