class Media:
	def __init__(self, type, name, rating):
		self.__type = type
		self.__name = name
		self.__rating = rating
	
	def __str__(self):
		return self.__name +' of type ' +self.__type +' has a rating of ' +str(self.__rating)
		
	def get_type(self):
		return self.__type
		
	def set_type(self, new_type):
		self.__type = new_type
		
	def get_name(self):
		return self.__name
		
	def set_name(self, new_name):
		self.__name = new_name
		
	def get_rating(self):
		return self.__rating
		
	def set_rating(self, new_rating):
		self.__rating = new_rating