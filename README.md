num=int(input("YOUR NUMBER : "))
def factorial(n):
    if n>=2:
        return n*(factorial(n-1))
    else:
        return 1
print("FACTORIAL IS : ",(factorial(num)))


from math import log
from math import sin
from math import sqrt
num=float(input("ENTER YOUR NUMBER : "))
def square(n):
    print("SQUARE ROOT IS : ",(sqrt(n)))
def loga(m):
    print("NATURAL LOGARITHM IS : ",(log(m)))
def sine(o):
    print("SINE IS : ",(sin(o)))
a=square(num)
b=loga(num)
c=sine(num)
