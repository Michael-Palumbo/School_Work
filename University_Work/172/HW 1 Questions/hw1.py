from Question import Question
from random import shuffle

#Used to determine if a user's input is valid (an int and between 1 and 4 inclusive)
def validate_input(inp):
	try:
		if int(inp) < 1 or int(inp) > 4:
			return False
		else:
			return True
	except:
		return False

#Used to created the questions in the game		
def init_questions():
	questions = []
	
	questions.append(Question('What year was Drexel founded?', ['1891', '1890', '1892', '1893'], 0))
	questions.append(Question('What is the name of the Drexel Dragon?', ['Mark', 'Mario', 'Jason', 'Balthuszar'], 1))
	questions.append(Question('What are the Drexel colors?', ['Blue and black', 'Gold and yellow', 'Blue and Gold', 'Fire Red and Leaf Green'], 2))
	questions.append(Question('Who founded Drexel?', ['AB Drexel', 'DJ Drexel', 'JA Drexel', 'AJ Drexel'], 3))
	questions.append(Question('What is the oldest building on campus?', ['Main', 'Hans', 'Nesbit', 'Myers Hal'], 0))
	questions.append(Question('Which of these is not a dorm hall?', ['Myers', 'Summit', 'Race', 'Van R'], 1))
	questions.append(Question('How large is the bio wall?', ['60ft', '70ft', '80ft', '90ft'], 2))
	questions.append(Question('what is the name of Drexel\'s college of business?', ['LaBua', 'Labeouf', 'DAC', 'LeBow'], 3))
	questions.append(Question('Which of these is not an academic building?', ['Hans', 'Nesbit', 'Drexel One', 'Academic Building'], 0))
	questions.append(Question('Which of these universities is next to Drexel?', ['Pennstate', 'U Penn', 'Rutgers', 'Berkley'], 1))
	
	#Randomly shuffles questions list
	shuffle(questions)
	return questions

#Main script function
def main():
	#Variable set-up
	questions = init_questions()
	p1_points = 0
	p2_points = 0
	turn = 1
	
	#Intro
	print('Welcome to the Python intro programming quiz')
	print('--------------------------------------------')
	
	#Loops through questions by popping one off while there are still questions in the list
	while len(questions) > 0:
		print('Player', turn, 'here is your question:')
		
		current_questions = questions.pop(0)
		print(str(current_questions))
		
		#Getting and validating user input
		inp = input('Enter your answer:\n')
		while not validate_input(inp):
			print('Error: The entry must be a number between 1 and 4 (inclusive)')
			inp = input('Enter your answer:\n')
			
		#Determining if user answer is correct and adjusting score accordingly
		if int(inp)-1 == current_questions.get_correct_answer():
			print('Correct! You get a point.\n')
			if turn == 1:
				p1_points += 1
			else:
				p2_points += 1
		else:
			print('Wrong! Better luck next time.\n')
			
		#Toggle the turn
		turn = 1 if turn == 2 else 2
	
	#Final print outs, score printing, and determining winner/tie
	print('And the final scores are:')
	print('Player 1:', p1_points)
	print('Player 2:', p2_points)
	if p1_points == p2_points:
		print('It was a tie!')
	else:
		print('Player', ('1' if p1_points > p2_points else '2') , 'wins!')
		
#run main script function
main()