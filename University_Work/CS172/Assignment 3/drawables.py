# Name: Michael Palumbo
# Section:
# Purpose: Contains all the classe we will be using, sorry that their in the same file

import pygame
import abc
import math

class drawables(metaclass = abc.ABCMeta):

    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__visible = True

    def setVisible(self, change):
        self.__visible = change

    def getVisible(self):
        return self.__visible

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    @abc.abstractmethod
    def draw(self, surface):
        pass

    @abc.abstractmethod
    def getRect(self):
        pass

class Rectangle(drawables):

    def __init__(self, color, x, y, width, height):
        super().__init__(x,y)
        self.__width = width
        self.__height = height
        self.__color = color

    def getWidth(self):
        return self.__width

    def draw(self, surface):
        if self.getVisible():
            # Easy way to get outline, draw rect, then draw small rect inside of it
            pygame.draw.rect(surface, (0,0,0), [self.getX(),self.getY(), self.__width, self.__height])
            pygame.draw.rect(surface, self.__color, [self.getX()+1,self.getY()+1, self.__width-2, self.__height-2])

    def getRect(self):
        return pygame.Rect(self.getX(),self.getY(),self.__width,self.__height)

class Ball(drawables):

    #<----Static Constants---->
    BOUNCE = .7
    FRICTION = .7
    GRAVITY = 6.67

    def __init__(self, x, y, radius):
        super().__init__(x,y)
        self.__radius = radius
        self.__dx = 0
        self.__dy = 0
        self.__dt = .1
        self.__color = (255,0,0)
        self.__falling = False

    def getRadius(self):
        return self.__radius

    def draw(self, surface):
        pygame.draw.circle(surface, self.__color, [int(self.getX()), int(self.getY())], self.__radius )

    # Updates Ball Position By The Velocity
    def tick(self):
        self.setX( self.getX() - self.getDx())
        self.setY(self.getY() - self.getDy() )
        if self.__falling:
            self.__dy -= Ball.GRAVITY
        else:
            self.Friction()

    def getDx(self):
        return self.__dx * self.__dt

    def getDy(self):
        return self.__dy * self.__dt

    def setDx(self, change):
        self.__dx = change

    def setDy(self, change):
        self.__dy = change

    def getRadius(self):
        return self.__radius

    # We need the top left corner, and then 2 times the radius
    def getRect(self):
        return pygame.Rect(self.getX()-self.__radius-self.getDx(),self.getY()-self.__radius-self.getDy(),self.__radius*2,self.__radius*2)

    def setFalling(self, change):
        self.__falling = change

    def getFalling(self):
        return self.__falling

    # Set the DY to the oposite, the ball starts bouncing really small, just set DY to 0
    def bounce(self,change):
        self.__dy *= -Ball.BOUNCE
        if abs(self.getDy()) < 4:
            self.__dy = 0
            self.__falling = change

    def Friction(self):
        self.__dx *= Ball.FRICTION

class Text(drawables):

    def __init__(self, font_type, size,loc):
        super().__init__(loc[0],loc[1])
        pygame.font.init()
        self.__myFont = pygame.font.SysFont(font_type,size)

    # Draws the score to the screen
    def draw(self,surface,score):
        textsurface = self.__myFont.render(f"Score: {score}", False, (0, 0, 0))
        surface.blit(textsurface,(super().getX(),super().getY()))

    def getRect(self):
        # We don't use this
        pass
