import pandas as pd
import numpy as np
import matplotlib as mtb

#

class solutions:

    M = "molarity"

    moleSolute = "moles of solute"
    leterSolution = "Leters of Solution"

    moleSolute = 0.400
    leterSolution = 1.70
    M = moleSolute / leterSolution
    #print(M)
    M = 0
    # M = molarity(moleSolute, leterSolution, M)
    # print(M)


    Mp = "Mass Percent"
    massSolute = "mass of solute (g)"
    massSolvent = "mass of the solvent (g)"

    massSolute = 15.0
    massSolvent = 235
    # learn how to round to sig figs use round(x, 2)

    Mp = (massSolute / (massSolute + massSolvent)) * 100
    #print(Mp)

    massSample = "Mass of Sample"
    ppm = "parts per million"
    ppb = "parts per billion"

    # ppm = (massSolute / massSample) * 1000000
    # ppb = (massSolute / massSample) * 1000000000

    volumePercent = "volume percentage"
    volumeSolute = "volume of solute"
    volumeSample = "Volume of Sample"

    # volumePercent = (volumeSolute / volumeSample) * 100

    Eq = "Equivalent is the amount of that ion equal..."

    def __init__(self):
        self
        #self.moleSolute = 0.0
        #self.leterSolution = 0.0
        #self.molarity = 0.0
        #self.mS = 0.0
        #self.mSo = 0.0
        #self.overallMass = 0.0
        #self.Mp = 0.0
        #self.volumeSolute = 0.0
        #self.volumeSample = 0.0

    # molarity
    # calculate the molarity 
    # input:    moleSolute
    #           leterSolution
    #           molarity
    # output: one of the above
    def molarity(self, nSolute, lSolution, M):
        if nSolute > 0:
            self.moleSolute = nSolute
        else:
            nSolute = M * lSolution
            self.moleSolute = nSolute
            return(self.moleSolute)
        if lSolution > 0:
            self.leterSolution = lSolution
        else:
            lSolution = nSolute / M
            self.leterSolution = lSolution
            return(self.leterSolution)
        if M > 0:
            self.molarity = M
        else:
            M = nSolute / lSolution
            self.molarity = M
            molarity = M
            return(molarity)

    # massPercent
    # calculate the mass percent using the mass of the salute divided by the overall mass
    # input:    massSolute
    #           massSolvent
    # output:   massPercent
    def massPercent(self, massSolute, overallMass, Mp):
        if massSolute > 0:
            self.massSolute = massSolute
        else:
            massSolute = overallMass * (Mp / 100)
            return(massSolute)
        if overallMass > 0:
            self.overallMass = overallMass
        else:
            overallMass = massSolute + massSolvent
            return(overallMass)
        if Mp > 0:
            self.Mp = Mp
        else:
            Mp = (massSolute / overallMass) * 100
            Mp = round(Mp, 2)
            return(Mp)
    
    #massSolvent
    # input:    massSolute
    #           overall mass
    # output: massSolvent
    def massSolvent(self, massSolute, overallMass):
        self.massSolvent = overallMass - massSolute
        massSolvent = overallMass - massSolute
        return(massSolvent)
    
    # volumePercent
    # calculate the volume percent from volume sample and volume solute
    # input:    volumeSample
    #           volumeSolute
    #           ?volumePercent
    # output:   volumePercent
    def volumePercent(self, volumeSolute, volumeSample):
        self.volumeSolute = volumeSolute
        self.volumeSample = volumeSample
        volumePercent = (volumeSolute / volumeSample) * 100
        round(volumePercent,2)
        return(volumePercent)
