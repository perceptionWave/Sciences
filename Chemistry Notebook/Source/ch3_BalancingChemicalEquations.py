import math
import csv
import numpy as np
import pandas as pd
from collections import Counter
from ch3_Molecule import molecule


   
class balancingChemicalEquations:
    
    f = pd.read_csv("Chemistry Notebook/Source/Periodic Table of Elements.csv")

    #def __init__(self):
    #    self

        ################################# Equation ###################
    def equation(self, w_equation):
        #input equation
        #w_equation = input("Enter the equation:\t")
        #delimit by "+, -, /, *, ="
        m = molecule()
        self.w_equation = w_equation
        z = 0
        p = 0
        indexarray = []
        xarray = []
        w_equation = w_equation.replace(" ", "")
        w_equation = w_equation.rsplit("=")
        for x in w_equation:
            x = x.rsplit("+")
            indexarray.append(x)
            for y in x:
                z = 0
                for yy in y:
                    z += 1
                    if yy.isupper():
                        lastUpperIndex = z - 1
                        xarray.append(yy)
                    if yy.islower():
                        yyy = y[lastUpperIndex:z]
                        xarray.pop()
                        xarray.append(yyy)
                    if yy.isdigit():
                        digit = int(yy) -1
                        l = len(xarray) - 1
                        a = xarray[l]
                        for n in range(digit):
                            xarray.append(a)
                    if yy == "+":
                        w_equation.extend(xarray)
        for w in indexarray:
            for z in w:
                docMoc = m.splitMolecule(z)
                indexarray[w][z] = docMoc

        w_equation = xarray.copy()
        xarray.clear()
        print(w_equation)
        #counters 
        r = Counter(w_equation)
        w = Counter
        print(indexarray)
        print(r)
        #print(atom_dict)
        #counter.elements() will print sequentially all the elements that have been countered
        #count.most_common() gives you most common
        
    #def splitMolecule(self, molecule):
    #    atomArray = []
    #    z = 0
    #    for x in molecule:
    #        z += 1
    #        if x.isupper():
    #            lastUpperIndex = z - 1
    #            atomArray.append(x)
    #        if x.islower():
    #            yyy = molecule[lastUpperIndex:z]
    #            atomArray.pop()
    #            atomArray.append(yyy)
    #        if x.isdigit():
    #            digit = int(x) -1
    #            l = len(atomArray) - 1
    #            a = atomArray[l]
    #            for n in range(digit):
    #                atomArray.append(a)
    #    return(atomArray)
        
        #nametuple
        # from collections import namedtuple
        # a = namedtuple('name', 'course')
        # t = a("name", "Chem")             or
        # t = a.make(['name', 'chem']) #### for lists 
        #output: (name = "name", course = "chem")
 
