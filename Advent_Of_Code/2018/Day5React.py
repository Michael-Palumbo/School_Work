from string import ascii_lowercase
import re

f = open("Day5Letters.txt").read()
print(len(f))

# looping = bool(True)
# Fan = "dabAcCaCBAcCcaDA"
# while looping:
#     looping = bool(False)
#     for i in range(len(Fan)-1):
#         bit = Fan[i:i+2]
#         if len(bit) <= 1:
#             continue
#         bit = list(bit)
#         if(bit[0].lower() == bit[1].lower()):
#             if (bit[0].islower() and bit[1].isupper()) or (bit[1].islower() and bit[0].isupper()):
#                 Fan = Fan[:i] + Fan[i+2:]
#                 looping = bool(True)
# print(Fan)
def remove(text):
    looping = bool(True)

    while looping:
        looping = bool(False)
        for i in range(len(text)-1):
            bit = text[i:i+2]
            if len(bit) <= 1:
                break
            bit = list(bit)
            if(bit[0].lower() == bit[1].lower()):
                if (bit[0].islower() and bit[1].isupper()) or (bit[1].islower() and bit[0].isupper()):
                    text = text[:i] + text[i+2:]
                    looping = bool(True)
    return text


def removeLetter(text):
    #remove(text)
    replace_lowest = 60000
    replace_winner = ""
    for c in ascii_lowercase:
        new_text = re.sub("(?i)"+c,"", text) #'bye bye bye'
        #new_text = text.replace(c,"")
        reduced_text = remove(new_text)
        if len(reduced_text) < replace_lowest:
            replace_lowest = len(reduced_text)
            replace_winner = reduced_text
    return replace_winner

text = removeLetter(f)

print(len(text))
print(text)
