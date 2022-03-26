from drawables import *
import pygame

class Ball(drawables):

    def __init__(self, x, y, radius):
        super().__init__(x,y)
        self.__radius = radius
        self.__dx = 0
        self.__dy = 0
        self.__dt = .1
        self.__color = (0,255,0)
        self.__falling = False
        self.__bounce = .7
        self.__friction = .7
        self.__gravity = 6.67


    def getRadius(self):
        return self.__radius

    def draw(self, surface):
        pygame.draw.circle(surface, self.__color, [int(self.getX()), int(self.getY())], self.__radius )

    #Change Position of Ball by velocity components
    def tick(self):
        self.setX( self.getX() - self.__dx*self.__dt )
        self.setY(self.getY() - self.__dy*self.__dt )
        #Gravity should only be applied when it's in the air
        if self.__falling:
            self.__dy -= self.__gravity

    def getDX(self):
        return self.__dx

    def setDX(self, change):
        self.__dx = change

    def getDY(self):
        return self.__dy

    def setDY(self, change):
        self.__dy = change

    def getDT(self):
        return self.__dt

    def getRadius(self):
        return self.__radius

    def getRect(self):
        # We times add (dy*dt) because we want to anticpate the collsion
        return pygame.Rect(self.getX()-self.__radius-self.__dx*self.__dt,self.getY()-self.__dy*self.__dt - self.__radius,self.__radius*2,self.__radius*2)

    def forceFalling(self, change):
        self.__falling = change

    # If the ball is hitting the ground, we want to flip it, if it's bouncing just a tiny bit we want to stop it
    def setFalling(self,change):
        self.__dy *= -self.__bounce
        if abs(self.__dy * self.__dt) < 4:
            self.__dy = 0
            self.__falling = change

    def getFalling(self):
        return self.__falling

    def enactFriction(self):
        self.__dx *= self.__friction
