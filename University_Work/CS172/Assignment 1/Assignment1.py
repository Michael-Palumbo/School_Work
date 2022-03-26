from question import Question

list_of_questions = [ #List of question objects, these are the questions we will see during the trivia
                        Question("How many calories do you burn banging your head against the wall?",
                                    ["100","150","200","250"] ,
                                        1),
                        Question("What country is it illegal to own just one guinea pig?",
                                    ["Switzerland","Finland","Poland","Merica"] ,
                                        0),
                        Question("Which reptile can detect earthquakes 75 miles away (5 days before it arrives)?",
                                    ["Lizard","Turtle","Snake","Crocidile"] ,
                                        2),
                        Question("A flock of crows is known as a _______.",
                                    ["Shoe","Murder","Sandal","Black Cloud"] ,
                                        1),
                        Question('When is "Put a pillow on your fridge day"?',
                                    ["May 29th","November 4th","December 1st","January 4th"] ,
                                        0),
                        Question("Percent of Americans that believe chocolate milk, comes from brown cows?",
                                    [".01%","1%","7%","15%"] ,
                                        2),
                        Question("Which animal pees on it's head to attract females?",
                                    ["Billy Goats","Lions","Mountain Goats","Cats"] ,
                                        0),
                        Question("During your life time, how much saliva do you produce?",
                                    ["Half a Swimming Pool","A Swimming Pool","2 Swimming Pools","5 Swimming Pools"] ,
                                        2),
                        Question("Polar bears could eat how many penguins in one sitting?",
                                    ["28","86","143","355"] ,
                                        1),
                        Question("King Henry VIII always slept with what leathal weapon?",
                                    ["Gigantic Axe","Mace","Crossbow","2 Handed Broad Sword"] ,
                                        0),
                    ]

class Player: #Mostly created just so I can pass by reference
    def __init__(self):
        self.points = 0
    def reward(self):
        self.points += 1
    def getPoints(self):
        return self.points

def getValidInput(): #Retrieves an input
    while True:
        ans = input("What is your answer?\n")

        if ans in ["1","2","3","4"]:
            return int(ans) - 1 #we already know it's an int, and we compare index between 0-3
        elif ans.lower() in ["a","b","c","d"]:
            return ord(ans.lower()) - ord('a')

        print("Invalid, please pick a letter between (A-D) or (1-4)")
# Get players input, reward them if they succeed
def quessQuestion(player, question):
        ans = getValidInput()
        # Might be poor design having getValidInput() here, but I feel like i can argue that it makes sense
        if ans == question.getAnswers():
            print("Correct!\n")
            player.reward()
        else:
            print("That is not correct D:\n")

def displayPoints():
    print("The Final Scores Are...")
    print("Player 1 Point(s): %d" %player1.getPoints())
    print("Player 2 Point(s): %d" %player2.getPoints())
    # Prints out the player's points, and then decides the winner
    if(player1.getPoints() == player2.getPoints()):
        print("Tie, Both Players have %d Point()s"%player1.getPoints())
    else:
        print("Player %d wins!"%(1 if player1.getPoints() > player2.getPoints() else 2))
        #Print who won, using an in line if statement (ternary operator)


# "Main" Function, where we start
if __name__ == "__main__":
    print("Welcome to the python intro programming quiz")
    print("-"*50)
    #Create 2 Players
    player1 = Player()
    player2 = Player()
    # Loop through questions while also unpacking index
    for i, currentQuestion in enumerate(list_of_questions):
        # Print the player, print the contents of question, and make a guess
        print("Player %d here is your question:"%(i%2+1))
        print("%d: %s\n"%(i+1 , currentQuestion))
        quessQuestion( player1 if (i%2 == 0) else player2 ,currentQuestion)
        # My "ternary operator" does make it less flexable to control which player goes
    displayPoints()

    #print("Done")
