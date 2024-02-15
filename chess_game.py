from chessboard import Chessboard
from gameanalyzer import Gameanalyzer
from move_generator import MoveGenerator
from chesspieces import Chesspiece
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
SQUARE_SIZE = 50
WHITE = (255, 255, 255)
BLACK = (0, 204, 102)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess by Mati")
clock = pygame.time.Clock()
#############################################################

### images ######################
background_image = pygame.image.load("chessboard_coordinates.png")
## piece images in chesspieces class
#################################


cb = Chessboard(None, isGameOver=False)

analyzer = Gameanalyzer()
game = Chessgame(analyzer)

legalMoveGenerator = MoveGenerator()



running = True
while running:    
    screen.blit(background_image, (0,0))
    
    for row in range(8):
        for col in range(8):
            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (x,y, SQUARE_SIZE, SQUARE_SIZE))
            
            
            square = cb.board[row][col]
            pygame.draw.rect(screen, (255, 0, 0), square.rect)
            if square.occupied_by is not None:
                pygame.draw.rect(screen, square.squareColor, (square.abs_x, square.abs_y, SQUARE_SIZE, SQUARE_SIZE))
                screen.blit(square.occupied_by.image, (square.abs_x, square.abs_y))
    
    pygame.display.flip()
    
    
    




    



    
            
            
        

    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print("mouse coord:", mouse_x, mouse_y)
            x,y = cb.square_mapping['e8']
            print(x,y)
            pygame.draw.rect(screen, 'red', (x,y, SQUARE_SIZE, SQUARE_SIZE))
            if mouse_x >= x and mouse_x <= x + 50:
                if mouse_y>= y and mouse_y <= y+ 50:
                    print("within bounds of square!!")
            # if clicked on a valid square that != null

            #print: clicked on square: [square] where resides: PAWN.Black
            
    #print(event)
            
        

    
    

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