from Drawable import *
import pygame
class Ball(Drawable):
    def __init__(self,x, y, r):
        super().__init__(x, y)
        self.__r = r
        self.__color = (111,111,111)
        self.__dx = 0
        self.__dy = 0
        self.__dt = .1
        self.__g = 6.67
        self.__falling = False
        self.__rep = .7
        self.__fric = .5

    def draw(self, surface):
        pygame.draw.circle(surface, self.__color, (int(self.getX()), int(self.getY())), self.__r)

    def get_rect(self):
        return pygame.Rect(self.getX()-self.__r, self.getY()-self.__r, 2*self.__r, 2*self.__r)

    def update(self):
        self.setX(self.getX()+self.__dx*self.__dt)
        self.setY(self.getY()+self.__dy*self.__dt)
        if self.__falling:
            self.__dy += self.__g

    def get_r(self):
        return self.__r

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self, dx):
        self.__dx = dx

    def set_dy(self, dy):
        self.__dy = dy

    def get_dt(self):
        return self.__dt

    def get_falling(self):
        return self.__falling

    def set_falling(self, c):
        self.__falling = c

    def bounce(self):
        self.__dy *= -self.__rep
        if abs(self.__dy * self.__dt) < 4:
            self.__dy = 0
            self.__falling = False

    def friction(self):
        self.__dx *= self.__fric
