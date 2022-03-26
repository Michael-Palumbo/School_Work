from media import Media

class Picture(Media):

	def __init__(self, type, name, rating, resolution):
		super().__init__(type, name, rating)
		self.__resolution = resolution
	
	def __str__(self):
		return 'With a resolution of ' +str(self.__resolution) +'dpi, ' +str(super().__str__())
	
	def get_resolution(self):
		return self.__resolution
	
	def set_resolution(self, new_resolution):
		self.__resolution = new_resolution
		
	def show(self):
		print('Showing ', super().get_name(), sep='')