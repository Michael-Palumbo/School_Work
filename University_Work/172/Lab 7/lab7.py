from Maze import Maze
from room import Room
'''
=======SOLUTION=======
east, east, east, south, south, south

-or-

south, south, south, east, east, east
=======SOLUTION=======
'''
def maze_init():
	my_rooms = []
	my_rooms.append(Room("This room is the entrance."))
	words = ['fish', 'blue', 'green', 'kitchen', 'apple', 'dog', 'room', 'maze', 'python', 'not exit']
	for i in range(0, 10):
		my_rooms.append(Room("This is the " +words[i] +' room.'))
	
	my_rooms.append(Room("This room is the exit. Good Job."))
		
	#Make a maze!
	#Set the start and exit rooms.
	my_rooms[0].setEast(my_rooms[1])
	my_rooms[1].setEast(my_rooms[2])
	my_rooms[2].setEast(my_rooms[3])
	my_rooms[3].setSouth(my_rooms[4])
	my_rooms[4].setSouth(my_rooms[5])
	my_rooms[5].setSouth(my_rooms[11])	
	
	my_rooms[0].setSouth(my_rooms[6])
	my_rooms[6].setSouth(my_rooms[7])
	my_rooms[7].setSouth(my_rooms[8])
	my_rooms[8].setEast(my_rooms[9])
	my_rooms[9].setEast(my_rooms[10])
	my_rooms[10].setEast(my_rooms[11])
	
	my_maze = Maze(my_rooms[0], my_rooms[11])
	return my_maze

def main():
	maze = maze_init()
	while not maze.atExit():
		inp = input('Enter a direction to go:\n')
		if inp not in ['north', 'south', 'east', 'west', 'restart']:
			print('You must choose', ['north', 'south', 'east', 'west', 'restart'])
		else:
			if inp == 'north':	
				if maze.moveNorth():
					print('You go north')
					print(maze.getCurrent())
				else:
					print('The north direction blocked.')
			if inp == 'south':
				if maze.moveSouth():
					print('You go south')
					print(maze.getCurrent())
				else:
					print('The south direction blocked.')
			if inp == 'east':
				if maze.moveEast():
					print('You go east')
					print(maze.getCurrent())
				else:
					print('The east direction blocked.')
			if inp == 'west':
				if maze.moveWest():
					print('You go west')
					print(maze.getCurrent())
				else:
					print('The west direction blocked.')
			if inp == 'restart':
				maze.reset()
				print('You go back to the first room')
				print(maze.getCurrent())
			
	print('You made to the exit!')

main()
