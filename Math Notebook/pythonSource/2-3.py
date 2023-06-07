import matplotlib as mtp
import matplotlib.pyplot as plt
import sympy as sy
import numpy as np
import pandas as pd
from sympy import *
from sympy.integrals.heurisch import components

print('Section 2.3')

print('Question 6')
r = 0
h = [1, 0.1, 0.001, 0.0001, -1, -0.01, -0.001, -0.0001]
def s2_3q6(h): return((sy.sqrt(81+h)-9)/h)


print(sy.limit((sy.sqrt(81+r)-9)/r, r, 0))
for x in h:
    print(s2_3q6(x))
# question ?
#h = sy.Symbol('h')
#u = (sy.sqrt(9+h)-3) / h
#u = ((sy.sqrt(9+h)-3) / h) * ((sy.sqrt(9+h)+3)/(sy.sqrt(9+h)+3))
#u = h / h (sy.sqrt(9+h)+3)
u = 1 / (sy.sqrt(9)+3)
print(u)

print('Question 7')
x = sy.Symbol('x')
e = x**2*sy.cos(15*sy.pi*x)
s2_3q7 = sy.limit(e, x, 0, dir='+-')
print(s2_3q7)


def q12(f): return (x**2-7*x+6)
#f = np.linspace(0,10, 100)
#plt.plot(f, q12(f))
#plt.show()
