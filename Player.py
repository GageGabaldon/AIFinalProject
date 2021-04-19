class Player:

    def __init__(self, board, whatSide, myTurn):
        self.board = board
        self.whatSide = whatSide
        self.turn = myTurn
        self.gotPiece = False
        self.piece = (-1, -1)
        self.validMoves = []
        self.validJumpMoves = []
        self.hasHopped = False

    # checks if the move being made is valid
    def isValidMoves(self, coord):
        # if validJumpMoves > 0 then a jump is mossible 
        if coord in self.validJumpMoves:
            self.hasHopped = True
            return True
        elif coord in self.validMoves:
            return True
        return False

    # checks if the place getting clicked has a pice on it
    def isValidPiece(self, cord):
        pos = self.board.boardArray[cord[0]][cord[1]]
        if(pos.piece and pos.color == self.whatSide):
            return True
        return False

    def getValidMoves(self):
        return (self.validMoves, self.validJumpMoves)

    # reset the player class
    def endTurn(self):
        self.turn = False
        self.piece = (-1, -1)
        self.gotPiece = False
        self.validMoves = []
        self.hasHopped = False

    # do move generator logic and save into valid moves for later
    def moveGenerator(self, cord):
        #get the piece being moved

        board_arr = self.board.boardArray
        board_size = self.board.bSize
        #piece = which_player.getPiece() idk about this

        #get the position (posInfo possibly)
        row = cord[0]
        col = cord[1]
        curr_space = board_arr[row][col]

        #use those coordinates of the piece to check
            # the spaces around that piece and see if its valid
        self.validMoves = []
        self.validJumpMoves = []
        poss_moves = []
        jump_moves = []
        #row-1 to row + 1
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                # if space is within board (not going over edge)
                if( i >= 0 and i < board_size and j >= 0 and j < board_size):
                    sur_space = board_arr[i][j] #surrounding space
                    if sur_space.piece:# if sur_piece is a piece
                        # if is enemy piece
                        difference_row = i - row # surrounding piece pos - current piece pos
                        difference_col = j - col # surrounding piece pos - current piece pos
                        # add this difference to the surrounding piece, to then find
                        # the space we land after jumping
                        jump_space_row = i + difference_row
                        jump_space_col = j + difference_col
                        # only space you can land if trying to jump, append to poss moves.
                        if (jump_space_row < board_size and jump_space_row >= 0) and ( jump_space_col < board_size and jump_space_col >= 0):
                            # check to see if the
                            if not board_arr[jump_space_row][jump_space_col].piece:
                                jump_moves.append((jump_space_row, jump_space_col))
                    else:
                        poss_moves.append(sur_space.boardPos)   
        
        if self.hasHopped:
            self.validJumpMoves = jump_moves
        else:
            self.validMoves = poss_moves
            self.validJumpMoves = jump_moves

