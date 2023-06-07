import matplotlib as mtp
import matplotlib.pyplot as plt
import sympy as sy
import numpy as np
import pandas as pd
from sympy import *
from sympy.integrals.heurisch import components

print("Section 2.2")
def lim(theta): return(sy.sin(5*theta)/sy.tan(4*theta))


limitt = [0.1, 0.01, 0.001, 0.0001, -0.0001, -0.001, -0.01, -0.1]

for theta in limitt:
    print(str(theta) + ":\t" + str(lim(theta)))
