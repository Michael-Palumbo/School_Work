import agent

import rgb
import util
	
# heuristic function counts the amount of colors next to each other
def heuristic(state):
	deltas = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
	count = 0
	for x in range(state.size):
		for y in range(state.size):
		# if self.get(x, y) == rgb.Cell.EMPTY:
			for dx, dy in deltas:
				x2, y2 = x + dx, y + dy
				if state.is_legal(x2, y2) and state.get(x,y) == state.get(x2,y2):
					count += 1
	return count

# Basically copied from rgb just added more elif(s) for the 
if __name__ == "__main__":
	cmd = util.get_arg(1)
	if cmd:
		state = rgb.State(util.get_arg(2))
		if cmd == 'print':
			util.pprint(state)
		elif cmd == 'goal':
			print(state.is_goal())
		elif cmd == 'actions':
			for action in state.actions():
				print(action)
		elif cmd == 'random':
			node = agent.Agent.random_walk(state, 8) # hard code 8 iterations
			agent.Agent.my_print(node)
		elif cmd == 'bfs':
			node, count = agent.Agent.bfs(state)
			agent.Agent.my_print(node)
			print(count)
		elif cmd == 'dfs':
			node, count = agent.Agent.dfs(state)
			agent.Agent.my_print(node)
			print(count)
		elif cmd == 'a_star':
			node, count = agent.Agent.a_star(state, heuristic)
			agent.Agent.my_print(node)
			print(count)