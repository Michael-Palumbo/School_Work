from spellchecker import spellchecker

def get_file():
    good = False
    while not good:
        file_name = input("Enter the name of the file to read:\n")
        try:
            f = open(file_name)
            good = True
        except:
            print("Could not open file.")
    lines = f.readlines()
    # words = [line for line in lines]
    print(lines)
    sc = spellchecker(f)
    print(sc)
    
          
print("Welcome to Text File Spellchecker!")
get_file()

    
            
        
        