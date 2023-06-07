import matplotlib as mtp
import matplotlib.pyplot as plt
import sympy as sy
import numpy as np
import pandas as pd
from sympy import *
from sympy.integrals.heurisch import components

print('Section 2.6')
print('Question 6')
s26q6 = sy.limit(sy.sqrt(36*(x**2)+x)-6*x, x, 0)
print(s26q6)


s26q14 = sy.sqrt(((x**2)+x+4)+x)
