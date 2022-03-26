from monster import monster

class medlock(monster):
	def __init__(self,name):
		self.__name = name
		self.__health = 30

	def __str__(self):
		return self.getName() +' is a ' +self.getDescription()

	def getName(self):
		return self.__name

	def getDescription(self):
		return 'CS 172 Professor'

	#Basic Attack Move
	#This will be the most common attack the monster makes
	#You are passed the monster you are fighting
	def basicAttack(self,enemy):
		enemy.doDamage(-1)

	#Print the name of the attack used
	def basicName(self):
		return 'Lecture'

	#Defense Move
	#This move is used less frequently to
	#let the monster defend itself
	def defenseAttack(self,enemy):
		enemy.doDamage(4)

	#Print out the name of the attack used
	def defenseName(self):
		return 'Bad Directions'

	#Special Attack
	#This move is used less frequently
	#but is the most powerful move the monster has
	def specialAttack(self,enemy):
		enemy.doDamage(-6)
		self.doDamage(1)

	def specialName(self):
		return 'Reading Check'

	#Health Management
	#A monster at health <= 0 is unconscious
	#This returns the current health level
	def getHealth(self):
		return self.__health

	#This function is used by the other monster to
	#either do damage (positive int) or heal (negative int)
	def doDamage(self,damage):
		self.__health += damage

	#Reset Health for next match
	def resetHealth(self):
		self.__health = 30
