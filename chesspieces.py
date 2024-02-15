#init gameanalyzer
#from chessboard import Chessboard.PlayerColor
import pygame
import chessboard


scale_factor = 0.85
class Chesspiece:
    
    def __init__(self, color):
        self.color = color
        self.image = None
        #self.isCapturable = isCapturable
    
    def isPieceCapturable():
        pass
    def loadImage(self):
        pass



class Pawn(Chesspiece):
    def __init__(self, color, IsPawnsFirstMove=True):
        super().__init__(color)
        self.IsPawnsFirstMove = IsPawnsFirstMove
        self.image = self.loadImage()

    def loadImage(self):
        if self.color == chessboard.Chessboard.PlayerColor.WHITE:
            img = pygame.image.load("pieces_icons_white/P60.png")
            final_image = pygame.transform.smoothscale(img, (int(img.get_width() * scale_factor), int(img.get_height() * scale_factor)))

        elif self.color == chessboard.Chessboard.PlayerColor.BLACK:
            img = pygame.image.load("pieces_icons_black/P60.png")  
            final_image = pygame.transform.smoothscale(img, (int(img.get_width() * scale_factor), int(img.get_height() * scale_factor)))
        return final_image

    
    def getLegalMoves():
        #call gameanalyzer()
        pass

    def isCapturable():
        pass




class Knight(Chesspiece):
    def __init__(self, color):
        super().__init__(color)
        self.image = self.loadImage()

    def getLegalMoves():
        pass

    def isCapturable():
        pass
    def loadImage(self):
        if self.color == chessboard.Chessboard.PlayerColor.WHITE:
            img = pygame.image.load("pieces_icons_white/N60.png")
            final_image = pygame.transform.smoothscale(img, (int(img.get_width() * scale_factor), int(img.get_height() * scale_factor)))

        elif self.color == chessboard.Chessboard.PlayerColor.BLACK:
            img = pygame.image.load("pieces_icons_black/N60.png")  
            final_image = pygame.transform.smoothscale(img, (int(img.get_width() * scale_factor), int(img.get_height() * scale_factor)))
        return final_image




class Bishop(Chesspiece):
    def __init__(self, color):
        super().__init__(color)
        self.image = self.loadImage()

    def getLegalMoves():
        pass

    def isCapturable():
        pass
    def loadImage(self):
        if self.color == chessboard.Chessboard.PlayerColor.WHITE:
            img = pygame.image.load("pieces_icons_white/B60.png")
            final_image = pygame.transform.smoothscale(img, (int(img.get_width() * scale_factor), int(img.get_height() * scale_factor)))

        elif self.color == chessboard.Chessboard.PlayerColor.BLACK:
            img = pygame.image.load("pieces_icons_black/B60.png")  
            final_image = pygame.transform.smoothscale(img, (int(img.get_width() * scale_factor), int(img.get_height() * scale_factor)))
        return final_image



class Rook(Chesspiece):
    
    def __init__(self, color):
        super().__init__(color)
        self.image = self.loadImage()

    def getLegalMoves():
        pass

    def isCapturable():
        pass
    def loadImage(self):
        if self.color == chessboard.Chessboard.PlayerColor.WHITE:
            img = pygame.image.load("pieces_icons_white/R60.png")
            final_img = pygame.transform.smoothscale(img, (int(img.get_width() * scale_factor), int(img.get_height() * scale_factor)))

        elif self.color == chessboard.Chessboard.PlayerColor.BLACK:
            img = pygame.image.load("pieces_icons_black/R60.png")  
            final_img = pygame.transform.smoothscale(img, (int(img.get_width() * scale_factor), int(img.get_height() * scale_factor)))
        
        return final_img



class Queen(Chesspiece):
    def __init__(self, color):
        super().__init__(color)
        self.image = self.loadImage()

    def getLegalMoves():
        pass

    def isCapturable():
        pass
    
    def loadImage(self):
        if self.color == chessboard.Chessboard.PlayerColor.WHITE:
            img = pygame.image.load("pieces_icons_white/Q60.png")
            final_image = pygame.transform.smoothscale(img, (int(img.get_width() * scale_factor), int(img.get_height() * scale_factor)))

        elif self.color == chessboard.Chessboard.PlayerColor.BLACK:
            img = pygame.image.load("pieces_icons_black/Q60.png")  
            final_image = pygame.transform.smoothscale(img, (int(img.get_width() * scale_factor), int(img.get_height() * scale_factor)))
        return final_image



class King(Chesspiece):
    def __init__(self, color, isCheck=False, isCheckMate=False):
        super().__init__(color)
        self.image = self.loadImage()
        self.isCheck = isCheck
        self.isCheckMate = isCheckMate

    def loadImage(self):
        if self.color == chessboard.Chessboard.PlayerColor.WHITE:
            img = pygame.image.load("pieces_icons_white/K60.png")
            final_image = pygame.transform.smoothscale(img, (int(img.get_width() * scale_factor), int(img.get_height() * scale_factor)))

        elif self.color == chessboard.Chessboard.PlayerColor.BLACK:
            img = pygame.image.load("pieces_icons_black/K60.png")  
            final_image = pygame.transform.smoothscale(img, (int(img.get_width() * scale_factor), int(img.get_height() * scale_factor)))
        return final_image
    
    def getLegalMoves():
        pass


    def isKingCheck():
        pass

    def isKingCheckMate():
        pass
    

        