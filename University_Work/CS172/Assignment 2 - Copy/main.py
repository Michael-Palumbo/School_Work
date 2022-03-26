#Mert Candan mc3943
#Create a playlist that accepts input and takes actions

from Media import *
from Movie import *
from Song import *
from Picture import *
import sys

List_of_Media = []
List_of_Media.append(Movie("movie", "Lady and the Trap", "3", "Nuna Business", "1:40"))
List_of_Media.append(Song("song","Calculus Rhapsody","2","WordGospel09","Calculicious"))
List_of_Media.append(Picture("picture", "Cat","5","960"))
List_of_Media.append(Movie("movie", "Lord of the Bling", "4", "Peter Jackson", "1:40"))
List_of_Media.append(Song("song","The Nut Cracker","4","E. T. A. Hoffmann","Tchaikovsky' Nutcracker"))
List_of_Media.append(Picture("picture", "Dog House","4","960"))
List_of_Media.append(Movie("movie", "Shrek 5, It's all Orger Now", "5", "Vicky Jenson", "2:00"))
List_of_Media.append(Song("song","All about the Treble","3","Megan Trainer","Intruments Series"))
List_of_Media.append(Picture("picture","Mona Minion","4","960"))
List_of_Media.append(Movie("movie", "Teeth", "3", "Steven Spielberg", "2:10"))
List_of_Media.append(Song("song","Monday","4","Rebecca Black","Days of the Week"))
List_of_Media.append(Movie("movie", "Star Shrek", "4", "J.J. Abrams", "2:10"))


def printf(media):
    println()
    print(media)

def println():
    print("-----------------------------------------")

def filterOutPrint(keyword, array):
    for a in array:
        if a.getType() == keyword:
            printf(a)

# Take's the user input, seperates them into the command portion and the parameters of the command
def seperateInput(inp):
    try:
        command = inp[:inp.index(' ')]
        parameters = inp[inp.index(' ')+1:]
        return command, parameters

    # If the user does ctrl+C to exit
    except KeyboardInterrupt:
        sys.exit(1)
    except:

        #We couldn't find a space
        return inp, None

# Display Possible Commands
def help():
    print("The following are acceptable commands")
    print("display [*, movie, song, picture]\n->\tdisplays the details of elements of said types, * means all")
    print("play [movie_name, song_name]\n->\tplays the movie or song")
    print("show [picture_name]\n->\tshows the picture")
    print("help\n->\tDisplays this message again")
    print("exit\n->\tLeaves the program")
if __name__ == "__main__":
    print("Welcome To Your Player")
    println()
    help()

    while True:

        command, parameters = seperateInput(input("\nPlease enter a valid command: ").strip())

        #<======== DISPLAY ========>
        if command == "display":

            # For each to display all contents in the list
            if parameters == "*":
                for current_media in List_of_Media:
                    printf(current_media)

            # Parameters are either movie, song, picture
            elif parameters == "movie" or parameters == "song" or parameters == "picture":
                filterOutPrint(parameters, List_of_Media)

            else:
                print("Invalid Name")

        #<======== PLAY ========>
        elif command == "play":

            # Search for the correct name, also check to see if it's a movie or song, since picture doesn't have play
            for s in List_of_Media:
                if parameters == s.getName() and (s.getType() == "movie" or s.getType() == "song"):
                    s.play()
                    break
            else:
                print("Invalid Name")

        #<======== SHOW ========>
        elif command == "show":
            for s in List_of_Media:
                if parameters == s.getName() and s.getType() == "picture":
                    s.show()
                    break
            else:
                print("Invalid Name")

        #<======== HELP ========>
        elif command == "help":
            help()

        #<======== QUIT ========>
        elif command == "quit":
            break

        else:
            print("Unrecognized Command")
