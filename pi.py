import random
from random import uniform
import math
from math import pi

def dart():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    return x, y

def stickfrac(y):
    #y = random.uniform(0, 1)
    return math.sqrt(1-y**2)*4

def circle(x, y):
     if (x*x)+(y*y) <= 1:
         return True
     else:
         return False
def f(x):
    return(1-x**2)**0.5
    
def dartPiAprox(throws):
    In = 0
    Out = 0
    for i in range(throws):
        x, y = dart()
        if circle(x, y):
            In += 1
        else:
            Out += 1
    print("pi =",4*(In/throws))

def piAprox(slices):
    s = 0
    for i in range(slices):
        s += (f(i/slices) + f((i+1)/(slices)))/(2*slices)
    dif =  math.pi - s*4
    print("pi aproximation=",s*4, "real pi =", math.pi, "difference = ",dif, "accurate up to", int(math.log10(dif))*(-1), "digits")

def stickPiAprox(throws):
    s = 0
    for i in range(throws):
        s+=stickfrac(i/throws)
    print("pi aproximation=",s/throws, "real pi =", math.pi, "difference =", s/throws - math.pi)

if __name__ == "__main__":
    piAprox(100000000)
