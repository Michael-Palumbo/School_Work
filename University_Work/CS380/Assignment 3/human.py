import game

class HumanPlayer(game.Player):
	def __init__(self, character):
		super().__init__(character)

	def choose_action(self, state):
		actions = state.actions(self.character)
		for num, action in enumerate(actions):
			print("%d:"%num, action)

		while True:
			inp = int(input("Please choose an action: "))
			if 0 <= inp < len(actions):
				break
			print("That is not in range!")

		state.execute(actions[inp])