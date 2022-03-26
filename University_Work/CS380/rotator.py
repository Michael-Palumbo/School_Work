import sys
import copy
import random

class Puzzle():
	NEIGHBORS = [[1,0],[-1,0],[0,1],[0,-1]]

	def __init__(self, puzzleString):
		self.puzzleArray = [ list(x) for x in puzzleString.split('|') ]

	def clone(self):
		return copy.deepcopy(self.puzzleArray)

	def rotate(self, y, dx):
		copyArray = self.clone()
		if dx == 1:
			copyArray[y].insert(0, copyArray[y].pop())
		elif dx == -1:
			copyArray[y].append(copyArray[y].pop(0))
		return copyArray

	def get_rotates(self, actions):
		for r in range(len(self.puzzleArray)):
			actions["rotate(%d,-1)"%(r)] = self.rotate(r, -1)
			actions["rotate(%d,1)"%(r)] = self.rotate(r, 1)

	def find_open(self, ):
		for r in range(len(self.puzzleArray)):
			for c in range(len(self.puzzleArray[r])):
				if self.puzzleArray[r][c] == ' ':
					return (r,c)
		return (None, None)

	def swapArray(self, array, p1, p2):
		temp = array[p1[0]][p1[1]]
		array[p1[0]][p1[1]] = array[p2[0]][p2[1]]
		array[p2[0]][p2[1]] = temp

	def slide(self, x1,y1,x2,y2):
		copyArray = self.clone()
		self.swapArray(copyArray, (x1,y1), (x2,y2))
		return copyArray

	def get_slides(self, slide_actions):
		#Rows and Columns are opposite to x and y
		r, c = self.find_open()
		for offset_c, offset_r in self.NEIGHBORS:
			#print(self.puzzleArray, c+offset_c, r+offset_r, c, r,sep='\n')
			if (offset_r != 0 and 0 <= (offset_r + r) < len(self.puzzleArray)):
				slide_actions["slide(%d,%d,%d,%d)"%(c+offset_c, r+offset_r, c, r)] = self.slide(r+offset_r, c+offset_c, r, c)
			elif (offset_c != 0 and 0 <= (offset_c + c) < len(self.puzzleArray[0])):
				slide_actions["slide(%d,%d,%d,%d)"%(c+offset_c, r+offset_r, c, r)] = self.slide(r+offset_r, c+offset_c, r, c)

	def get_all_actions(self):
		actions = {}
		self.get_rotates(actions)
		self.get_slides(actions)
		return actions

	def is_goal(self):
		for r in range(len(self.puzzleArray) - 1):
			for c in range(len(self.puzzleArray[0])):
				if self.puzzleArray[r][c] != " " and self.puzzleArray[r+1][c] != " " and self.puzzleArray[r][c] != self.puzzleArray[r + 1][c]:
					return False
		return True

	def execute(self, index):
		actions = self.get_all_actions()
		self.puzzleArray = actions[list(actions)[index]]

	def walk(self, index):
		past_set = set()
		while Puzzle.get_string(self.puzzleArray) not in past_set:
			past_set.add(Puzzle.get_string(self.puzzleArray))
			print(self)
			self.execute(index)
			

	def get_string(puzzleArr):
		return "|".join([ "".join(x) for x in puzzleArr])
	
	def __str__(self):
		return Puzzle.get_string(self.puzzleArray)

	def __eq__(self, puzzle):
		return Puzzle.get_string(self.puzzleArray) == Puzzle.get_string(puzzle.puzzleArray)

def process_args():

	if len(sys.argv) > 1:
		command = sys.argv[1]

		puzzleArg = sys.argv[2] if len(sys.argv) == 3 else "12345|1234 |12354"

		#setPuzzle(puzzleArg)

		puzzle = Puzzle(puzzleArg)

		if command == "print":
			print(puzzle)
		elif command == "goal":
			print(puzzle.is_goal())
		elif command == "actions":
			print("\n".join(puzzle.get_all_actions().keys()))
		elif command[0:4] == "walk":
			puzzle.walk(int(command[4:]))

if __name__ == "__main__":
	process_args()