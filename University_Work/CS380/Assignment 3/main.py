import util
# from connect3 import State
import connect3
import game
import human
import agent

players = {"human": human.HumanPlayer , "random": agent.RandomPlayer , "minimax": agent.MinimaxPlayer }

if __name__ == '__main__':
	cmd = util.get_arg(1)
	if cmd:
		if cmd in list(players.keys()):
			game = game.Game(connect3.State(), players[cmd]("X"), players[util.get_arg(2)]("O"))
			winner, history = game.play()
			print("the winner is", winner)
			util.pprint(history)
		elif cmd == 'print':
			state = connect3.State(util.get_arg(2))
			util.pprint(state)
		elif cmd == 'over':
			state = connect3.State(util.get_arg(2))
			print(state.game_over())
		elif cmd == 'winner':
			state = connect3.State(util.get_arg(2))
			print(state.winner())
		elif cmd == 'actions':
			char = util.get_arg(2)
			state = connect3.State(util.get_arg(3))
			util.pprint(state)
			for action in state.actions(char):
				print(action)
