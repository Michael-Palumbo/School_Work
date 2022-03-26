class Question:
	def __init__(self, question, possible_answers, correct_answer):
		self.__question = question
		self.__possible_answers = possible_answers
		self.__correct_answer = correct_answer
	
	def __str__(self):
		out = self.__question +'\n'
		for i in range(0, len(self.__possible_answers)):
			out += str(i+1) +'. ' +self.__possible_answers[i] +'\n'
		return out
	
	def get_question(self):
		return self.__question
		
	def get_possible_answers(self):
		return self.__possible_answers
		
	def get_correct_answer(self):
		return self.__correct_answer
		
	def set_question(self, new_question):
		self.__question = new_question
		
	def set_possible_answers(self, new_possible_answers):
		self.__possible_answers = new_possible_answers
		
	def set_correct_answer(self, new_correct_answer):
		self.__correct_answer = new_correct_answer