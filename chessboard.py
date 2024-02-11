from enum import Enum
from chesspieces import Pawn, Rook, Bishop, Knight, Queen, King


class Chessboard:

    class PlayerColor(Enum):
        WHITE = 1
        BLACK = 2
    
    def __init__(self, boardState, isGameOver):
        self.boardState = boardState
        self.isGameOver = isGameOver

        self.files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.ranks = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.square_mapping = self.create_square_mapping()

    def create_square_mapping(self):
        square_mapping = {}
        start_y = 47
        for rank in self.ranks:
            start_x = 48
            for file in self.files:
                square_mapping[file + rank] = (start_x, start_y)
                start_x += 45
            start_y += 45
        
        return square_mapping

    @staticmethod
    def initialChessboardState():
        initial_chessboard = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]
        piece_mapping  = {
            'p' : Pawn(Chessboard.PlayerColor.BLACK, IsPawnsFirstMove=True ),
            'P' : Pawn(Chessboard.PlayerColor.WHITE, IsPawnsFirstMove=True ),
            
            'r' : Rook(Chessboard.PlayerColor.BLACK),
            'R' : Rook(Chessboard.PlayerColor.WHITE),
            
            'n' : Knight(Chessboard.PlayerColor.BLACK),
            'N' : Knight(Chessboard.PlayerColor.WHITE),

            'b' : Bishop(Chessboard.PlayerColor.BLACK),
            'B' : Bishop(Chessboard.PlayerColor.WHITE),

            'q' : Queen(Chessboard.PlayerColor.BLACK),
            'Q' : Queen(Chessboard.PlayerColor.WHITE),

            'k' : King(Chessboard.PlayerColor.BLACK, isCheck=False, isCheckMate=False),
            'K' : King(Chessboard.PlayerColor.WHITE, isCheck=False, isCheckMate=False),

            ' ' : None

        }

        chessboard = [[piece_mapping[piece] for piece in row] for row in initial_chessboard]

        return chessboard
    
    def initializeBoard(self):
        self.boardState = Chessboard.initialChessboardState()

    def getAlgebraicNotation():
        algebraic_notation = [
    ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
    ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
    ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
    ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
    ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
    ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
    ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
    ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
]
        return algebraic_notation

    def move(self, movement, player_color): 
        file_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        
        source_file, source_rank = movement[0], 8 - int(movement[1])
        dest_file, dest_rank = movement[2], 8 - int(movement[3])       

        piece = self.boardState[source_rank][file_map[source_file]]
        
        if piece is not None:
            
            self.boardState[dest_rank][file_map[dest_file]] = piece #e2e4 --> e2 source ist: [6][4] dest ist [4][4]
            self.boardState[source_rank][file_map[source_file]] = None
            return self.boardState
        
        print('Something went wrong with move function, Piece == NULL??')
        return None


            

        
    
    def getGameState(self):
        return self.boardState()
        

    
        

    def printGameState(self):
        for row in self.boardState:
            for col in row:
                if col is None:
                    print('[] ', end='')
                    continue
                if (col.color == Chessboard.PlayerColor.BLACK):
                    if isinstance(col, Pawn):
                        print('p  ', end='')
                    elif isinstance(col, Knight):
                        print('n  ', end='')
                    elif isinstance(col, Rook):
                        print('r  ', end='')
                    elif isinstance(col, Bishop):
                        print('b  ', end='')
                    elif isinstance(col, King):
                        print('k  ', end='')
                    elif isinstance(col, Queen):
                        print('q  ', end='')
                    
                elif (col.color == Chessboard.PlayerColor.WHITE):
                    if isinstance(col, Pawn):
                        print('P  ', end='')
                    elif isinstance(col, Knight):
                        print('N  ', end='')
                    elif isinstance(col, Rook):
                        print('R  ', end='')
                    elif isinstance(col, Bishop):
                        print('B  ', end='')
                    elif isinstance(col, King):
                        print('K  ', end='')
                    elif isinstance(col, Queen):
                        print('Q  ', end='')
                

            print('\n')
        