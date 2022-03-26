#File:      DrawableObjects.py
#Purpose:   Demo of a basic program using pygame
#Author:    A. Medlock
#Date:      February 4, 2019

import pygame
import abc

# abstract class to represent a drawable obejct
class Drawable(metaclass = abc.ABCMeta):
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def getLocation(self):
        return (self.__x, self.__y)

    def setLocation(self, point):
        self.__x = point[0]
        self.__y = point[1]

    def moveRight(self):
        self.__x += 1

    def __str__(self):
        return "located at (" + str(self.__x) + "," + str(self.__y) +")"

    @abc.abstractmethod
    def draw(self, surface):
        pass

    @abc.abstractmethod
    def getRectangle(self):
        pass

      
# derived class that represents a House
class House(Drawable):
    def __init__(self, x = 0, y = 0, color = (0,0,0)):
        super().__init__(x, y)
        self.__color = color

    def __str__(self):
        return "A house " + super().__str__()

    def draw(self, surface):
        location = self.getLocation()
        pygame.draw.rect(surface, self.__color, [location[0]-15, location[1]-10, 30, 20])
        pygame.draw.polygon(surface, self.__color, [(location[0]-15, location[1]-10), (location[0]+15, location[1]-10), (location[0], location[1]-20)])

    def getRectangle(self):
        location = self.__getLocation()
        return pygame.Rect( [location[0] - 15, location[1] - 20, 30, 30] )
      
# derived class that represents a Snowman
class Snowman(Drawable):
    def __init__(self, x = 0, y = 0, color = (0,0,0)):
        super().__init__(x, y)
        self.__color = color	

    def __str__(self):
        return "A snowman " + super().__str__()
	
    def draw(self,surface):
        location = self.getLocation()
        pygame.draw.circle(surface, self.__color, [location[0], location[1]], 20)
        pygame.draw.circle(surface, self.__color, [location[0], location[1] - 20], 15)
        pygame.draw.circle(surface, self.__color, [location[0], location[1] - 40], 10)

    def getRectangle(self):
        location = self.__getLocation()
        return pygame.Rect( [location[0] - 20, location[1] - 45, 40, 90] )
    
# derived class for Text
class Text(Drawable):
    def __init__(self, message = "Pygame", x = 0, y = 0, color = (0,0,0)):
        super().__init__(x, y)
        fontObj = pygame.font.Font("freesansbold.ttf", 26)
        self.__surface = fontObj.render(message, True, color)
	
    def draw(self, surface):
        surface.blit(self.__surface, self.getLocation())

    def getRectangle(self):
        location = self.__getLocation()
        return pygame.Rect( [location[0], location[1], len(message) * 26, 26] )


# main scrip starts here
#initialization                           
pygame.init()
surface = pygame.display.set_mode((400, 300))
pygame.display.set_caption('My Drawable Objects')
fpsclock = pygame.time.Clock()

# list of drawable objects to be displayed
drawables = []                 
newHouse = House(100, 100, (255, 0, 0))
drawables.append(newHouse)
newSnow = Snowman(200, 100, (255, 255, 255))
drawables.append(newSnow)
newText = Text('Python and Pygame!', 75, 200, (0, 0, 255))
drawables.append(newText)

# game loop
while True: 
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()

    surface.fill((204, 229, 255))
    for drawable in drawables:
        drawable.draw(surface)

    ''' animation 
    surface.fill((204, 229, 255))
    for drawable in drawables:
        drawable.moveRight()
        drawable.draw(surface)
    '''
    pygame.display.update()
    fpsclock.tick(30)

# a collision detection funcion
def collisionDetection(rect1, rect2) :
    if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y) :
        return True
    return False
