#init gameanalyzer

class Chesspiece:
    def __init__(self, color):
        self.color = color
        #self.isCapturable = isCapturable
    
    def isPieceCapturable():
        pass



class Pawn(Chesspiece):
    def __init__(self, color, IsPawnsFirstMove):
        super().__init__(color)
        self.IsPawnsFirstMove = IsPawnsFirstMove

    def getLegalMoves():
        #call gameanalyzer()
        pass

    def isCapturable():
        pass




class Knight(Chesspiece):
    def __init__(self, color):
        super().__init__(color)

    def getLegalMoves():
        pass

    def isCapturable():
        pass



class Bishop(Chesspiece):
    def __init__(self, color):
        super().__init__(color)

    def getLegalMoves():
        pass

    def isCapturable():
        pass


class Rook(Chesspiece):
    
    def __init__(self, color):
        super().__init__(color)

    def getLegalMoves():
        pass

    def isCapturable():
        pass


class Queen(Chesspiece):
    def __init__(self, color):
        super().__init__(color)

    def getLegalMoves():
        pass

    def isCapturable():
        pass


class King(Chesspiece):
    def __init__(self, color, isCheck, isCheckMate):
        super().__init__(color)
        self.isCheck = isCheck
        self.isCheckMate = isCheckMate

    def getLegalMoves():
        pass


    def isKingCheck():
        pass

    def isKingCheckMate():
        pass
        