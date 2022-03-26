import random
import util
# import copy #didn't notice there was a clone

class Node:
	def __init__(self, parent, value):
		self.parent = parent
		self.value = value

	def setParent(self, parent):
		self.parent = parent

	def setValue(self, value):
		self.value = value

	# Depth isn't hard coded value, instead can be found when looking through parents, slower but less work
	def depth(self):
		depth = 0
		node_t = self
		while node_t.parent != None:
			depth += 1
			node_t = node_t.parent
		return depth

	# Functions to kind of "encapsulate" the rgb State functions
	def actions(self):
		return self.value.actions()

	def execute(self, action):
		return self.value.execute(action)

	def is_goal(self):
		return self.value.is_goal()

	# Doesn't clone parent, but does clone node, both will point to the same parent
	def produce_child_copy(self):
		return Node(self, self.value.clone())

	# Wrote this since asking if parent != None wouldn't work if i overwrote __eq__
	def equals(self, node):
		return str(self.value) == str(node.value)

	def __str__(self):
		node = self
		string = ""
		while node != None:
			string += "%d %s\t"%(node.depth(), node.value)
			node = node.parent
		return string

class Agent:

	#state being current state, n states have been visited
	def random_walk(state, n):
		node_pointer = Node(None, state)
		for i in range(n):
			actions = state.actions()
			if len(actions) != 0:
				state = state.clone()
				state.execute(random.choice(actions))
				node_pointer = Node(node_pointer, state)
				# print(node_pointer.value)

		return node_pointer

	# The array contains node, but we only care about values, so I have a helper to only compare values
	def checkArray(node, array):
		inside = False
		for n in array:
			if n.equals(node):
				inside = True
		return inside

	# If the value was found in the array, it's likely we want to know who's its parent, so we use this
	def getNode(node, array):
		for n in array:
			if n.equals(node):
				return n
		return None

	#base search
	def _search(state, breadth, heur):
		OPEN = [Node(None, state)]
		CLOSED = []
		count = 0 # Used to count the iterations 
		while len(OPEN) != 0:
			count += 1

			#Equivalent to first() and rest()
			s = OPEN[0]
			OPEN = OPEN[1:len(OPEN)]

			CLOSED.append(s)

			#### So I had this, but turns out that dfs fails because it takes to many iterations and quits (i'm assuming)
			# dfs will essentially follow the left branch until the left branch is is_goal
			# so we add a depth limit so it's forced to search other branches
			# if not breadth: 
			# 	if s.depth() > 7: #hard coded, the path can only be 7 nodes long
			# 		continue
			
			Agent.my_print(s)

			if s.is_goal():
				return s, count
			
			for r in s.actions():
				# Since we are looking at nodes, and not just values, I decide to give the parent to s right off the bat
				s_p = s.produce_child_copy()
				s_p.execute(r)

				if not Agent.checkArray(s_p, OPEN) and not Agent.checkArray(s_p, CLOSED):
					# s_p.setParent(s) # already done for us 
					if heur != None:
						for i in range(len(OPEN)):
							# Nodes could contain the value, but being we use it literally just here, I decided to choose the slower option
							# Which is throw the value in the heuristic function every time (very slow, but works)
							if heur(OPEN[i].value) > heur(s_p.value):
								OPEN.insert(i, s_p)
								break
						else:
							OPEN.append(s_p)
					elif breadth:
						OPEN.append(s_p)
					else:
						OPEN.insert(0, s_p)
				# If value already exists in array, grab the object and its barent, then compare it to s or it's already parent
				# Note: s_p is no longer the one with s as parent, its the one that exists in OPEN/CLOSED
				elif Agent.checkArray(s_p, OPEN):
					s_p = Agent.getNode(s_p, OPEN)
					if s_p.depth() > s.depth(): # If s's depth is smaller, then make that the new parent of the node
						s_p.setParent(s) # changes parent and depth

				elif Agent.checkArray(s_p, CLOSED):
					s_p = Agent.getNode(s_p, CLOSED)
					if s_p.depth() > s.depth():
						s_p.setParent(s)

	#Breadth-first search
	def bfs(state):
		return Agent._search(state, True, None)

	#depth-first search
	def dfs(state):
		return Agent._search(state, False, None)

	#a-star (follows breadth-first search but also passes the heuristic function)
	def a_star(state, heuristic):
		return Agent._search(state, True, heuristic)

	# Helper function to turn a node to an array, and then pass it to util's pretty_print function
	def my_print(node):
		value_list = [] # wanting to print in the proper order
		while node != None:
			value_list.insert(0, node.value)
			node = node.parent
		util.pprint(value_list)