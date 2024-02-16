from chessboard import Chessboard
from gameanalyzer import Gameanalyzer
from move_generator import MoveGenerator
from chesspieces import Rook
import pygame


class Chessgame:
    
    def __init__(self, analyzer):
        self.gameAnalyzer = analyzer
        self.isGameOver = False
    
    def endGame(self):
        pass
    
    def move(self, board, screen, sourceSquare, destSquare):
        if sourceSquare.occupied_by is not None:
            piece = sourceSquare.occupied_by
            destSquare.occupy(piece)
            sourceSquare.is_occupied = False
            sourceSquare.occupied_by = None

            src_file_index = board.files.index(sourceSquare.file_rank[0])
            src_rank_index = board.ranks.index(sourceSquare.file_rank[1])

            dst_file_index = board.files.index(destSquare.file_rank[0])
            dst_rank_index = board.ranks.index(destSquare.file_rank[1])

            board.board[src_rank_index][src_file_index] = sourceSquare
            board.board[dst_rank_index][dst_file_index] = destSquare
            
        
        else:
            print("Something went wrong. board: ", board)
            print("sourceSquare:", sourceSquare)
            print("destSquare:", destSquare)
        
        
        board.updateDisplay(screen)

        return board
        
        
        
        
         
        
    
    





#pygame inits################################################
pygame.init()
WIDTH, HEIGHT = 450, 450


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess by Mati")
clock = pygame.time.Clock()
#############################################################


cb = Chessboard()
analyzer = Gameanalyzer()
game = Chessgame(analyzer)
legalMoveGenerator = MoveGenerator()


running = True
source_square = None
dest_square = None
while running:   
    #pygame.draw.rect(screen, (255,20,199), square.rect)
    cb.drawBoard(screen)
        
        
    while game.isGameOver is False:

        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game.isGameOver = True
        
            
            #select a piece
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                source_square = cb.getClickedOnSquare(mouse_x, mouse_y)
            
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dest_square = cb.getClickedOnSquare(mouse_x, mouse_y)
            
            if source_square is not None and dest_square is not None:
                 cb = game.move(cb, screen, source_square, dest_square)
                 #make source_square empty here

            
        
            
            
    
            

        clock.tick(60)  
        pygame.display.flip()




pygame.quit()

