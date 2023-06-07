import math
import matplotlib as mtp
import matplotlib.pyplot as plt
import sympy as sy
import numpy as np
import pandas as pd
from sympy import *
from sympy.integrals.heurisch import components
# import calcRules
# from calcRules import rules as cr

x, y, z, u, t = symbols('x y z u t')
a, b, c, d = symbols('a b c d')
f, g, H = symbols('f g H', cls=Function)

'''Section 3.2'''
print('Section 3.2\n')

############################################## Question 4
print('Question 4')
print('Differentiate H(u) = (u - sqrt(u)) * (u + sqrt(u))')
def s32q4(u): return((u-sqrt(u))*(u+sqrt(u)))
s32q4_derivative = diff(s32q4(u),u)
print("H'(u) = " + str(s32q4_derivative))
s32q4_derivative = simplify(diff(s32q4(u),u))
print("H'(u) = " + str(s32q4_derivative))
print()

############################################### Question 11
print('Question 11')
print("Find the equations of the tangent lines to the curve y = (x-1)/(x+1)  || parallel to the line x - 2y = 2")
print("a(x) = (x-1)/(x+1)")
def s32q11(x): return((x-1)/(x+1))
def s32q11Der(x): return(2/((x + 1)**2))
def ptanq11(x): return((-x+2)/-2)

s32q11_derivative = simplify(diff(s32q11(x),x))
print("a'(x) = " + str(s32q11Der(x)))
m = frac(Rational(1/2))
print('m = ' + str(m))
print("a'(-3) = " + str(s32q11Der(-3)))
print("a'(1) = " + str(s32q11Der(1)))
print("a(-3) = " + str(s32q11(-3)))
print("a(1) = " + str(s32q11(1)))
print("a(0) = " + str(s32q11(0)))
#print("a(1) = " + str(s32q11(1)))
# y -y1 = 1/2(x-3)

q = solveset(Eq(s32q11Der(x), m), x)
print(q)
q = solve(s32q11Der(x)- m, x)
print(q)

def y1(x): return((1/2)*x-0.5)
def y2(x): return((1/2)*x+3.5)

d = limit(s32q11(x),x, -3)
d2 = limit(s32q11(x),x, 1)
print(d)
print(d2)
'''
# 2/(x+1)**2 = 2
j = np.linspace(-5,5, 500)
plt.title("Question 11")
plt.plot(j, s32q11(j), 'r', label='a(x)')
plt.plot(j, s32q11Der(j), 'b', label="a'(x)")
plt.plot(j, ptanq11(j), 'g', label='ptan')
plt.plot(j, y1(j), label='y1')
plt.plot(j, y2(j), label='y2')
#plt.plot()
plt.legend()
plt.grid()
plt.ylim(-5,5)
plt.ylabel('y')
plt.xlabel('x')
plt.show()
'''

################################################### Question 12

def R(p): return(p*f(p))

#################################################### Question 13
print('\nQuestion 13')
print("The curve y=x/(1 + x2) is called a serpentine. \nFind an equation of the tangent line to this curve at the point\n(2, 0.40).")
def s32q13(x): return(x/(1+x**2))

q = diff(s32q13(x),x)
print("f'(x) = " + str(q))

q = simplify(diff(s32q13(x),x))
print("f'(x) = " + str(q))

def derq13(x): return((1 - x**2)/(x**4 + 2*x**2 + 1))
m = derq13(2)
print("f'(2) = "+ str(m))

def q13tan(x): return(m*(x-2)+0.4)

print('Answer')
q = simplify(m*(x-2)+0.4)
print('y = ' + str(q))

'''
i = np.linspace(-2,6, 500)
plt.title('y=x/(1+x^2')
plt.plot(i, s32q13(i), 'r', label="f(x)")
plt.plot(i, derq13(i), 'blue', label="f'(x)")
plt.plot(i, q13tan(i), 'black', label='tan(2)')
plt.grid()
plt.legend()
plt.ylim(-1,1.2)
plt.show()
'''

########################################################### Question 14
print('\nQuestion 14')
print("If f(x) = x2/(1 + x), find f ''(2).")

def q14(x): return((x**2)/(1+x))

e = simplify(diff((q14(x),x, 2)))
print(e)

q = Derivative(((x**2)/(1+x)), x, x)
print(q)

def q14p2(x): return(0)

############################################################ Question 17

def g(t): return ( (t - sqrt(t)) / (t**(1/3)))
e = simplify(diff(g(t), t))
fraction(e)
print(e)

