from Stack import Stack
import sys

equations = []

def main():
	f = open('input.txt', 'r')
	for line in f.readlines():
		if line == 'exit':
			sys.exit(0)
		else:
			print(line.strip(), '=', post_fix(line))
		
	
			
def post_fix(eq):
	eq = eq.strip()
	eq = eq.split(' ')
	
	stack = Stack()
	for op in eq:
		if op in ['+','-','*','/']:
			num1 = stack.pop()
			num2 = stack.pop()
			if op == '+':
				stack.push(num1+num2)
			elif op == '-':
				stack.push(num2-num1)
			elif op == '/':
				stack.push(num2/num1)
			elif op == '*':
				stack.push(num1*num2)
		else:
			stack.push(int(op))	
	return stack.pop()
	

main()