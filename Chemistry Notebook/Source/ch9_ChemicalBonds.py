import csv
import pandas as pd 
import numpy as np
# Chapter 11

# non polar = x > 0.0 & x <= 0.4
# polar covalent = x > 0.5 & x < 1.7
# ionic = x > 1.8

### Examples
# Br - Br
# Na - Cl
# P - O
# Ni - Cl
# C - H
# Br - I

class chemicalBonds:
    
    periodicTable = pd.read_csv("Chemistry Notebook/Source/Periodic Table of Elements.csv")
    
    # x = 0 # table index
    # print(str(periodicTable.Element[x]) + " " + str(periodicTable.NumberofValence[x]))
    # print(periodicTable)
    # print(periodicTable.Element) prints element column

    # chemB = Element Symbol  Electronegativity  MeltingPoint  BoilingPoint  NumberofShells  NumberofValence
    chemB = pd.read_csv("Chemistry Notebook/Source/Periodic Table of Elements.csv", usecols = [1,2,17,20,21,26,27])
    
    #eNN = chemicalBonds.electronegativity(neg)
    #print(eNN)
    # look at regex (import regex as re) for finding wxact case of str and whatever else it does 
        

    def __init__(self):
        self
        # separate molecule (class molecule) unless array
        # lewis = lewisStructure(molecule) = method
        # combine lewis structures
        # determine electronegativity / polarity (maybe two separate methods) of certain bonds
        #   Lable direction of polarity
        # Determine Shapes and angle of a molecule
        # determine IMF's (intermolecular forces)
        # determine Boiling point
        # lable hydrogen bonding (H-N, H-O, H-F)

    # Lewis Structure: draw the dot structure of a molecule
    # input: array
    # output: the lewis structure
    # determine highest covalent bond
    # read from periodic table:
    #   electronegativity
    def lewisStructure(self, array):
        self.array = array
        # get valence electrons
        # draw the lewis structure of an atom
        # draw the lewis structure of a molecule



    # electronegativity: 
    # determine if -  ionic, covalent polar, covalent nonpolar
    # input: a covalent bond
    # output: type of electronegativity
    def electronegativity(self, bond):
        # Split into each bond
        chemB = pd.read_csv("Chemistry Notebook/Source/Periodic Table of Elements.csv",
                            usecols=[1, 2, 17, 20, 21, 26, 27])
        #self.bond = bond
        # self.molecule = molecule
        ionic = "ionic"
        slightlyPolar = "Slightly Polar"
        polarCovalent = "Polar Covalent"
        nonPolar = "Non Polar"
        
        w = ''
        doc = 0
        i = 0
        el = 0
        a = []
        eN = 0
        nP = 0                      # non-polar
        sP = 0.4                    # slightly polar
        pC = 1.9                    # polar covalent
        ion = 1.9 #< x              # ionic
        aa = 0
        for w in bond:
            w = w.title()
            doc = chemB.loc[chemB['Symbol'] == w]
            i = chemB.index[chemB["Symbol"] == w]  # index of element
            el = float(chemB.Electronegativity[i])
            a.append(el)
            print(doc)
            if el > aa:
                higherPolarity = str(chemB.Element[i])
            aa = el
        
        print("Higher Polarity pulls towards:\t" + higherPolarity)

        a.sort(reverse=True)

        if len(bond) > 1:
            eN = a[0]-a[1]
            eN = round(eN, 2)
            print("Electronegativity of Bond:\t" + str(eN))

        

         
        if eN == nP:
            #bond = nonPolar
            print(nonPolar)
        elif eN < sP:
            #bond = slightlyPolar
            print(slightlyPolar)
        elif eN < pC or eN >= nP:
            #bond = polarCovalent
            print(polarCovalent)
        else:
            #bond = ionic
            print(ionic)

        #for e in molecule:
        #    # define atoms electronegativity
        #    doc = chemB.loc[chemB['Symbol'] == (e)]
        #    i = chemB.index[chemB["Symbol"] == e]
        #    elecNeg = float(chemB.Electronegativity[i])
        #    print(elecNeg)
        

    # Bond Energies
    # breaking bonds (either exothermic or endothermic)
    # poitive or negative KJ
    # input: ?
    # output: energy 
    def bondEnergies(self):
        self

    # def ElectronNumbers
    # input: molecule
    # output:   how many shared electrons (bonding) (and pairs)
    #           how many unshared electrons (nonbonding) (and pairs) 
    #           total valence electrons
    def electronNumbers(self):
        (self)

# ......................CLASS COMMENTS
# and to add to hers, how do you figure out which way the arrow goes?
# can you use the  molecule shape simulation to be able to tell what the elements are?
# can you go slowly pls
# what's the role of the "C" in the middle there?
# sure.. you can recap the project ples
# how many slides you expect. etc..
# so. .no ppwerpoint?
# i sent you an article i was working on, so in addition to that.. add a website or video?
# what's not clear. is that. .are we bringing up one issue or multiple..?
# yes this morning
# the nicotine article
# yes you did.. it's unclear

