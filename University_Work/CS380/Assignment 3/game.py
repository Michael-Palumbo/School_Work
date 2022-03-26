import util

class Player():
	def __init__(self, character):
		self.character = character # Either X or O

	def choose_action(self, state):
		pass

class Game():
	# Allows for creating a new game with an initial state and two players
	def __init__(self, initial_state, player1, player2):
		self.cur_state = initial_state
		self.player1 = player1
		self.player2 = player2 

	def play(self):
		visited_states = [self.cur_state.clone()]

		players = [self.player1, self.player2]
		turn = 0
		while True:
			current_player = players[turn%2] # Alternates between the list (and also keeps track of turns, how fun)
			current_player.choose_action(self.cur_state)
			visited_states.append(self.cur_state.clone())
			util.pprint(self.cur_state)
			# A player won, and its game over
			if self.cur_state.game_over(): 
				return (self.cur_state.winner(), visited_states)
			# A player did not win, increment the turn and move to the next round

			turn += 1