import random
from random import uniform
import math

def dart():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    return x, y

def circle(x, y):
     if (x*x)+(y*y) <= 1:
         return True
     else:
         return False
    
def piAprox(throws):
    In = 0
    Out = 0
    for i in range(throws):
        x, y = dart()
        if circle(x, y):
            In += 1
        else:
            Out += 1
    print("pi =",4*(In/throws))

if __name__ == "__main__":
    piAprox(10000000)
