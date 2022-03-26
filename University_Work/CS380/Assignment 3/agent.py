import game
import random
import connect3
import util 

class RandomPlayer(game.Player):
	def __init__(self, character):
		super().__init__(character)

	def choose_action(self, state):
		state.execute(random.choice(state.actions(self.character)))

class MinimaxPlayer(game.Player):
	def __init__(self, character):
		super().__init__(character)

	def choose_action(self, state):
		move, backed = self.alpha_beta_search(state)
		state.execute(move)

	# different idea
	def alpha_beta_search(self, state):
		return self.max_value(state, -10000,10000,3) 

	def max_value(self, state, alpha, beta, depth):
		if state.game_over():
			return None, -10000
		if depth <= 0:
			# h = self.h(state, "X" if self.character == "O" else "O")
			# print("Max: H value for below is", h)
			util.pprint(state)
			return None, self.h(state, "X" if self.character == "O" else "O")
		backed = -9999
		move = None
		for m in state.actions(self.character):
			# Just so move has something
			if move == None:
				move = m
			throw_away, pos_backed = self.min_value(state.clone().execute(m), alpha, beta, depth - 1)
			if pos_backed > backed:
				backed = pos_backed
				move = m
			if backed >= beta:
				return move, backed
			alpha = max(alpha, backed)
		return move, backed

	def min_value(self, state, alpha, beta, depth):
		if state.game_over():
			# print("Min: H value for below is inf")
			# util.pprint(state)
			return None, 10000
		if depth <= 0:
			# h = self.h(state, "O" if self.character == "O" else "X")
			# print("Min: H value for below is", h)
			# util.pprint(state)
			return None, self.h(state, "O" if self.character == "O" else "X")
		backed = 9999
		move = None
		for m in state.actions("X" if self.character == "O" else "O"):
			# Just so move has something
			if move == None:
				move = m
			throw_away, pos_backed = self.max_value(state.clone().execute(m), alpha, beta, depth - 1)
			if pos_backed < backed:
				backed = pos_backed
				move = m
			if backed <= alpha:
				return move, backed
			beta = min(beta, backed)
		return move, backed

	# Key notes
	# Look to see if anyone is close to making it, if opponent is close rate negatively, vise versa
	# Favor going defensive rather than offesive
	# I noticed this isn't the strongest since it misses some obviouse moves
	def h(self, state, character):
		deltas = [(+1, 0), (0, +1), (+1, +1), (-1, +1),(-1, 0), (0, -1), (-1, -1), (+1, -1)]
		points = 0

		for x in range(state.max_x):
			for y in range(state.max_y):
				c = state.get(x, y)
				# if 2 pieces next to each other are the same, and the apposing side isn't blocked, weight it hard
				for dx, dy in deltas:
					# X |  | X piece can go inbetween
					if c == connect3.Cell.EMPTY:
						if state.get(x+dx, y+dy) == state.get(x-dx, y-dy) and state.get(x+dx, y+dy) != connect3.Cell.EMPTY and state.get(x+dx, y+dy) != None:
							if state.get(x+dx,y+dy) == character:
								# print(dx,dy,x,y,"plus 1 for",state.get(x+dx, y+dy),state.get(x-dx, y-dy),"for character",character)
								points += 1
							else:
								# print(dx,dy,x,y,"minus 3 for .| |.",state.get(x+dx, y+dy),state.get(x-dx, y-dy),"for character",character)
								points -= 3
					#   | X | X 
					elif state.get(x+dx,y+dy) == c:
						if state.get(x-dx, y-dy) == connect3.Cell.EMPTY:
							# Check to see if this is your piece or not
							if c == character:
								# print(dx,dy,x,y,"plus 1 for |.|.",state.get(x+dx, y+dy),c,state.get(x-dx, y-dy),"for character",character)
								points += 1
							else:
								# print(dx,dy,x,y,"minus 3 for |.|.",state.get(x+dx, y+dy),c,state.get(x-dx, y-dy),"for character",character)
								points -= 3
						elif state.get(x-dx, y-dy) != None:# we know it cant be the same color (since they would have won) or empty
							if state.get(x+dx, y+dy) != c:
								# print(dx,dy,x,y,"plus 1 for _|.|.",state.get(x+dx, y+dy),c,state.get(x-dx, y-dy),"for character",character)
								points += 1
		return points
