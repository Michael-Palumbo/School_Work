from Fraction import Fraction

def H(n):
	result = Fraction(1,1)
	for k in range(2, n+1):
		result += Fraction(1, k)
	return result
		
def T(n):
	result = Fraction(1, 2) ** 0 
	for k in range(1, n+1):
		result += Fraction(1, 2) ** k 
	return result
		
def Z(n):
	return Fraction(2, 1) - T(n)

def R(n, b):
	result = Fraction(1, 1) ** b
	for k in range(2, n+1):
		result += Fraction(1, k) ** b
	return result

def validate_input(inp):
	try:
		if int(inp) <= 0:
			return False
		else:
			return True
	except:
		return False
	
def main():
	print("Welcome to Fun with Fraction")
	inp = input('Enter number of iterations(integer > 0):\n')
	while not validate_input(inp):
		inp = input('Enter number of iterations(integer > 0):\n')
	inp = int(inp)
	bs = [2, 3, 4, 5, 6, 7, 8]
	print('H(' +str(inp) +')=' +str(H(inp)))
	print('H(' +str(inp) +')~=' +str(H(inp).approximate()))
	
	print('T(' +str(inp) +')=' +str(T(inp)))
	print('T(' +str(inp) +')~=' +str(T(inp).approximate()))
	
	print('Z(' +str(inp) +')=' +str(Z(inp)))
	print('Z(' +str(inp) +')~=' +str(Z(inp).approximate()))
	
	for b in bs:
		print('R(' +str(inp) +',' +str(b) +')=' +str(R(inp, b)))
		print('R(' +str(inp) +',' +str(b) +')~=' +str(R(inp, b).approximate()))	
	
main()