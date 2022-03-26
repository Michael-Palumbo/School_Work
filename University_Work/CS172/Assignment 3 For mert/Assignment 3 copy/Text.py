from drawables import *
import pygame

class Text(drawables):

    def __init__(self, font_type, size,loc):
        super().__init__(loc[0],loc[1])
        pygame.font.init()
        self.__myFont = pygame.font.SysFont(font_type,size)

    # Draws the score
    def draw(self,surface,score):
        textsurface = self.__myFont.render(f"Score: {score}", False, (0, 0, 0))
        surface.blit(textsurface,(super().getX(),super().getY()))

    # We never need the boundaries of the text box, but we need to add due to abstract
    def getRect(self):
        pass
