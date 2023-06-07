# Moles
## conversion from atoms to moles
import math
import csv
import pandas as pd
import numpy as np

#with open(r"C:\Users\jeric\Documents\School\Chemistry\Periodic Table of Elements.csv", "rt")as f:
class moles:
    
    f = pd.read_csv("Chemistry Notebook/Source/Periodic Table of Elements.csv")
    data = csv.reader(f)
    atomArray = []
    grams = 0.0
    mol = 0
    gramsInUse = 0
    coefficient = 0
    molecules = 0.0  # return answer: molecules
    atomicMassAns = 0.0  # Accumulated Atomic mass
    avogadrosNumber = 6.022*(pow(10, 23))  # Avogadros Number
    atomicmass = 0

    def __init__(self):
        self
        
    def input_Molecule(self, mol, gramsInUse, coefficient, elementArray):
        
        f = pd.read_csv("Chemistry Notebook/Source/Periodic Table of Elements.csv")
        #atomArray = []                          
        compound = " "
        i = 0
        grams = 0.0
        #gramsInUse = 0.0
        self.mol = mol
        self.gramsInUse = gramsInUse
        self.coefficient = coefficient
        self.elementArray = elementArray
        molecules = 0.0                                 #return answer: molecules
        atomicMassAns = 0.0                             #Accumulated Atomic mass
        avogadrosNumber = 6.022*(pow(10, 23))           #Avogadros Number
        atomicmass = 0
        #a = 0
        #b = 0
        for w in elementArray:
            w = w.title()
            doc = f.loc[f['Symbol'] == w]
            i = f.index[f["Symbol"] == w]
            el = float(f.AtomicMass[i])
            atomicMassAns += el
       

        #while compound != "=":
        #    compound = input("Enter Atoms one at a time, enter '=' to solve:\n")
        #    compound = compound.lower()
        #    f.seek(0) #returns the curser to the first line of the (f) document
        #    for a in data:
        #        for b in data:
        #            if compound.upper() == b[2].upper():
        #                atomicMass = float(b[3])
        #                atomicMassAns += atomicMass
        #                atomArray.append(str(b[2]) + ": " + str([b[3]]))
        #                print(atomArray) 
        #                print("Combined Atomic Mass: \t" + str(atomicMassAns) + "\n")
        #            #if compound.upper() != b[2].upper():
        #            #    print("No Match")
        print("\n")
        #Compound array
        print("Ionic compound:\t" + str(elementArray))
        #atomic mass
        print("Atomic Mass: " + str(atomicMassAns))
        #atomic mass with coefficients
        print("Coefficient:\t" + str(coefficient))
        massWithC = coefficient * atomicMassAns
        print("Atomic Mass with Coefficients:\t" + str(massWithC))
        #grams converted to mol
        if gramsInUse > 0:
            print("Grams of substance:\t" + str(gramsInUse))
            mol = gramsInUse / atomicMassAns
            print("Moles per grams:\t" + str(mol))
        #mol
        if mol > 0:
            print("Mol:\t " + str(mol))
        #grams per mole
            grams = atomicMassAns * mol
            print("Grams of substance:\t " + str(grams))
            #Number of molecules
            molecules = float(mol) * (float(avogadrosNumber))
            print("Molecules:\t" + str(molecules))
        

    ############################ convert #########################
    
    #Ionic Compunds With Polyatomic Ions dictionary
    #ions Dictionary
    ions_Dict = {"Charges" : {"-1" : {"Nitrite" : "NO2",
                                        "Nitrate" : "NO3-", 
                                        "Clorite" : "ClO2",
                                        "Clorate" : "Clo3",
                                        "Cyanide" : "CN-",
                                        "Hydroxide" : "OH-",
                                        "Hydrogen Carbonate" : "HCO3-"}
                                ,"+1" : {"Ammonium": "NH4+"}
                                ,"-2" : {"Sulfite": "SO3-2", 
                                        "Sulfate": "SO4-2", 
                                        "Carbonate": "CO3-2"}
                                ,"-3" : {"Phosphite": "PO3-3", 
                                        "phosphate": "PO4-3"}}}
    """
    print("\n")
    print(ions_Dict)
    print(ions_Dict.keys())
    print(ions_Dict.values())
    print(ions_Dict.get('Charges'))
    for m in ions_Dict.values():
        print(m)
    for m, n in ions_Dict.items():
        print(m, n)
    """
    #Enter mole
    #return molecules
    #################################### Conversions #####################################

"""
print("Convert atoms to moles\n")


#iterated a loop until user inputs correct number of moles and atoms          
while True:
    
    #The conversion process of molecules into atoms
    print("Conversion into molecules")
    
    #input: atoms, to the power of
    atoms, power = input("Enter Number of Atoms then enter power:\n"), input("Input Power:\n")
                    
    ############################ python conversion:
    #      atoms str to float
    #      power str to int
    try:
        atoms = float(atoms)
        power = int(power)
        False
    except:
        #cant be a string
        print("Must be a number")
        continue
    
    # if not type iteration
    if not type(atoms) is float and not type(power) is int:
        raise TypeError("only floats and ints are allowed")
    else:
        if atoms < 0 or power < 0:
            print("Number must be greater than 0")
            True


        ################################ Conversion Equation 
        if atoms > 0 and power > 0:
    
            atoms = atoms*pow(10, power)
            print("atoms:\t" + str(atoms))

            moles = 6.022*(pow(10, 23))
            print("moles:\t" + str(moles))

            v = atoms / moles
            
            print("answer:\t" + str(v))

            break



# class atoms(atom, number, mass):

# atoms.C = ["carbon", 6, 12]
"""


############################### Reactions ##################################
#The reaction between iron(II) oxide and carbon monoxide produces 
#iron and carbon dioxide. How many moles of iron can be obtained when
#4.75 mol FeO reacts with an excess of CO?
#FeO+CO⟶Fe+CO2

