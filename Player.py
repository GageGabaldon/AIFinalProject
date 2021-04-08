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
        
        board_arr = self.board.boardArray 
        #piece = which_player.getPiece() idk about this
        
        #get the position (posInfo possibly)
        row = cord[0]
        col = cord[1]
        current_pos = board_arr[row][col]
        
        #use those coordinates of the piece to check
            # the spaces around that piece and see if its valid
        poss_moves = []
        #row-1 to row + 1
        for i in range(row-1,row+1):
            for j in range(col-1,col+1):
                sur_piece = board_arr[i][j] #surrounding piece
                if sur_piece.piece:#if sur_piece is a piece
                    if sur_piece.color != self.whatSide:#if is enemy piece
                        #if theres a piece after the enemy piece to hop to(loop?)
                        if(board_arr[i-1][j-1].piece != True): #if theres not a piece top left
                            poss_moves.append(board_arr[i-1][j-1])                           
                        if(board_arr[i-1][j].piece != True): #if theres not a piece top
                            poss_moves.append(board_arr[i-1][j])
                        if(board_arr[i-1][j+1].piece != True): #if theres not a piece topright
                            poss_moves.append(board_arr[i-1][j+1])
                        if(board_arr[i][j+1].piece != True): #if theres not a piece right
                            poss_moves.append(board_arr[i][j+1])
                        if(board_arr[i+1][j+1].piece != True): #if theres not a piece botright
                            poss_moves.append(board_arr[i+1][j+1])
                        if(board_arr[i+1][j].piece != True): #if theres not a piece bottom
                            poss_moves.append(board_arr[i+1][j])
                        if(board_arr[i+1][j-1].piece != True): #if theres not a piece botleft
                            poss_moves.append(board_arr[i+1][j-1])
                        if(board_arr[i][j-1].piece != True): #if theres not a piece left
                            poss_moves.append(board_arr[i][j-1])
             
                else:
                    poss_moves.append(sur_piece.boardPos)
        
        
        #eg if piece being moved is at (0,0) then it can move to
           # (0,1), (1,0), (1, 1). (assuming space not occupied)

        
           #if there is an enemy piece in adjacent space positionInfo
           #it can jump the enemy piece if there is an open space after tha

        
        pass





