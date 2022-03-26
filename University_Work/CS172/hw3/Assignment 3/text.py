import pygame
from Drawable import *

class Text(Drawable):
    def __init__(self,x,y):
        super().__init__(x,y)
        pygame.font.init()
        self.__font = pygame.font.SysFont("Times New Roman",37)

    def draw(self, surface, score):
        textsurface = self.__font.render("Score: " + str(score), False, (0, 0, 0))
        surface.blit(textsurface,(super().getX(),super().getY()))

    def get_rect(self):
        pass
