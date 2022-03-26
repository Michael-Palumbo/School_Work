from monster import monster

class Dragonite(monster):
	def __init__(self, name):
		self.__name = name
		self.__health = 20
	def __str__(self):
		return (self.getName()+ ": "+ self.getDescription())
	def getName(self):
		return self.__name
	def getDescription(self):
		return "The dragon flying type pokemon!"
	def basicAttack(self,enemy):
		return enemy.doDamage(-1)
	def basicName(self):
		return("Aqua Jet")
	def defenseAttack(self,enemy):
		enemy.doDamage(2)
	def defenseName(self):
		return "Mist"
	def specialAttack(self,enemy):
		self.doDamage(5)
	def specialName(self):
		return "Hyper Beam"
	def getHealth(self):
		return self.__health
	def doDamage(self,damage):
		self.__health += damage
	def resetHealth(self):
		self.__health = 20
