import abc
class Drawable(metaclass=abc.ABCMeta):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__visible = True

    def setLocation(self,x , y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getVisible(self):
        return self.__visible

    def setVisible(self, v):
        self.__visible = v

    def setX(self,x):
        self.__x = x

    def setY(self,y):
        self.__y =y

    @abc.abstractmethod
    def draw(self, surface):
        pass

    @abc.abstractmethod
    def get_rect(self):
        pass
