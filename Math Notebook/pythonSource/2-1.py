import math
import matplotlib as mtp
import matplotlib.pyplot as plt
import sympy as sy
import numpy as np
import pandas as pd
from sympy import *
from sympy.integrals.heurisch import components


print("2.1 - Limits and Derivatives")
#Question 1
print("#1")
x = [2.9,2.99,2.999,2.9999,3.0001,3.001,3.01,3.1]
for e in x:
    y = (2/(2-e))
    y = round(y, 4)
    print(str(e) + ":\t" + str(y))

#Question 2
print("#2")
t = 2
def v(t):
    y=(36*t)-(16*(t**2)) 
    return(y)

avgVel = [0.5,0.1,0.05,0.01]
for e in avgVel:
    que = t+e
    ans = v(que)
    ans = round(ans,6)
    print(str(que) + ":\t" + str(ans))

q2 = v(t)
print(q2)

#Question 3
print("#3")
def s(t): 
    s = 5 * sy.sin(sy.pi*t) + 3* sy.cos(sy.pi* t)
    return(s)
t = np.array([[1,2],[1,1.1],[1,1.01],[1,1.001]])
for e in t:
    que = e[1]-e[0]
    ans = s(que)
    print(ans)

#Question 4
print("#4")
def f(x): 
    y = sy.sqrt(x-2)
    return(y)
sy.Point(3,1)
q = np.array([2.5,2.9,2.99,2.999,3.5,3.1,3.01,3.001])
for x in q:
    y = f(x)
    y = round(y,6)
    print(y)
#x = np.linspace(0,5,100)
#plt.plot(x, f(x))
#plt.xlabel("X")
#plt.ylabel("Y")
#plt.xticks([0,4],['0','4'])
#plt.show()

# question 5
print("#5")
def q5(x):
    #x = sy.Symbol("x")
    y = 5*(x**2)
    return(y)




