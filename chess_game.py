from chessboard import Chessboard
from gameanalyzer import Gameanalyzer
from move_generator import MoveGenerator
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





#pygame inits###
pygame.init()
screen = pygame.display.set_mode((457, 457))
pygame.display.set_caption("Chess by Mati")
clock = pygame.time.Clock()

### images ###
background_image = pygame.image.load("chessboard_3.png")
#black_pieces = 
files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


###


####



cb = Chessboard(None, isGameOver=False)
cb.initializeBoard()

analyzer = Gameanalyzer()
game = Chessgame(analyzer)

legalMoveGenerator = MoveGenerator()


#cb.printGameState()
running = True
print(cb.square_mapping['a1'])

while running:
    
    
    screen.fill("purple")
    screen.blit(background_image, (0,0))

    start_y = 47
    for rank in range(8):
        start_x = 48
        for file in files:
            pygame.draw.rect(screen, "red", [start_x, start_y, 45, 45], 1)
            start_x = start_x + 45
        start_y = start_y + 45


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('mouseclicked')
            
        
        #print(event)

    # RENDER YOUR GAME HEREl

    
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60




    

pygame.quit()

'''
#white move
    print('WHITE MOVES')
    playermove = game.inputMove(cb.getGameState)
    cb.move(playermove, Chessboard.PlayerColor.WHITE)
    print('white moved')
    cb.printGameState()
    #cb.move(cb.PlayerColor == Chessboard.WHITE, playermove)
    
    
    
    #LATER:isGameOver == True ??
    playermove = game.inputMove(cb.getGameState)
    cb.move(playermove, Chessboard.PlayerColor.BLACK)
    cb.printGameState()
    break


'''