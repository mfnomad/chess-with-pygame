from chesspieces import Pawn,Bishop,Knight,Queen, King
from chessboard import Chessboard


class MoveGenerator:
    @staticmethod
    def getLegalMoves(boardState):
    #def getLegalMoves(piece, current_position, board_state):
        legal_moves = []

        legal_moves.extend(['a4', 'a2a4', 'b4', 'b2b4', 'c4', 'c2c4', 'd4', 'd2d4', 'e4', 'e2e4', 'f4', 'f2f4', 'g4', 'g2g4', 'h4', 'h2h4'])
        legal_moves.extend(['a3','b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3', 'a2a3', 'b2b3', 'c2c3', 'd2d3', 'e2e3', 'f2f3', 'g2a3', 'h2a3'])
        legal_moves.extend(['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5', 'a7a5', 'b7b5', 'c7c5', 'd7d5', 'e7e5', 'f7f5', 'g7g5', 'h7h5'])
        legal_moves.extend(['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6', 'a7a6', 'b7b6', 'c8c6', 'd7d6', 'e7e6', 'f7f6', 'g7g6', 'h7h6'])
        
        return legal_moves