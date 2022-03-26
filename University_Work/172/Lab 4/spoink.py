from monster import monster
class Spoink(monster):
	def __init__(self, name):
		self.__name = name
		self.__health = 20
	def __str__(self):
		return (self.getName()+ ": "+ self.getDescription())
	def getName(self):
		return self.__name
	def getDescription(self):
		return "The psychic type pokemon!"
	def basicAttack(self,enemy):
		return enemy.doDamage(-1)
	def basicName(self):
		return("Confuse Ray")
	def defenseAttack(self,enemy):
		enemy.doDamage(2)
	def defenseName(self):
		return "Magic Coat"
	def specialAttack(self,enemy):
		self.doDamage(-5)
	def specialName(self):
		return "Psybeam"
	def getHealth(self):
		return self.__health
	def doDamage(self,damage):
		self.__health += damage
	def resetHealth(self):
		self.__health = 20
