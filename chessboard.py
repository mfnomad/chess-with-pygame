from enum import Enum
from chesspieces import Pawn, Rook, Bishop, Knight, Queen, King
from square import Square
import pygame

SQUARE_SIZE = 50
WHITE = (255, 255, 255)
BLACK = (0, 204, 102)


class Chessboard:

    class PlayerColor(Enum):
        WHITE = 1
        BLACK = 2
    
    
    
    def __init__(self):
        self.squarePieceMapping = self.createSquarePieceMapping()
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        
        self.files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.ranks = ['8', '7', '6', '5', '4', '3', '2', '1']
        self.squares = self.generateSquares()
        self.setupBoard()

    def areCoordinatesInSquare(self, mouse_x, mouse_y, square):
        return square.rect.collidepoint(mouse_x, mouse_y)
    
    def getClickedOnSquare(self, mouse_x, mouse_y):
        for row in range(8):
                for col in range(8):
                    square = self.board[row][col]
                    if(self.areCoordinatesInSquare(mouse_x, mouse_y, square)):
                        return square
        return None

            

    def generateSquares(self):
        squares = []
        for y in range(8):
            row = []
            for x in range(8):
                fileRank = self.files[x] + self.ranks[y]
                square = Square(file_rank=fileRank,x=x,y=y)
                row.append(square)
            squares.append(row)
        return squares
    
    def setupBoard(self):
        for y in range(8):
            for x in range(8):
                piece_symbol = self.board[y][x]
                if piece_symbol != ' ':
                    piece = self.squarePieceMapping[piece_symbol]
                    self.squares[y][x].occupy(piece)
                
                self.board[y][x] = self.squares[y][x]
            
    
    def createSquarePieceMapping(self):
        piece_mapping  = {
            'p' : Pawn(Chessboard.PlayerColor.BLACK),
            'P' : Pawn(Chessboard.PlayerColor.WHITE),
            
            'r' : Rook(Chessboard.PlayerColor.BLACK),
            'R' : Rook(Chessboard.PlayerColor.WHITE),
            
            'n' : Knight(Chessboard.PlayerColor.BLACK),
            'N' : Knight(Chessboard.PlayerColor.WHITE),

            'b' : Bishop(Chessboard.PlayerColor.BLACK),
            'B' : Bishop(Chessboard.PlayerColor.WHITE),

            'q' : Queen(Chessboard.PlayerColor.BLACK),
            'Q' : Queen(Chessboard.PlayerColor.WHITE),

            'k' : King(Chessboard.PlayerColor.BLACK),
            'K' : King(Chessboard.PlayerColor.WHITE),

            ' ' : None

        }
        return piece_mapping
    
    
    def drawBoard(self, screen):
        background_image = pygame.image.load("chessboard_coordinates.png")
        screen.blit(background_image, (0,0))
        for row in range(8):
            for col in range(8):
                x = col * SQUARE_SIZE
                y = row * SQUARE_SIZE
                color = WHITE if (row + col) % 2 == 0 else BLACK
                pygame.draw.rect(screen, color, (x,y, SQUARE_SIZE, SQUARE_SIZE))
            
            
                square = self.board[row][col]
                if square.is_occupied():
                    #pygame.draw.rect(screen, square.squareColor, (square.abs_x, square.abs_y, SQUARE_SIZE, SQUARE_SIZE))
                    screen.blit(square.occupied_by.image, (square.abs_x, square.abs_y))

    def updateDisplay(self, screen):
        for row in range(8):
            for col in range(8):
                square = self.board[row][col]
                if square.occupied_by is not None:
                    screen.blit(square.occupied_by.image, (square.abs_x, square.abs_y))

        

                  


    


            

        
    
    
        

    
        
        