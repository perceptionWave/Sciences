import math
import numpy as np
import sympy as sy
#from sympy import *
from sympy.integrals.heurisch import components

def f(x): 
    y = sy.sqrt(x-5)
    return(y)

x = np.array([5.5, 5.9, 5.99, 5.999, 6.5, 6.1, 6.01, 6.001])

pX = 6
pY = 1
qX = x
qY = f(x)

def slope(y): 
    m = ((qY - pY) / (qX - pX))
    return(m)
    
for a in x:
    print(slope(x))