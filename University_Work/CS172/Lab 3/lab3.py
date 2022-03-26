from Fraction import *

def harmonic_series(num):
    total = Fraction(0,1)
    for k in range(1, num+1):
        total += Fraction(1, k)

    return total

def two_series(num):
    total = Fraction(0,1)
    for k in range(num+1):
        total += Fraction(1, 2)**k

    return total

def zero_series(num):
    return Fraction(2,1) - two_series(num)

def partial_riemann_zeta(num,b):
    total = Fraction(0,1)
    for k in range(1,num+1):
        total += Fraction(1,k)**b

    return total

def get_valid_input():
    try:
        return int(input("Enter Number of Iterations (integer>0):\n"))
    except:
        return get_valid_input()


def print_jawn(temp_s, num,val):
    print("%s(%s) = %s"%(temp_s, str(num), val))
    print("%s(%s) ~= %s"%(temp_s, str(num), val.approximate()))

if __name__ == "__main__":
    print("Welcome to Fun with Fractions!")
    inp = get_valid_input()
    print_jawn("H",inp,harmonic_series(inp))

    print_jawn("T", inp, two_series(inp))

    print_jawn("Z", inp, zero_series(inp))

    for b in range(2, inp-1):
        print_jawn("R", str(inp)+","+str(b), partial_riemann_zeta(inp,b))
