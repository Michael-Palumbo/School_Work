from Birthday import Birthday

hashtable = []

for i in range(12):
    hashtable.append([])
	
f = open('bdaylist.txt')
text = f.readlines()

for line in text:
	vals = line.split('/')
	b = Birthday(int(vals[1]), int(vals[0]), int(vals[2]))
	hashtable[hash(b)].append(b)

for i in range(12):
		print('Hash location', i, 'has', len(hashtable[i]), 'elements in it')