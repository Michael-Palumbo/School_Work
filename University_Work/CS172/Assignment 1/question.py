class Question:
    # Constructor
    def __init__(self, prompt, choices, answer):
        self.__prompt = prompt
        self.__choices = choices
        self.__answer = answer

    # Overirde string casting
    def __str__(self):
        s = self.__prompt + "\n"
        for letter, choice in enumerate(self.__choices, start = ord('A')):
           s += "    %c: %s\n" %( letter, choice )
        # I'm proud of my ord('A'), so i'm keeping it
        return s

    #Getters
    def getAnswers(self):
        return self.__answer

    def getChoices(self):
        return self.__choices

    def getPrompt(self):
        return self.__prompt

    #Setters
    def setQuestion(self, prompt,choices, answer):
        self.__prompt = prompt
        self.__choices = choices
        self.__answer = answer

    def setPrompt(self, prompt):
        self.__prompt = prompt

    def setChoices(self, choices):
        self.__choices = choices

    def setAnswer(self, answer):
        self.__answer = answer
