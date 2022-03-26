import math

# (n, t)
nt = {
10000:  921.0,
20000:  1827.0,
30000:  2950.0,
40000:  3786.0,
50000:  5338.0,
60000:  6945.0,
70000:  7347.0,
80000:  8581.0, 
90000:  9478.0, 
100000: 10059.0, 
}

# Jawn content
jc = ''

for n in nt.keys():
	jc += str(n) +'\t' +str(nt[n]) +'\t'
	jc += str(nt[n]/n) +'\t'
	jc += str((nt[n]/(n**3))) +'\t'
	jc += str((nt[n]/(n**2))) +'\t'
	jc += str((nt[n]/(n*math.log(n, 10)))) +'\t'
	jc += str((nt[n]/(math.log(n, 10)))) +'\t'
	jc += '\n'

f = open('jawn.txt', 'w')
f.write(jc)
f.close()
