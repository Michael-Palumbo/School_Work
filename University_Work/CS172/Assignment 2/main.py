from Media import *
from Movie import *
from Song import *
from Picture import *

#<======================== LIST OF MEDIA ========================>
List_of_Media = []
List_of_Media.append(Movie("movie", "Bad Movie", "2", "Some Director", "2:30"))
List_of_Media.append(Song("song","Some Song","3","Dude From Seven Eleven","Seven Eleven Songs"))
List_of_Media.append(Picture("picture", "Cool Picture","5","1040"))
List_of_Media.append(Movie("movie", "Good Movie", "3", "Some Other Director", "3:00"))
List_of_Media.append(Song("song","Some Other Song","3","Some Artist","No one heard of the album"))
List_of_Media.append(Picture("picture", "Bad Picture","1","1040"))
List_of_Media.append(Movie("movie", "Terrible Movie", "1", "Never Heard of Director", "4:20"))
List_of_Media.append(Song("song","Terrible Song","1","Bad Artist","Terrible Album"))
List_of_Media.append(Picture("picture","Decent Picture","4","1040"))
List_of_Media.append(Movie("movie", "Decent Movie", "4", "Emmy Award Winning Director", "1:50"))
List_of_Media.append(Song("song","Decent Song","4","Carly, just Carly","Decent Album"))
List_of_Media.append(Movie("movie", "Amazing Movie", "5", "Struggling Director", "1:59"))

#<======================== TEXT PARSER ========================>
def parseInput(inp):
    # Takes input, seperate it into command and contents
    try:
        # Fetch First Word
        command = inp.split()[0]
        try:
            # Get the remaining words after the first
            contents = inp[inp.index(' ')+1:]
            return command, contents
        except:
            return command, ""

    except KeyboardInterrupt:
        exit()
    except:
        return "",""

#<======================== HELP COMMANDS ========================>
def help():
    # List of possible commands
    print("============================================")
    print("Available Commands:")
    print(">> display all\n   --> display everything")
    print(">> display [media type]\n   --> displays everything in the type [movie, song, picture]")
    print(">> play [item]\n   --> play a movie or song")
    print(">> show [item]\n   --> show a picture")
    print(">> quit\n   --> quit program")
    print(">> help\n   --> reprint this jawn")
    print("============================================")
    print()

#<======================== MAIN CODE ========================>
if __name__ == "__main__":
    print("Welcome to Your Playlist")
    help()

    #<========== MAIN LOOP ==========>
    while True:
        inp = input("What is your choice: ")
        command, contents = parseInput(inp)

        #<========== DISPLAY ==========>
        if command == "display":
            if contents == "all":
                for current_media in List_of_Media:
                    print("============================================")
                    print(current_media)

            # Check if it's a possible type
            elif contents == "movie" or contents == "song" or contents == "picture":
                for current_media in List_of_Media:
                    if current_media.getType() == contents:
                        print("============================================")
                        print(current_media)
            else:
                print("Cannot Determine Type \""+contents+"\"\nTry \"movie\" \"song\" or \"picture\"")

        #<========== PLAY ==========>
        elif command == "play":

            for s in List_of_Media:
                # Picture does not have a play method, so filter them out
                if s.getType() != "picture":
                    if contents == s.getName() :
                        s.play()
                        break
            else:
                print("Cannot Play \""+contents+"\"")

        #<========== SHOW ==========>
        elif command == "show":

            for s in List_of_Media:
                # Only picture has a show method
                if s.getType() == "picture":
                    if contents == s.getName():
                        s.show()
                        break
            else:
                print("Unknown Name: \""+contents+"\"")

        #<========== HELP ==========>
        elif command == "help":
            help()

        #<========== QUIT ==========>
        elif command == "quit":
            break

        #<========== ELSE ==========>
        else:
            print("Cannot do command \""+command+"\"")
