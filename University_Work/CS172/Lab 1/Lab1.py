from spellchecker import *

def get_file():
    while True:
        try:
            name = input("Enter the name of the file to read:\n")
            file = open(name,"r")
            return file
        except:
            print("Could not open file.")

if __name__ == "__main__":
    f = get_file()
    SP = spellchecker("english_words.txt")
    print(SP)
    total, wrong, right = 0,0,0
    for index, line in enumerate(f):
        for word in line.split():
            if( word.isspace()):
                continue
            total += 1
            if(not SP.check(word)):
                print("Possible Spelling Error on line %d: %s"%(index+1,word))
                wrong += 1
            else:
                right += 1
    print("%d words passed spell checker."%right)
    print("%d word failed spell checker."%wrong)
    print("%.2f%% of the words passed."%(right/total*100))
