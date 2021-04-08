class Player:

    def __init__(self, board, whatSide, myTurn):
        self.board = board
        self.whatSide = whatSide
        self.turn = myTurn
        self.gotPiece = False
        self.piece = (-1, -1)
        self.validMoves = []

    def nextMove(self):
        nextMove = self.gui.nextMove()
        return nextMove

    def validMoves(self, coord):
        if coord in self.validMoves:
            return True
        else:
            return False

    def isValidPiece(self, cord):
        pos = self.board.boardArray[cord[0]][cord[1]]
        if(pos.piece):
            return True

        return False

    def endTurn(self):
        self.turn = False
        self.piece = (-1, -1)
        self.gotPiece = False
        self.validMoves = []

    # do move generator logic and save into valid moves for later
    def moveGenerator(self, cord):
        #get the piece being moved
        #piece = which_player.getPiece()
        
        #get the position (posInfo possibly)
        #    coords = getPos(board)
        
        #use those coordinates of the piece to check
            # the spaces around that piece and see if its valid
            
        #eg if piece being moved is at (0,0) then it can move to
           # (0,1), (1,0), (1, 1). (assuming space not occupied)

        
           #if there is an enemy piece in adjacent space positionInfo
           #it can jump the enemy piece if there is an open space after tha

        
        pass





