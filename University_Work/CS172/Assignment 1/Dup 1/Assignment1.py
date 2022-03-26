import sys
from question import Question

questions = [   # List of Question Objects
                Question("What is the capital of the UK",                                    "London", "Washington", "Paris", "Brussles",        0),
                Question("What is the sixth letter of the alphabet",                         "A", "C", "F", "E" ,                                3),
                Question("What is the name given to a baby dog?",                            "Socks", "Puppy", "Boi", "Sandal",                  1),
                Question("What is 2 x 14",                                                   "7", "14", "21", "28",                              3),
                Question("What is the third planet from the sun?",                           "Earth", "Neptune", "Venus", "Mars",                0),
                Question("How many years are in a century?",                                 "1", "5", "10", "100",                              3),
                Question("What does the K in KFC stand for?",                                "Kansas", "Klutteny", "Kentucky", "Kindergartener", 2),
                Question("What fruit is also the name of a company that makes smartphones?", "Orange", "Pear", "Lemon", "Apple",                 3),
                Question("Henry VIII had how many wives?",                                   "1", "0", "10", "6",                                3),
                Question("How many Toy Story films have there been so far?",                 "None", "3", "1", "Not Enough",                     1),
            ]

players = [0,0] # Index 0 is player 1, Index 1 is player 2

# Display the Points of Play 1 and 2
def display_total_points():
    print("And the final scores are:")
    print("Player 1: {}".format(players[0]))
    print("Player 2: {}".format(players[1]))

    # Decide who won
    if players[0] == players[1]:
        print("Player 1 and 2 have tied with {} points(s)".format(players[0]))
    elif players[0] > players[1]:
        print("Player 1 wins!")
    else:
        print("Player 2 Wins!")

# Retrieves a valid input, between 1 and 4
def get_users_input():
    while True:
        try:
            ans = int(input("Enter your answer: "))
            if 0 < ans < 5:
                return ans - 1
        # They excited the program with ctrl+c
        except KeyboardInterrupt as e:
            print("\nGood-Bye")
            sys.exit(1)
        except:
            pass
        # They gave bad input
        print("Error: your answer has to be a value between 1 and 4. Try again.")

# Checks to see if user's guess
def quess_the_question(player_index, answer, question):
        if answer == question.get_answers():
            print("Excellent! You score!\n")
            players[player_index] += 1
        else:
            print("That is incorrect. Better luck with the next question.\n")

# Start Here
if __name__ == "__main__":
    print("Welcome to the python intro programming quiz\n" + "-"*50 + "\n")
    # Loop through the questions
    for index in range(len(questions)):
        # Print who's turn it is, it corresponds to turn
        print("Player {} here is your question:".format(index%2 + 1))
        # Print Contents of Question List
        print("{}: {}".format(index+1 , str(questions[index])))

        # Get User Input, Then Ask the Question
        users_input = get_users_input()
        quess_the_question(index%2, users_input, questions[index])

    display_total_points()
