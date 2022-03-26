from stack import *

equations = {
    "+": lambda x,y: x+y,
    "*": lambda x,y: x*y,
    "-": lambda x,y: y-x,
    "/": lambda x,y: y/x,
}

stack = Stack()

def post_fix(line):
    for digit in line.strip().split(' '):
        if digit in equations.keys():
            stack.push( equations[digit]( stack.pop(), stack.pop() ) )
        else:
            stack.push(int(digit))

    return stack.pop()

if __name__ == "__main__":
    print("Welcome to Postfix Calculator")
    while True:
        line = input("Enter Expression\n")
        if line == 'exit': break
        print(f"{line}\nResult: {post_fix(line)}")
