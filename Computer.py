import time

class Computer:

    def __init__(self, board, whatSide, myTurn, timeLimit, ab=True):
        self.board = board
        self.whatSide = whatSide
        self.turn = myTurn
        self.time = timeLimit
        self.abEnabled = ab

    def MakeAMove(self, depth, playerColor,  a=float("-inf"),
                b=float("inf"), maxing=True, prunes=0, boards=0):

        if depth == 0 or self.board.gameWon(playerColor) or time.time() > self.time:
            return self.utility(playerColor), None, prunes, boards

        best_move = None
        if maxing:
            best_val = float("-inf")
        else:
            best_val = float("inf")

        moves = self.boardMoves(playerColor)

        for move in moves:
            for moveTo in move["move"]:
                if time.time() > self.time:
                    return best_val, best_move, prunes, boards

                piece = move["piece"]
                newPos = moveTo
                self.board.updateBoard(piece, newPos)
                boards += 1

                val, _, new_prunes, new_boards = self.MakeAMove(depth - 1,
                                                                playerColor,
                                                                a, b, not maxing,
                                                                prunes, boards)
                prunes = new_prunes
                boards = new_boards

                self.board.updateBoard(newPos, piece)

                if maxing and val > best_val:
                    best_val = val
                    best_move = (piece, newPos)
                    a = max(a, val)

                if not maxing and val < best_val:
                    best_val = val
                    best_move = (piece, newPos)
                    b = min(b, val)

                if self.abEnabled and b <= a:
                    return best_val, best_move, prunes + 1, boards

        return best_val, best_move, prunes, boards

    def boardMoves(self, color):
        pass

    # this prunes the sub trees of the search space.
    def AlphaPrunning(self):
        pass

    # this just compares every piece to the goal using a distance formula
    def utility(self, color):
        # determine goal states based on enemy color
        goalSpaces = None
        if playerColor == "green":
            goalSpaces = self.redGoal
        else:
            goalSpaces = self.greenGoal
        
        # remove already occupied goalSpaces
        for goal in goalSpace:
            if goal.piece != "none":
                goalSpaces.remove(goal)

        distanceValue = 0
        # loop through all spaces
        for row in self.boardArray:
            for col in row:
                currPiece = self.boardArray[row][column]
                currFurthestGoal = # unoccupied
                # find each player piece's distance to a unoccupied goal state
                if currPiece.piece != "none" and color == playerColor:


        # return distance
        return distanceValue


