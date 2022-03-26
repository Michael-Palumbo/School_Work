def checkId(guard):
    if messages[1] in idMap:
        print(messages[1], "is in idMap")
    else:
        idMap[messages[1]] = {}

def checkTime(guard, time):
    #print(guard, time)
    if time in idMap[guard]:
        idMap[guard][time] += 1
    else:
        idMap[guard][time] = 0

def countTime(guard, start, end):
    for t in range(start, end):
        checkTime(guard,t)

def getTotal(schedule):
    #this is a dict
    total = 0

    for key,value in schedule.items():
        total += int(value)
    #print(total)
    return total

def getHighest(schedule):
    max = 0
    for key,value in schedule.items():
        if  int(value) > max:
            max = int(value)
    return max

def findPop():
    max = 0
    winnerId = ""
    for key,value in idMap.items():
        temp_max = getHighest(value)#getTotal(value)
        if temp_max > max:
            max = temp_max
            winnerId = key
    print(winnerId, max)
    return winnerId

f = open("Day4GuardTime.txt").read().splitlines()
f.sort()
#print(f)

idMap = {}

#test = f[0:8]

lastGuard = ""
startTime = 0
endTime = 0
for line in f:
    messageTime = line[line.index("]")-2:line.index("]")]
    #print(messageTime)

    message = line[line.index("]")+2:len(line)]
    #print(message)


    messages = message.split(" ")
    if "Guard" in line:
        lastGuard = messages[1]
        checkId(lastGuard)
    elif "falls" in line:
        startTime = messageTime
    elif "wakes" in line:
        endTime = messageTime
        countTime(lastGuard, int(startTime), int(endTime))

print("REACHED")
winner = findPop()
print(winner, idMap[winner])

#print(idMap)
