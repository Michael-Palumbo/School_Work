class Question:
    def __init__(self, question, choices, answer): #Initially called when made
        self.__question = question
        self.__choices = choices
        self.__answer = answer

    def __str__(self): #automatically called with str()
        s = self.__question + "\n"
        index = 0
        for choice in self.__choices:
           s += "    " + str(index+1) + ": " + choice + "\n"
           index += 1
        return s

    #Getters
    def get_answers(self):
        return self.__answer

    def get_choices(self):
        return self.__choices

    def get_question(self):
        return self.__question

    #Setters
    def set_question(self, question):
        self.__question = question

    def set_choices(self, choices):
        self.__choices = choices

    def set_answer(self, answer):
        self.__answer = answer
