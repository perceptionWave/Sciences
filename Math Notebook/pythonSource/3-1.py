import matplotlib as mtp
import matplotlib.pyplot as plt
import sympy as sy
import numpy as np
import pandas as pd
from sympy import *
from sympy.integrals.heurisch import components

# Section 3.1
print('Section 3.1')

# Differentiate the function.
print('Question 6')
def s31q6(x): return(sy.exp(x+8)+7)


print(diff(s31q6(x), x))

#Find an equation of the tangent line to the curve at the given point.
print('Question 7')
def s31q7(x): return(3*x**3-x*2 + 3)


sy.Point(1, 5)
yD = diff(s31q7(x), x)
print("y' = " + str(yD))
# m = 9-2
y = 7*(x-1) + 5
print('y = ' + str(y))

print('Question 8')


def s31q8(x):
    y = x**4+4*sy.exp(x)
    y = diff(y, x)
    print(y)

    #return(y)
s31q8(x)


def derivative(y, x):
    y = diff(y, x)
    print(y)


def slope(y):
    pass


print('Question 8: Using derivative function')
P = sy.Point(0, 4)
y = x**4+4*sy.exp(x)
derivative(y, x)
xk = 0
y = xk**4+4*sy.exp(xk)
# Y' at (x = 0)
print("slope = " + str(y))
# slope of the normal line is the negative reciprocal of the slope of y'
nrec = -1/y
print("normal slope = " + str(nrec))
l = nrec*x - 4
print(l)

print("3.1: Question 9")
y = sy.sqrt(x)+(3*sy.sqrt(x))
yP = derivative(y, x)
print("y' = " + str(yP))
#yPP = derivative(yP, x)
#print('y" = ' + str(yPP))


def s(t): return(80*t-16*t**2)
def sP(t): return(80-32*t)


for t in range(11):
    print(str(t) + "\t:  " + str(s(t)) + " \t:  m='" + str(sP(t)))

print('s(2.5) = ' + str(s(2.5)))

print('test Question 3')
y = sy.ln(x)/x
yP = diff(y, x)
print(yP)


def f(x): return(sy.ln(x)/x)


print(diff(f(x), x))
def fP(x): return(-log(x)/x**2 + x**(-2))


print(fP(1))


y = 36*t-16*t**2

