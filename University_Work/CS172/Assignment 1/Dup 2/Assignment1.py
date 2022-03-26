from question import Question

player_list = [0,0] #Players

question_list = [
                    Question("What country is Rome located in?",
                                ["France","Italy","Jamaica","Spain"] , 1),
                    Question("Which of these famous film/book trilogies is Gollum a part of?",
                                ["Harry Potter","The Chronicles of Narnia","The Lord of the Rings","Eragon"] , 2),
                    Question("What color is a dandelion before its flowers turn to pollen?",
                                ["Blue","Purple","Yellow","White"] , 2),
                    Question("George Harrison was member of which famous band?",
                                ["The Rolling Stones","Led Zeppelin","The Beatles","Pink Floyd"] , 2),
                    Question("What's the capital of the United States",
                                ["New York City, New York","Philadelphia, Pennsylvania","Los Angeles, California","Washington, D.C."] , 3),
                    Question("In geometry, what do you call a shape with 5 sides?",
                                ["Sphere","Pentagon","Square","Hexagon"] , 1),
                    Question("Will Smith is the prince of which neighborhood?",
                                ["Hollywood","Encino","Northridge","Bel Air"] , 3),
                    Question("What's the longest running cartoon series on TV?",
                                ["Family Guy","The Simpsons","South Park","Rick & Morty"] , 1),
                    Question("Which country is Big Ben located in?",
                                ["Finland","Germany","England","France"] , 2),
                    Question("What does the 'C' in CIA stand for?",
                                ["Central","Communal","Communicative","Chain"] , 0),
                ]

def show_point(): #Display the Point
    print("And the final scores are:")
    print("Player 1 Point(s):",player_list[0])
    print("Player 2 Point(s):",player_list[1])

    if player_list[0] == player_list[1]:
        print("Tie! Players Tied with", player_list[0], "points(s)")
    else:
        print("Player", player_list[0] if player_list[0] > player_list[1] else player_list[1], "wins!" )

def quess_question(answer, question, index): #Using input, find out if player wins
        if answer == question.get_answers():
            player_list[index] += 1
            print("Excellent! You score!\n")
            return
        print("That is incorrect. Better luck with the next question.\n")

def get_input(): #retrieves valid input
    try:
        ans = int(input("Enter your answer:"))
        if ans in [1,2,3,4]:
            return ans - 1
        int("g")
    except:
        print("Error: your answer has to be a value between 1 and 4. Try again.")
        return get_input()

#Start of the code
print("Welcome to the python intro programming quiz")
print("-"*50)
i = 0
#For each though each questions
for current_question in question_list:
    #Print who's turn it is
    print("Player",i%2+1 , "here is your question:")
    #Print current_question, calling str()
    print(i+1, ": ", str(current_question), sep= "")
    quess_question(get_input() ,current_question, i%2)
    i += 1

show_point()
