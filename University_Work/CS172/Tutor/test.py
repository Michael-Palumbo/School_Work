
def toLower(string11):
    s=""
    for i in range(len(string11)):
        if string11[i] >= "A" and string11[i] <= "Z":
            temp = ord(string11[i])
            temp = temp+(ord("a")-ord("A"))
            s+= chr(temp)
        else:
            s+=string11[i]
    return s
if __name__=="__main__":
    print(toLower("PhiLaDELpHia"))
