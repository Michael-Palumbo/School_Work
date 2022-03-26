from Media import *

class Song(Media):

    def __init__(self, type, name, rating, Artist, Album):
        super().__init__(type, name,rating)
        self.__Artist = Artist
        self.__Album = Album

    # Calls the inherited string method and then attaches it's own attributes
    def __str__(self):
        s =  super().__str__()
        s += "Artist: "+self.__Artist +"\n"
        s += "Album: "+self.__Album+"\n"
        return s

    def play(self):
        print(super().getName(), "by",self.__Artist,"is now playing")

    # Getters
    def getArtist(self):
        return self.__Artist

    def getAlbum(self):
        return self.__Album

    # Setters
    def setArtist(self, d):
        self.__Artist = d

    def setAlbum(self, rt):
        self.__Album = rt
