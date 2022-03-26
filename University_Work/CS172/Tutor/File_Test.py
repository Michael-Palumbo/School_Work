# import os
#
# f = open("Plan.txt","r")
#
# print(f.readline())
# f.seek(4,os.SEEK_SET)
# print(f.readline())
#
#
#
# f.close()

def toLower(string):
    new_string = ""
    for i in string:
        if "A" <= i <= "Z":
            new_string += chr( ord(i) + ( ord("a") - ord("A") ) )
        else:
            new_string += i
    return new_string

def my_enumerate(lis):
    new_lis = []
    i = 0
    for val in lis:
        new_lis.append((i,val))
        i += 1
    return new_lis

# temp = ["my","dog","is","fat"]
# print(my_enumerate(temp))
# for i, val in my_enumerate(temp):
#     print(i,val)

print(toLower("meM e  ABC S"))
