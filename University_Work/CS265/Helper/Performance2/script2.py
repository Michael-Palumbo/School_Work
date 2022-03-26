import math

# (n, t)
nt = {
10000:  45669600,
20000:  98213010,
30000:  153718561,
40000:  209910393,
50000:  264587515,
60000:  321936947,
70000:  377492624,
80000:  429764872,
90000:  507689137, 
100000: 571776534, 
}

# Jawn content
jc = ''

for n in nt.keys():
	jc += str(n) +'\t' +str(nt[n]) +'\t'	
	jc += str((nt[n]/float(n))) +'\t'
	jc += str((nt[n]/float((n**3)))) +'\t'
	jc += str((nt[n]/float(n**2))) +'\t'
	jc += str((nt[n]/(n*math.log(n, 10)))) +'\t'
	jc += str((nt[n]/(math.log(n, 10)))) +'\t'
	jc += '\n'

f = open('jawn.txt', 'w')
f.write(jc)
f.close()
