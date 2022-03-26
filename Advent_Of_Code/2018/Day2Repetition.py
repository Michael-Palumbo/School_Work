f  = open("Day2List.txt").read().splitlines()


def Question1():
    twice = 0
    thrice = 0

    for line in f:
        time = []
        for i in line:
            time.append(line.count(i))
        if 2 in time:
            twice += 1
        if 3 in time:
            thrice += 1
    print(twice*thrice)

# def Question2():

    # constLength = len(f.readline())
    # #f.seek(0)
    #
    # for i in range(0,constLength):
    #     Map = {}
    #     for id in f:
    #         substring = id[0:i] + id[i+1: constLength]
    #         if id in Map:
    #             print(substring)
    #             return
    #         else:
    #             Map[substring] = id
    #     #f.seek(0)

def Kyle2():
    for s1 in f:
        for s2 in f:
            diff = 0
            for i in range(len(s1)-1):
                if s1[i] != s2[i]:
                    diff += 1;
            if diff == 1:
                print(s1 + " " + s2)





Kyle2()
