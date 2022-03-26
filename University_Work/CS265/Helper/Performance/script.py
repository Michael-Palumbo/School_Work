import math

# (n, t)
nt = {
1000:   3410305,
10000:  45669600,
20000:  98213010,
30000:  153718561,
40000:  209910393,
50000:  264587515,
60000:  321936947,
70000:  377492624,
80000:  429764872 
}

# Jawn content
jc = ''

for n in nt.keys():
	jc += str(n) +'  ' +str(nt[n]) +'  '
	jc += str((nt[n]/(n**3))) +'  '
	jc += str((nt[n]/(n**2))) +'  '
	jc += str((nt[n]/(n*math.log(n, 10)))) +'  '
	jc += str((nt[n]/(math.log(n, 10)))) +'  '
	jc += '\n'

f = open('jawn.txt', 'w')
f.write(jc)
f.close()