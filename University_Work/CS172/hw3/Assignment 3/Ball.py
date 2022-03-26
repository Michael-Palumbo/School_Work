from Drawable import *
import pygame
class Ball(Drawable):
    def __init__(self,x, y, r):
        super().__init__(x, y)
        self.__r = r
        self.__color = (250,0,0)
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

    # Update ball's position by velocity
    def update(self):
        self.setX(self.getX()+self.get_dx())
        self.setY(self.getY()+self.get_dy())
        # If ball is in air, apply gravity constant to Y component, if on ground apply friction to X component
        if self.__falling:
            self.__dy += self.__g
        else:
            self.friction()


    def get_r(self):
        return self.__r

    def get_dx(self):
        return self.__dx * self.__dt

    def get_dy(self):
        return self.__dy * self.__dt

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

    # Reflects the Balls Y velocity so it bounces, also stops it's bounce when it starts boucing really small
    def bounce(self):
        self.__dy *= -self.__rep
        if abs(self.get_dy()) < 4:
            self.__dy = 0
            self.__falling = False

    # Applies friction, only called when it hits the ground, or on the ground
    def friction(self):
        self.__dx *= self.__fric
