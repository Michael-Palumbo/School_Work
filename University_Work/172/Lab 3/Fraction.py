class Fraction:
	#Constructor. Puts fraction in simplest form
	def __init__(self,a,b):
		self.num = a
		self.den = b
		self.simplify()
	#Print Fraction as a String
	def __str__(self):
		if self.den==1:
			return str(self.num)
		else:
			return str(self.num)+"/"+str(self.den)
	#Get the Numerator
	def getNum(self):
		return self.num
	#Get the Denominator
	def getDen(self):
		return self.den
	#Give Numerical Approximation of Fraction
	def approximate(self):
		return self.num/self.den
	#Simplify fraction
	def simplify(self):
		x = self.gcd(self.num,self.den)
		self.num = self.num // x
		self.den = self.den // x
	#Find the GCD of a and b
	def gcd(self,a,b):
		if b==0:
			return a
		else:
			return self.gcd(b,a % b)
	#Complete these methods in lab
	def __add__(self,other):
		new_num = (self.getNum()*other.getDen() + self.getDen()*other.getNum())
		new_den = (self.getDen() * other.getDen())
		return Fraction(new_num, new_den)
		
	def __sub__(self,other):
		new_other = Fraction(-other.getNum(), other.getDen())
		return self + new_other
		
	def __mul__(self,other):
		new_num = self.getNum() * other.getNum()
		new_den = self.getDen() * other.getDen()
		return Fraction(new_num, new_den)
		
	def __truediv__(self,other):
		new_num = self.getNum() * other.getDen()
		new_den = self.getDen() * other.getNum()
		return Fraction(new_num, new_den)
		
	def __pow__(self,exp):
		if exp == 0:
			return Fraction(1, 1)
			
		exp = -exp if exp < 0 else exp
		
		return self * self**(exp-1)