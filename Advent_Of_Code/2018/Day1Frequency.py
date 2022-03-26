f = open("Day1List.txt","r")
total = {0}
totalnum = 0
def secondQ():
    global totalnum
    for x in range(0,200):
        for i in f:
            totalnum += int(i)
            if totalnum in total:
                print(totalnum)
                print(x)
                return;
            total.append(totalnum);
        f.seek(0);

def firstQ():
    global totalnum
    for i in f:
        totalnum += int(i)
    print(totalnum);

"""
if the device displays frequency changes of +1, -2, +3, +1,
 then starting from a frequency of zero, the following changes
 would occur:

Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
In this example, the resulting frequency is 3.
"""

def secondQ2():
    global totalnum
    for x in range(0,200): #Kind of bad, loops about 140 times
        for i in f:
            totalnum += int(i)
            if totalnum in total:
                print(totalnum)
                print(x)
                return;
            total.add(totalnum);
        f.seek(0);

"""
You notice that the device repeats the same frequency change
list over and over. To calibrate the device, you need to find
the first frequency it reaches twice.
"""

secondQ2();

f.close();
