import time
import math
import copy
from Player import Player

"""
Bug 1: If all the moves for computer give the same value, prioritize
   moving into a goal state or further into a goal state
   (it kept going back and forth since it was valid since it has no or = state)
   something has to happen here. this prevents computer from winning(fix this)

Bug 2: We need to add jump moves to computer. e.g.
    1)iterate through jump moves first( recursion it should go first)
    2)iterate through the other valid moves
    3)keep track of hops (if hasHopped check for only jumpmoves, if not then return)

Bug 3: should change board state based on our best move but rn it just beelines for
     goals instead( it shouldn't let us hop as easily, maybe because sLD??).
     take into account player's hops since hops are not included.

UI Bug

Timer? - physical timer or just computer idk? keep in mind

some kinda tie-breaker in the utility function somewhere
 - run thru whole utility function
    - if piece can move in corner piece (size.b) do - 1 or somethin to
       give it lower value(AKA higher priority?

if state leads to a game win, then prioritize it. 


"""


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
        self.jumpdict = {}
        self.jumpdict["green"] = False
        self.jumpdict["red"] = False
        self.startTime = 0


    # calls boardStatesHelper with the starting parameters
    def boardStates(self):
        print("Starting Board State Recursion")
        self.startTime = time.time()
        output = self.boardStatesHelper(self.board, self.whatSide, 0, 0, 2)
        self.startTime = 0
        self.jumpdict["green"] = False
        self.jumpdict["red"] = False
        print("values after running boardStates")
        print(output[0])
        print(output[1][0].boardPos)
        print(output[1][1])
        print(output[2])
        return output

    # recursively makes moves and returns back path value to find best value/move
    def boardStatesHelper(self, board, whosTurn, prunes, numMoves, level, a=float("inf"), b=float("-inf"), pieceJumping=None):
        # check if goal board state found or ran out of time, return current value
        # do NOT set gameWon, just check!!
        board.getBoardInfo()
        howManySeconds = time.time() - self.startTime
        print(howManySeconds)
        if board.winCondition(whosTurn, True) or howManySeconds > self.time or level <= 0:
            return self.utility(board, whosTurn), None, prunes, numMoves

        # best board value for max would be the lowest sLD or for min it would be the highest sLD
        if self.whatSide == whosTurn:
            bestBoardValue = float("inf")
        else:
            bestBoardValue = float("-inf")

        bestBoardMove = None

        # if the piece has jumped only check the piece jumping values
        if self.jumpdict[whosTurn]:
            piece = pieceJumping
            moves = self.newGen(piece, True)
            if len(moves) == 0:
                return self.utility(board, whosTurn), None, prunes, numMoves

            for jmove1 in moves:
                if howManySeconds > self.time:
                    return bestBoardValue, bestBoardMove, prunes, numMoves
                numMoves += 1
                board.updateBoard((piece[0], piece[1]), jmove1)
                # recursively call with whose next turn it is (will be flipping between min and max based on playerColor)
                moveValue = None
                movePrunes = None
                moveBoard = None
                if whosTurn != self.whatSide:
                    moveOutput = self.boardStatesHelper(board, self.whatSide, prunes, numMoves, level - 1, a, b, jmove1)
                    moveValue = moveOutput[0]
                    movePrunes = moveOutput[2]
                    moveBoard = moveOutput[3]
                else:
                    moveOutput = self.boardStatesHelper(board, self.enemyColor, prunes, numMoves, level - 1, a, b, jmove1)
                    moveValue = moveOutput[0]
                    movePrunes = moveOutput[2]
                    moveBoard = moveOutput[3]

                # reset original board
                board.updateBoard(jmove1, (piece[0], piece[1]))

                # update best value/move based on whos turn it is (if its min or max we are tracking)
                if whosTurn == self.whatSide and moveValue < bestBoardValue:
                    bestBoardValue = moveValue
                    bestBoardMove = (piece, jmove1)
                    a = min(a, moveValue)

                if whosTurn != self.whatSide and moveValue > bestBoardValue:
                    bestBoardValue = moveValue
                    bestBoardMove = (piece, jmove1)
                    b = max(b, moveValue)

                if self.ab and b >= a:
                    return bestBoardValue, bestBoardMove, prunes + 1, numMoves

            return bestBoardValue, bestBoardMove, prunes, numMoves

        # depth += 1 # increment depth
        possibleMoves = self.boardMoves(board, whosTurn)

        # for each piece in the available moves
        for tupleTriple in possibleMoves:
            piece = tupleTriple[0] # posinfo piece
            pieceCoord = piece.boardPos # posinfo piece coords
            validMoves = tupleTriple[1] # coord to move to
            validJumpMoves = tupleTriple[2] # cord to jump

            for jmove in validJumpMoves:
                howManySeconds = time.time() - self.startTime
                if howManySeconds > self.time:
                    return bestBoardValue, bestBoardMove, prunes, numMoves

                # update board object for recursion
                board.updateBoard((pieceCoord[0], pieceCoord[1]), jmove)
                self.jumpdict[whosTurn] = True

                # recursively call with whose next turn it is (will be flipping between min and max based on playerColor)
                moveValue = None
                movePrunes = None
                moveBoard = None
                if whosTurn != self.whatSide:
                    moveOutput = self.boardStatesHelper(board, self.whatSide, prunes, numMoves, level - 1, a, b, jmove)
                    moveValue = moveOutput[0]
                    movePrunes = moveOutput[2]
                    moveBoard = moveOutput[3]
                else:
                    moveOutput = self.boardStatesHelper(board, self.enemyColor, prunes, numMoves, level - 1, a, b, jmove)
                    moveValue = moveOutput[0]
                    movePrunes = moveOutput[2]
                    moveBoard = moveOutput[3]

                # reset original board and jump dict
                board.updateBoard(jmove, (pieceCoord[0], pieceCoord[1]))
                self.jumpdict[whosTurn] = False

                # update best value/move based on whos turn it is (if its min or max we are tracking)
                if whosTurn == self.whatSide and moveValue < bestBoardValue:
                    bestBoardValue = moveValue
                    bestBoardMove = (piece, jmove)
                    a = min(a, moveValue)

                if whosTurn != self.whatSide and moveValue > bestBoardValue:
                    bestBoardValue = moveValue
                    bestBoardMove = (piece, jmove)
                    b = max(b, moveValue)

                if self.ab and b >= a:
                    return bestBoardValue, bestBoardMove, prunes + 1, numMoves

            # checkt the other non jumping moves
            for move in validMoves:
                # timing to end recursion
                howManySeconds = time.time() - self.startTime
                if howManySeconds > self.time:
                    return bestBoardValue, bestBoardMove, prunes, numMoves

                 # update the board with a move in order to find next depth board state
                board.updateBoard((pieceCoord[0], pieceCoord[1]), move)

                # recursively call with whose next turn it is (will be flipping between min and max based on playerColor)
                moveValue = None
                movePrunes = None
                moveBoard = None
                if whosTurn != self.whatSide:
                    moveOutput = self.boardStatesHelper(board, self.whatSide, prunes, numMoves, level - 1, a, b, pieceJumping)
                    moveValue = moveOutput[0]
                    movePrunes = moveOutput[2]
                    moveBoard = moveOutput[3]
                else:
                    moveOutput = self.boardStatesHelper(board, self.enemyColor, prunes, numMoves, level - 1, a, b, pieceJumping)
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
                if self.ab and b >= a:
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
                    output = self.newGen((row, col), False) # calculate possible moves of that piece
                    moves.append((piece, output[1], output[0])) # append as tuple pairs
        return moves

    # only currently uses straight line distance formula. bare bones.
    def utility(self, board, color):
        # find goal states of enemy color
        goalSpaces = board.getGoals()
        goals = None

        if color == "red":
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
                    if len(goals) == 0:
                        shortestDistance = -10
                    else:
                        for goal in goals:
                            # sLD from current piece to current goal square
                            sLD = self.pointDistance(goal.boardPos[0], goal.boardPos[1], x,  y)
                            if sLD < shortestDistance or shortestDistance == -999:
                                shortestDistance = sLD

                    # add to total value for board
                    totalValue += shortestDistance
        return totalValue

    def pointDistance(self, p1x, p1y, p2x, p2y):
        distx = (p1x - p2x) * (p1x - p2x)
        disty = (p1y - p2y) * (p1y - p2y)

        return math.sqrt(distx + disty)

    # do move generator logic and save into valid moves for later
    def newGen(self, cord, hopped):
        # get the piece being moved

        board_arr = self.board.boardArray
        board_size = self.board.bSize
        # piece = which_player.getPiece() idk about this

        # get the position (posInfo possibly)
        row = cord[0]
        col = cord[1]
        curr_space = board_arr[row][col]

        # use those coordinates of the piece to check
        # the spaces around that piece and see if its valid
        poss_moves = []
        jump_moves = []
        # row-1 to row + 1
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                # if space is within board (not going over edge)
                if (i >= 0 and i < board_size and j >= 0 and j < board_size):
                    sur_space = board_arr[i][j]  # surrounding space
                    if sur_space.piece:  # if sur_piece is a piece
                        difference_row = i - row  # surrounding piece pos - current piece pos
                        difference_col = j - col  # surrounding piece pos - current piece pos
                        # add this difference to the surrounding piece, to then find
                        # the space we land after jumping
                        jump_space_row = i + difference_row
                        jump_space_col = j + difference_col
                        # only space you can land if trying to jump, append to poss moves.
                        if (jump_space_row < board_size and jump_space_row >= 0) and (
                                jump_space_col < board_size and jump_space_col >= 0):
                            if not board_arr[jump_space_row][jump_space_col].piece:
                                    jump_moves.append((jump_space_row, jump_space_col))
                    else:
                        poss_moves.append(sur_space.boardPos)
        if hopped:
            return jump_moves
        else:
            return jump_moves, poss_moves
