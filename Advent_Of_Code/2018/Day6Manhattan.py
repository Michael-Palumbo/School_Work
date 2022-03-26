f = open("Day6Manhattan.txt").read().splitlines()

BigArray = [x.split(", ") for x in f]
print(BigArray[1])
#array of array of array; whoops

# dic = []
#
# for y in BigArray:
#     dic[int(y[0]),int(y[1])]

#[print(y,x) for y,x in dic.items()]

def Find_Man(loc1,loc2):
    min = (abs(int(loc1[0]) - int(loc2[0])) + (abs(int(loc1[1]) - int(loc2[1]))))
    #print(loc2,min)
    return min

def find_man_winner(loc1):
    min = 10000
    winner = None
    multi = bool(False)
    for key in BigArray:
        loc_min = Find_Man(loc1,key)
        if loc_min < min:
            multi = bool(False)
            min = loc_min
            winner = key
        elif loc_min == min:
            multi = bool(True)
    return winner #if multi else [0,0]

map = [[0  for x in range(400)] for y in range(400)]

for x in range(400):
    for y in range(400):
        map[x][y] = find_man_winner([x,y])

# print(map[0].count(BigArray[]))

print("LOOK HERE")

keys_to_skip = []
for x in range(400):
    look = map[0][x]
    look2 = map[399][x]
    look3 = map[x][0]
    look4 = map[x][399]
    if look not in keys_to_skip:
        keys_to_skip.append(look)
    if look2 not in keys_to_skip:
        keys_to_skip.append(look2)
    if look3 not in keys_to_skip:
        keys_to_skip.append(look3)
    if look4 not in keys_to_skip:
        keys_to_skip.append(look4)

print("Length of keys to leave out", len(keys_to_skip))

for key in BigArray:
    if key not in keys_to_skip:
        print(key, sum([x.count(key) for x in map]) )
