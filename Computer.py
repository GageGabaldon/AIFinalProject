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

    # calls boardStatesHelper with the starting parameters
    def boardStates(self):
        print("Starting Board State Recursion")
        output = self.boardStatesHelper(self.board, self.whatSide, 999, -999, 0, 0)
        self.board.gameWon = False
        return output

    # recursively makes moves and returns back path value to find best value/move
    def boardStatesHelper(self, board, whosTurn, bestVal, worstVal, prunes, numMoves):
        # print(numMoves)
    
        # check if goal board state found or ran out of time, return current value
        # do NOT set gameWon, just check!!
        if board.winCondition(whosTurn):
            return self.utility(board, whosTurn), None, prunes, numMoves
        # depth += 1 # increment depth
        possibleMoves = self.boardMoves(board, whosTurn)
        # best board value for max would be the lowest sLD or for min it would be the highest sLD
        bestBoardValue = bestVal
        bestBoardMove = None
        for tupleTriple in possibleMoves:
            piece = tupleTriple[0] # posinfo piece
            pieceCoord = piece.boardPos # posinfo piece coords
            validMoves = tupleTriple[1] # coord to move to
            validJumpMoves = tupleTriple[2] # cord to jump
            for move in validMoves:

                numMoves += 1 # keep track of number of moves made
                # update the board with a move in order to find next depth board state
                board.updateBoard((pieceCoord[0], pieceCoord[1]), move)
                pathValue = self.utility(board, whosTurn)

                # recursively call with whose next turn it is (will be flipping between min and max based on playerColor)
                moveValue = None
                movePrunes = None
                moveBoard = None
                if whosTurn != self.whatSide:
                    moveOutput = self.boardStatesHelper(board, self.whatSide, bestVal, worstVal, prunes, numMoves)
                    moveValue = moveOutput[0]
                    movePrunes = moveOutput[2]
                    moveBoard = moveOutput[3]
                else:
                    moveOutput = self.boardStatesHelper(board, self.enemyColor, bestVal, worstVal, prunes, numMoves)
                    moveValue = moveOutput[0]
                    movePrunes = moveOutput[2]
                    moveBoard = moveOutput[3]

                # reset original board
                board.updateBoard(move, (pieceCoord[0], pieceCoord[1]))

                # update best value/move based on whos turn it is (if its min or max we are tracking)
                if whosTurn == self.whatSide and moveValue < bestBoardValue:
                    bestBoardValue == moveValue
                    bestBoardMove = (piece, move)
                    if bestBoardValue < bestVal:
                        bestVal = bestBoardValue
                if whosTurn != self.whatSide and moveValue > bestBoardValue:
                    bestBoardValue == moveValue
                    bestBoardMove = (piece, move)
                    if bestBoardValue > worstVal:
                        worstVal = bestBoardValue
                
                # return and end current loop through moves if bestVal meets or is worse than worstVal
                if self.ab == True & bestVal <= worstVal:
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

        # remove already occupied goal spaces
        for goal in goals:
            if goal.piece == True:
                goals.remove(goal)

        # add up sLD to nearest unoccupied goal 
        boardArray = board.getBoardArray()
        totalValue = 0
        for row in range(self.bSize):
            for col in range(self.bSize):
                spaceInfo = boardArray[row][col]
                # find each space with parameter color piece
                shortestDistance = -999 # placeholder unti first number entered
                if spaceInfo.piece and spaceInfo.pieceColor() == color:
                    x, y = spaceInfo.boardPos
                    for goal in goals:
                        # sLD from current piece to current goal square
                        sLD = math.sqrt( (goal.boardPos[0] - x)**2 + (goal.boardPos[1] - y)**2 )
                        if sLD < shortestDistance or shortestDistance == -999:
                            shortestDistance = sLD
                # add to total value for board 
                totalValue += shortestDistance
        return totalValue




