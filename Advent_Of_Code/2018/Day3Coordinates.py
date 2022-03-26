Matrix = [[0 for x in range(1000)] for y in range(1000)]

f = open("Day3Coordinates.txt").read().splitlines()

def Question1():
    numInter = 0

    for line in f:
        lineLength = len(line)
        loc = (line[line.index("@")+2 : line.index(":")].split(","))
        size = (line[line.index(":")+2 : lineLength].split("x"))
        for x in range(int(loc[0]), int(loc[0])+int(size[0])):
            for y in range(int(loc[1]), int(loc[1])+int(size[1])):
                Matrix[x][y] += 1

    for x in range(1000):
        for y in range(1000):
            numInter += 0 if Matrix[x][y] <=1 else 1 #print(Matrix[x][y],end="")

    print(numInter)

# line = f[27]
# constLength = len(line)
# loc1 = line[line.index("@")+2 : line.index(":")].split(",")
# size1 = line[line.index(":")+2 : constLength].split("x")
# print(loc1, size1)

def Question2():
    #PLZ FIX, REALLY BAD SOLUTION
    for line1 in f:
        #line1 = f[0]
        lineLength1 = len(line1)
        loc1 = list(map(int,line1[line1.index("@")+2 : line1.index(":")].split(",")))
        size1 = list(map(int,line1[line1.index(":")+2 : lineLength1].split("x")))
        Int = []
        for line2 in f:
            lineLength2 = len(line2)
            loc2 = list(map(int,line2[line2.index("@")+2 : line2.index(":")].split(",")))
            size2 = list(map(int,line2[line2.index(":")+2 : lineLength2].split("x")))

            overlayX = max( 0, min(loc1[0] + size1[0], loc2[0] + size2[0]) - max(loc1[0], loc2[0]) )
            overlayY = max( 0, min(loc1[1] + size1[1], loc2[1] + size2[1]) - max(loc1[1], loc2[1]) )
            if overlayX * overlayY > 0:
                #print(overlayX, overlayY, overlayX*overlayY)
                Int.append(line1)
        if len(Int) == 1:
            print(line1)
            return

Question2()

#Possible Speedy Way
#Arrange rectangles by start/end of x/y coordinate and use this to compute
# intersection area (p1) or check if any two intersect (p2) instead of filling a matrix/array
