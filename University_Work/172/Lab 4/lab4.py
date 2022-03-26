#Mark Boady and Matthew Burlick
#Drexel University 2018
#CS 

from boady import boady
from medlock import medlock
from spoink import Spoink
from dragonite import Dragonite

import random

#This function has two monsters fight and returns the winner
def monster_battle(m1, m2):

	#first reset everyone's health!
	#####TODO######
	m1.resetHealth()
	m2.resetHealth()

	#next print out who is battling
	print("Starting Battle Between")
	print(m1.getName()+": "+m1.getDescription())
	print(m2.getName()+": "+m2.getDescription())


	#Whose turn is it?
	attacker = None
	defender = None

	attacker = m1 if random.randint(0,1) == 0 else m2
	defender = m1 if attacker == m2 else m2

	#Select Randomly whether m1 or m2 is the initial attacker
	#to other is the initial definder
	######TODO######


	print(attacker.getName()+" goes first.")
	#Loop until either 1 is unconscious or timeout
	while( m1.getHealth() > 0 and m2.getHealth() > 0):
		#Determine what move the monster makes
		#Probabilities:
		#	60% chance of standard attack
		#	20% chance of defense move
		#	20% chance of special attack move

		#Pick a number between 1 and 100
		move = random.randint(1,100)
		#It will be nice for output to record the damage done
		before_health=defender.getHealth()

		#for each of these options, apply the appropriate attack and
		#print out who did what attack on whom
		if( move >=1 and move <= 60):
			attacker.basicAttack(defender)
			print(attacker.getName(), 'used', attacker.basicName(), 'on', defender.getName())
			#Attacker uses basic attack on defender
			######TODO######
		elif move>=61 and move <= 80:
			attacker.defenseAttack(defender)
			print(attacker.getName(), 'used', attacker.defenseName(), 'on', defender.getName())
			#Defend!
			######TODO######
		else:
			attacker.specialAttack(defender)
			print(attacker.getName(), 'used', attacker.specialName(), 'on', defender.getName())
			#Special Attack!
			######TODO######

		#Swap attacker and defender
		######TODO######
		attacker, defender = defender, attacker
		print(m1.getName(), 'has', m1.getHealth(), 'health')
		print(m2.getName(), 'has', m2.getHealth(), 'health')
		#Print the names and healths after this round
		######TODO######

	return m1 if m2.getHealth() == 0 else m2
	#Return who won
	######TODO######

#----------------------------------------------------
if __name__=="__main__":
	#Every battle should be different, so we need to
	#start the random number generator somewhere "random".
	#With no input Python will set the seed

	#random.seed(0) This makes no sense
	d = Dragonite('Bawls')
	b = Spoink('Baller')
	print(d)
	winner1 = monster_battle(b, d)
	print(winner1.getName(), 'is the winner of round 1!')
	#
	# winner2 = monster_battle(medlock(), Spoink('Kiara'))
	# print(winner2.getName(), 'is the winner of round 2!')
	#
	# largeWinner = monster_battle(winner1, winner2)
	# print(largeWinner.getName(), 'is the winner of the whole thing!')

	#Print out who won
	####TODO####
