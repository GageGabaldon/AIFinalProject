import time
import Player

class Computer(Player):

    def __init__(self, bSize, board, enemyPlayer, whatSide, myTurn, timeLimit, ab=True):
        Player.__init__(self) # subclass of player
        self.board = board
        self.color = whatSide
        self.enemyColor = None
        if self.color == "green":
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
    def boardStates(self)
        return boardStatesHelper(self.board, self.color, 0, 0, 1)

    # recursively makes moves and returns back path value to find best value/move
    def boardStatesHelper(self, board, whosTurn, prunes, numMoves)

        # check if goal board state found or ran out of time, return current value
        if self.board.gameWon(whosTurn) or time.time() > self.time():
            return utility(whosTurn), prunes, numMoves
        depth += 1 # increment depth
        possibleMoves = self.boardMoves(whosTurn)
        # best board value for max would be the lowest sLD or for min it would be the highest sLD
        bestBoardValue = None
        bestBoardMove = None
        for piece, moves in possibleMoves:
            for move in moves:
                numMoves += 1 # keep track of number of moves made

                # copy of board to not mess with original board
                copyBoard = Board(self.originalboard)
                # update the board with a move in order to find next depth board state
                self.copyBoard.updateBoard(piece, moves)
                pathValue = utility(self, copyBoard, playerColor)

                # recursively call with whose next turn it is (will be flipping between min and max based on playerColor)
                moveValue, movePrunes, moveBoard = None
                if whosTurn != self.color:
                    moveValue, movePrunes, moveBoard = self.createBoardStatesHelper(copyBoard, self.color, prunes, numMoves, depth)
                else
                    moveValue, movePrunes, moveBoard = self.createBoardStateHelper(copyBoard, self.enemycolor, prunes, numMoves, depth)

                # update best value/move based on whos turn it is (if its min or max we are tracking)
                if whosTurn == self.color & (moveValue < bestBoardValue or bestBoardValue == None:
                    bestBoardValue == moveValue
                    bestBoardMove = (piece, move)
                if whosTurn != self.color & (moveValue > worstBoardValue or worstBoardValue == None):
                    bestBoardValue == moveValue
                    bestBoardMove = (piece, move)
                
                # return if current for loop pathing is proving to be weak / bad
                if ab == True:
                    return bestBoardValue, bestBoardMove, prunes, numMoves

        # return best first move/value found, number of prunces, and number of states created.
        return bestBoardValue, bestBoardMove, prunes, numMoves


    def boardMoves(self, playerColor):
        moves = []
        for row in range(self.bSize):
            for col in range(self.bSize):
                if board[row][col].color == playerColor: # find player color piece
                    piece = board[row][col]
                    pieceMoves = self.moveGenerator(row, col) # calculate possible moves of that piece
                    moves.append(piece, piecesMoves) # append as tuple pairs 
        return moves

    # this just compares every piece to the goal using a distance formula
    def utility(self, board, color):
        pass




