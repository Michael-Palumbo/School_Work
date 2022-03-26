class Question():
    # Constructor
    def __init__(self, the_question, q1, q2, q3, q4, answer):
        self.__the_question = the_question
        self.__options = [q1,q2,q3,q4]
        self.__answer = answer

    # Getters
    def get_answers(self):
        return self.__answer

    def get_options(self):
        return self.__options

    def get_the_question(self):
        return self.__the_question

    # Setters
    def set_the_question(self, the_question):
        self.__the_question = the_question

    def set_options(self, options):
        self.__options = options

    def set_answer(self, answer):
        self.__answer = answer

    # Overloading the str()
    def __str__(self):
        # everything will be summed up in s
        s = self.__the_question + "\n"
        for index in range(len(self.__options)):
            s += "\t{}: {}\n".format( index+1, self.__options[index] )

        return s
