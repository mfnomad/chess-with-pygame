from chessboard import Chessboard
from gameanalyzer import Gameanalyzer
from move_generator import MoveGenerator
from chesspieces import Rook
import pygame


class Chessgame:
    
    def __init__(self, analyzer):
        self.gameAnalyzer = analyzer
    
    def endGame(self):
        pass
    
    def inputMove(self, boardState):
        move = input("Enter your move (in algebraic notation, e.g., 'e2e4'): ")
        print('Move entered:', move)

        if not len(move) >= 2:
            print("Invalid move. Please enter a legal move.")
            return self.inputMove(boardState)  # Return the value obtained from the recursive call
        elif move in legalMoveGenerator.getLegalMoves(boardState):
            print('MOVE IS LEGAL')
            return move
        else:
            print('MOVE NOT LEGAL')
            return self.inputMove(boardState)
    
    





#pygame inits################################################
pygame.init()
WIDTH, HEIGHT = 450, 450


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess by Mati")
clock = pygame.time.Clock()
#############################################################

### images ######################

## piece images in chesspieces class
#################################


cb = Chessboard()

analyzer = Gameanalyzer()
game = Chessgame(analyzer)

legalMoveGenerator = MoveGenerator()







running = True
while running:    
    
        #pygame.draw.rect(screen, (255,20,199), square.rect)
        cb.drawBoard(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #if event.type == pygame.MOUSEBUTTONDOWN:
            
            
    #print(event)
            

        clock.tick(60)  # limits FPS to 60
        pygame.display.flip()





    

pygame.quit()

