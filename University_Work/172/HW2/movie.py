from media import Media

class Movie(Media):

	def __init__(self, type, name, rating, director, runtime):
		super().__init__(type, name, rating)
		self.__director = director
		self.__runtime = runtime
	
	def __str__(self):
		return 'With a runtime of ' +str(self.__runtime) +' minutes, and the director ' +self.__director +', ' +str(super().__str__())
	
	def get_director(self):
		return self.__director
	
	def set_director(self, new_director):
		self.__director = new_director
	
	def get_runtime(self):
		return self.__runtime
	
	def set_runtime(self, new_runtime):
		self.__runtime = new_runtime
		
	def play(self):
		print(super().get_name(), ', playing now', sep='')
		