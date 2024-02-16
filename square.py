import pygame

SQUARE_SIZE = 50
WHITE = (255, 255, 255)
BLACK = (0, 204, 102)


class Square:
    def __init__(self, file_rank, x, y):
        self.x = x
        self.y = y
        self.file_rank = file_rank
        self.width = SQUARE_SIZE
        self.height = SQUARE_SIZE
        self.abs_x = self.x * SQUARE_SIZE
        self.abs_y = self.y * SQUARE_SIZE
        self.occupied_by = None
        
        self.squareColor = WHITE if (x + y) % 2 == 0 else BLACK


        self.rect = self.rect = pygame.Rect(
			self.abs_x,
			self.abs_y,
			self.width,
			self.height
		)

    def occupy(self, piece):
        self.occupied_by = piece
    
    def is_occupied(self):
        return self.occupied_by is not None

    def get_pos(self):
        return (self.x, self.y)

    def get_file_rank(self):
        return self.file_rank
    


    
     