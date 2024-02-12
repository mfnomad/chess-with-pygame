from chessboard import Chessboard
from gameanalyzer import Gameanalyzer
from move_generator import MoveGenerator
import chesspieces
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
w_pawn_image = pygame.image.load("pieces_icons_white/P60.png")  
w_rook_image = pygame.image.load("pieces_icons_white/R60.png")
w_knight_image = pygame.image.load("pieces_icons_white/N60.png")
w_bishop_image = pygame.image.load("pieces_icons_white/B60.png")
w_queen_image = pygame.image.load("pieces_icons_white/Q60.png")
w_king_image = pygame.image.load("pieces_icons_white/K60.png")

b_pawn_image = pygame.image.load("pieces_icons_black/P60.png")  
b_rook_image = pygame.image.load("pieces_icons_black/R60.png")
b_knight_image = pygame.image.load("pieces_icons_black/N60.png")
b_bishop_image = pygame.image.load("pieces_icons_black/B60.png")
b_queen_image = pygame.image.load("pieces_icons_black/Q60.png")
b_king_image = pygame.image.load("pieces_icons_black/K60.png")
#################################


# Scale the images
# Define the scale factor (90% of the original size)
scale_factor = 0.85

# Scale the images
w_pawn_image = pygame.transform.smoothscale(w_pawn_image, (int(w_pawn_image.get_width() * scale_factor), int(w_pawn_image.get_height() * scale_factor)))
w_rook_image = pygame.transform.smoothscale(w_rook_image, (int(w_rook_image.get_width() * scale_factor), int(w_rook_image.get_height() * scale_factor)))
w_knight_image = pygame.transform.smoothscale(w_knight_image, (int(w_knight_image.get_width() * scale_factor), int(w_knight_image.get_height() * scale_factor)))
w_bishop_image = pygame.transform.smoothscale(w_bishop_image, (int(w_bishop_image.get_width() * scale_factor), int(w_bishop_image.get_height() * scale_factor)))
w_queen_image = pygame.transform.smoothscale(w_queen_image, (int(w_queen_image.get_width() * scale_factor), int(w_queen_image.get_height() * scale_factor)))
w_king_image = pygame.transform.smoothscale(w_king_image, (int(w_king_image.get_width() * scale_factor), int(w_king_image.get_height() * scale_factor)))

b_pawn_image = pygame.transform.smoothscale(b_pawn_image, (int(b_pawn_image.get_width() * scale_factor), int(b_pawn_image.get_height() * scale_factor)))
b_rook_image = pygame.transform.smoothscale(b_rook_image, (int(b_rook_image.get_width() * scale_factor), int(b_rook_image.get_height() * scale_factor)))
b_knight_image = pygame.transform.smoothscale(b_knight_image, (int(b_knight_image.get_width() * scale_factor), int(b_knight_image.get_height() * scale_factor)))
b_bishop_image = pygame.transform.smoothscale(b_bishop_image, (int(b_bishop_image.get_width() * scale_factor), int(b_bishop_image.get_height() * scale_factor)))
b_queen_image = pygame.transform.smoothscale(b_queen_image, (int(b_queen_image.get_width() * scale_factor), int(b_queen_image.get_height() * scale_factor)))
b_king_image = pygame.transform.smoothscale(b_king_image, (int(b_king_image.get_width() * scale_factor), int(b_king_image.get_height() * scale_factor)))

####



cb = Chessboard(None, isGameOver=False)
initial_cb = cb.initialChessboardState()

analyzer = Gameanalyzer()
game = Chessgame(analyzer)

legalMoveGenerator = MoveGenerator()


#cb.printGameState()
running = True



while running:    
    screen.blit(background_image, (0,0))
    
    for row in range(8):
        for col in range(8):
            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (x,y, SQUARE_SIZE, SQUARE_SIZE))


    start_y = 350
    for rank in cb.ranks:
        start_x = 0
        for file in cb.files:
            piece = initial_cb[cb.square_index_mapping[file + rank][1]][cb.square_index_mapping[file + rank][0]]
            
            if piece is not None:
                if piece.color == Chessboard.PlayerColor.WHITE:
                    if isinstance(piece, chesspieces.Pawn):
                        piece_image = w_pawn_image
                    elif isinstance(piece, chesspieces.Bishop):
                        piece_image = w_bishop_image
                    elif isinstance(piece, chesspieces.Knight):
                        piece_image = w_knight_image
                    elif isinstance(piece, chesspieces.King):
                        piece_image = w_king_image
                    elif isinstance(piece, chesspieces.Queen):
                        piece_image = w_queen_image
                    elif isinstance(piece, chesspieces.Rook):
                        piece_image = w_rook_image
                
                elif piece.color == Chessboard.PlayerColor.BLACK:
                    if isinstance(piece, chesspieces.Pawn):
                        piece_image = b_pawn_image
                    elif isinstance(piece, chesspieces.Bishop):
                        piece_image = b_bishop_image
                    elif isinstance(piece, chesspieces.Knight):
                        piece_image = b_knight_image
                    elif isinstance(piece, chesspieces.King):
                        piece_image = b_king_image
                    elif isinstance(piece, chesspieces.Queen):
                        piece_image = b_queen_image
                    elif isinstance(piece, chesspieces.Rook):
                        piece_image = b_rook_image
            
            
            
                screen.blit(piece_image, (start_x, start_y))
            
            start_x += 50
        start_y -= 50
        
        

    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Square clicked: a1 with coordinates: ', cb.square_mapping['a1'])
        print(event)
            
        

    
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