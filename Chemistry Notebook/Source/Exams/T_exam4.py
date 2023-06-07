from ch1_Conversions import conversions
from ch3_Molecule import molecule
from ch3_BalancingChemicalEquations import balancingChemicalEquations
from ch4_Moles import moles
from ch9_ChemicalBonds import chemicalBonds
from ch10_SolidsAndLiquids import solidsAndLiquids
from ch11_Solutions import solutions
from ch12_ArrheniusAcidsAndBases import arrheniusAcidsAndBases

import pandas as pd
import numpy as np
import matplotlib as mtb

f = pd.read_csv("Chemistry Notebook/Source/Periodic Table of Elements.csv")


mol = 0
grams = 0
coefficient = 0
moleSolute = 0
leterSolute = 0
massSolute = 0
molarity = 0
compound = ""
compoundList = []
eN = 0
millileter = "mL"
leter = "L"

molesObj = moles()
balanceObj = balancingChemicalEquations()
moleculeObj = molecule()
solutionsObj = solutions()
bondObj = chemicalBonds()
conversionObj = conversions()

# Question 2
compoundList = "CaCl2"
mP = 35.5
totalMass = 750.9
massSolute = 0
massSolute = solutionsObj.massPercent(massSolute, totalMass, mP)
print(massSolute)
massSolvent = solutionsObj.massSolvent(massSolute, totalMass)
print(massSolvent)
print("..................................................")
ans = 750.9 * 0.355
print(ans)
ans = 100 -35.5
print(ans)
ans = totalMass * 0.645
print(ans)

# question 4
compound = "OO"
compoundList = moleculeObj.splitMolecule(compound)
eN = bondObj.electronegativity(compoundList)
print(eN)
compound = "CsBr"
compoundList = moleculeObj.splitMolecule(compound)
eN = bondObj.electronegativity(compoundList)
print(eN)
compound = "NF"
compoundList = moleculeObj.splitMolecule(compound)
eN = bondObj.electronegativity(compoundList)
print(eN)
compound = "NaF"
compoundList = moleculeObj.splitMolecule(compound)
eN = bondObj.electronegativity(compoundList)
print(eN)
compound = "SF"
compoundList = moleculeObj.splitMolecule(compound)
eN = bondObj.electronegativity(compoundList)
print(eN)
compound = "FF"
compoundList = moleculeObj.splitMolecule(compound)
eN = bondObj.electronegativity(compoundList)
print(eN)

# 8
compound = "CH"
compoundList = moleculeObj.splitMolecule(compound)
eN = bondObj.electronegativity(compoundList)
print(eN)

# 15
compound = "NaOH"
compoundList = moleculeObj.splitMolecule(compound)
moleSolute = 0
M = 0.300
ml = 252.0
g = 0 
c = 1
l = conversionObj.convert(ml, millileter, leter)
massSolute = solutionsObj.molarity(moleSolute, l, M)
massSolute = molesObj.input_Molecule(massSolute, g, c, compoundList)
print(compound)
print(massSolute)



