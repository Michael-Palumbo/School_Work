from media import Media

class Song(Media):

	def __init__(self, type, name, rating, artist, album):
		super().__init__(type, name, rating)
		self.__artist = artist
		self.__album = album
	
	def __str__(self):
		return 'With the album ' +self.__album +', the artist ' +self.__artist +', ' +str(super().__str__())
	
	def get_artist(self):
		return self.__artist
	
	def set_artist(self, new_artist):
		self.__artist = new_artist
	
	def get_album(self):
		return self.__runtime
	
	def set_album(self, new_album):
		self.__album = new_album
		
	def play(self):
		print(super().get_name(), ' by ', self.__artist, ', playing now', sep='')