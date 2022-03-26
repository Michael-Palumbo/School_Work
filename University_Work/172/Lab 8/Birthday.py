class Birthday:
	def __init__(self, day, month, year):
		self.__day = day
		self.__month = month
		self.__year = year
		
	def __str_(self):
		return 'Birth date: ' +str(month) +'/' +str(day) +'/' +str(year)
	
	def __hash__(self):
		return (self.__day + self.__month + self.__year)%12
		
	def __eq__(self, other):
		return self.get_attr() == other.get_attr()
	
	def get_attr(self):
		return [self.__day, self.__month, self.__year]
	
	def get_day(self):
		return self.__day
		
	def get_month(self):
		return self.__month
		
	def get_year(self):
		return self.__year
		
	def set_day(self, d):
		self.__day = d
		
	def set_month(self, m):
		self.__month = m
		
	def set_year(self, y):
		self.__year = y
	