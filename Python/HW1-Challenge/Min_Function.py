import sys
import math
input = sys.stdin.readline

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def givenFunction(a, x):
    return ((x**2)/math.log(x) + (a*x))


def getMinimumFunctionValue(a, high, low):
    phi = (math.sqrt(5)-1)/2
    
    diff = high - low 

    x1 = high - phi*(diff)
    x2 = low + phi*(diff)

    f1 = givenFunction(a, x1)
    f2 = givenFunction(a, x2)

    while diff>1e-10:
        diff = high - low 
        if f1<f2:
            high = x2 
            x2 = x1 
            f2 = f1 
            diff = high-low 
            x1 = high - phi*(diff)
            f1 = givenFunction(a, x1)

        else:
            low = x1 
            x1 = x2
            f1 = f2 
            diff = high - low 
            x2 = low + phi*(diff)
            f2 = givenFunction(a, x2)

    return (f1+f2)/2

if __name__ == '__main__':
    a = float(input())
    low = 1.0
    high = 2.0
    print(getMinimumFunctionValue(a, high, low))
