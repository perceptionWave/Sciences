import numpy as np
import sympy as sp
from sympy import *
import matplotlib as mtp
import matplotlib.pyplot as plt
import pandas as pd
from pandas import *
from sympy.integrals.heurisch import components

class rules:

    def __init__(self):
        super().__init__()

    def ddxconst(self,c): return(0)
    def ddxRegularExp(self, x, n): return(n*x**(n-1))
    def ddxExp(self, x): return(diff(exp(x)))
    def constddxfunction(self, c, f): return(c*diff(f))
    def ddxfplusg(self, f, g):return(diff(f)+diff(g))
    def ddxfminusg(self, f, g):return(diff(f)-diff(g))
    def ddxftimesg(self, f, g):return(f*diff(g)+g*diff(f))
    def quotientRule(self, f, g): return((g*diff(f)-f*diff(g))/g**2)
