#!/usr/bin/env python3
#
# Michael Palumbo
#
# Create a file, one expression per line
#	 redirect from standard input:
#		test.py < input
#
# Notes:  We are not making our input bullet-proof.  If it looks like a #,
# then it is
#
#		Operands must be integers
#
#		The parser doesn't handle negative operands
#

from lexer import *

class Tree():
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right

class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

def print_post(tree):
	if tree == None:
		return ""
	s = print_post(tree.left)
	s += print_post(tree.right)
	return s + tree.data + " "

def print_pre(tree):
	if tree == None:
		return ""
	s = tree.data + " "
	s += print_pre(tree.left)
	s += print_pre(tree.right)
	return s

def print_in(tree):
	if tree == None:
		return ""
	s = print_in(tree.left)
	s += tree.data + " "
	s += print_in(tree.right)
	return s

def eval_tree(tree):
	if not str.isdigit(tree.data):
		return str(eval( eval_tree(tree.left) + str(tree.data) + eval_tree(tree.right) ))
	else:
		return str(tree.data)

if __name__ == "__main__":

	stack = Stack()

	while get_expression():
		t = get_next_token()
		while t:
			if str.isdigit( t[0] ) : # we have a (non-negative) number
				stack.push(Tree(t))
				#op = 'operand'
			else:
				#if t[0] == "-" or t[0] == "/" :
				#	left = stack.pop()
				#	right = stack.pop()
				#else:
				right = stack.pop()
				left = stack.pop()
				stack.push(Tree(t[0], left, right))
				#op = 'operator'
			#print( 'Got token: ' + t + ' (an ' + op + ')' )
			t = get_next_token()
		print("pre: " + print_pre(stack.peek()))
		print("in: " + print_in(stack.peek()))
		print("post: " + print_post(stack.peek()))
		print("eval: " + eval_tree(stack.pop()))
		

