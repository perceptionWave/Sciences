import math
import pandas as pd
import numpy as np

# Change this to Jupyter Notebook
class energy:

    def __init__(self):
        (self)
        

    ################### Chapter 7: Energy and Chemistry ####################

    ############################ 7.1 : Energy ##############################

    potentialEnergy = "potential energy: energy due to position or stored in chemicals"
    energy = "Energy: the ability to do work"
    kineticEnergy = "Kenetic energy: energy of motion"

    one_calorie_cal = "Calorie: the energy needed to heat 1 g of water 1oC"
    k_cal = "Kilocalorie: 1 kcal = 1000 cal"

    # Calories in food are determined by placing a 
    # sample in a calorimeter, burning the food, and determining 
    # the amount of heat released.

    ##################### Law of Conservation of Energy #################

    #               a.k.a. The First Law of Thermodynamics
    #               The energy of the universe is constant.
    #               Energy cannot be created or destroyed, but 
    #          it can be exchanged between objects and change forms.
    #              You can’t win, you can only break even.
    #               There’s no such thing as a free lunch.

    ######################## 7.2 Work and Energy ##########################
    # Energy is the ability to do work. Think about it: when you have a lot of energy, you can do a lot of work; but if you’re low on energy, 
    # you don’t want to do much work. Work (w) itself is defined as a force (F) operating over a distance (Δx):
    # w = F × Δx
    # In SI, force has units of newtons (N), while distance has units of meters. Therefore, 
    # work has units of N·m. This compound unit is redefined as a joule (J):
    # 1 joule = 1 newton·meter
    # 1 J = 1 N·m
    work = "a force operating over a distance"
    heat = "The transfer of thermal energy from one body to another due to difference in temperature"
    cal = 4.184 #J
    def energy_definitions(self):
        print(potentialEnergy)
        print(energy)
        print(kineticEnergy)
        print(one_calorie_cal)
        print(k_cal)
        print(work)
        print(heat)

    #Joules are usually preferred by scientists.
    #4.184 Joule(J) = 1 cal
    #1000 J = 1 kJ

    energy_dict = {"J": 4.18, "cal": 1, "kcal": 1000}
    
    def joule_cal_conversions(self, num, x_fro, x_to):
        if num > 0:
            num = num
        else:
            print("Num must be greater than 0\n")
        x_to = x_to
        x_fro = x_fro
        for k in energy_dict:
            if x_to == energy[k]:
                x_to == energy[k]
            else:
                print("'to' Conversion unit can't be matched\n")
            if x_fro == energy[k]:
                x_fro == energy[k]
            else:
                print("'fro' Conversion unit can't be matched\n")
        try:        
            ans = num * x_fro / x_to
        except:
            raise TypeError
        finally:
            ans = -1
        return(ans)

    # constants and variables
    Specific_Heat = "mC(Delta)T or q = m * C * (Tf - Ti)"
    q = "q = Joules or Calories"
    m = "m = Mass or weight"
    C = "C = specific heat temp of element (J/gC)"
    Tf = "Tf = Final Temperature"
    Ti = "Ti = Initial Temperature"

    def energy_constants_definitions(self):
        print(Specific_Heat)
        print(q)
        print(m)
        print(C)
        print(Tf)
        print(Ti)

    #substances and their specific heat
    specificHeat_dict = {
        "water" : 4.184,
        "iron" : 0.449,
        "gold" : 0.129,
        "mercury" : 0.139,
        "aluminum" : 0.900,
        "ethyl_alcohol" : 2.419,
        "magnesium" : 1.03,
        "helium" : 5.171,
        "oxygen" : 0.918,
        "lead" : 0.128,
        "silver": 0.235,
        "copper": 0.385,
        }
    #the amount of heat required to increase the temperature of 1 g of a substance by 1'C
    def specificHeat_substance(self, compound):
        compound = compound
        for k in specificHeat_dict:
            if compound == specificHeat_dict[k]:
                compound = specificHeat_dict[k] #check for key or item definition
            else:
                print("Compound or element can't be found\n")
        return(compound)

    def specifiedQ(self, q, m, c, Ti, Tf):
        if m > 0:
            m = m
        else:
            delta_t = Tf - Ti
            m = q / (c * delta_t)
            return(m)
        if c > 0:
            c = c
        else:
            delta_t = Tf - Ti
            print(delta_t)
            c = q / (m * delta_t)
            return(c)
        if Ti > 0:
            Ti = Ti
        else:
            Ti = (q / (m * c)) - Tf
            return(Ti)
        if Tf > 0:
            Tf = Tf
        else:
            Tf = (q / (c * m)) + Ti
            return(Tf)
        if q > 0:
            q = q
        else:
            delta_t = Tf - Ti
            q = m * c * delta_t
            return(q)
    """
    ########### Example 1
    question_One = "Ethanol has a specific heat of 2.46 J/g◦C. When 655 J are added to a sample of ethanol, \nits temperature increases from 18.2°C to 32.8°C. How many grams of ethanol are in the sample?"

    # 655J = m * 2.46 J/gC * (32.8'c - 18.2'c)
    # 655J = m * 2.46 J/gC * (14.6'c)
    # 655J = m * (35.916 J/g)
    # (655J / 35.916J) * 1g = 18.2369974384675 g


        
    q = 655                 # Jouls
    C = 2.46                # Ethenols specific heat (Jouls / gram'Celcius)
    Tf = 32.8               # temp final
    Ti = 18.2               # temp initial
    m = q / (C * (Tf - Ti)) # Solving for Mass

    print(question_One)
    print("Example 1\t m = " + str(m) + "\n")

    ########### Example 2
    question_Two = "If 9.2 kJ of heat are absorbed by 55g of water at 25C, \nwhat will be the final temperature of the water?"

    C = 4.18                # Joules per gramCelcius 
                            # constant per calorie specific to water
    m = 55                  # grams of H2O
    Ti = 25                 # degrees celcius
    kj = 9.2                # kilo jouls = q 
    q = 9200                # Kilo jouls turned joules 
    Tf = q / (C*m) + Ti     # solving for Temp final

    print(question_Two)
    print("Example 2:\t Tf = " + str(Tf) + "\n")

    #9200 = 55 * 4.18 (Tf - 25)

    ########### Example 3 - How to find the specific substance
    question_Three = "What is the specific heat of a metal if 24.8 g of the metal absorbs \n65.7 cal of energy and the temperature rises from 20.2'C to 24.5'C?"

    m = 24.8                # mass of (specific) metal
    q = 65.7                # cal of energy
    Ti = 20.2               # Temp initial
    Tf = 24.5               # Temp final
    C = (m * (Tf-Ti)) / q   # Solving for Specified heat

    print(question_Three)
    print("Example 3:\t C = " + str(C) + "\n")


    ########### Example 4
    question_Four = "If 361 J of heat are added to 35g piece of iroon at 21C, \nwhat is the new temperature? C for iron = 0.449 J/gC"

    q = 361                 # Joules of heat
    m = 35                  # gram piece of iron
    C = 0.449               # J/gC = Fe : Specified heat of iron 
    Ti = 21                 # Temp Initial
    Tf = (q / (m*C)) + Ti   # Solving for Temp Final

    print(question_Four)
    print("Example 4:\t Tf = " + str(Tf) + "\n") 
    """


    ################## 7.3 Enthalpy and Chemical Reactions #################

    # Enthalpy (H) is a form of energy.  It is 
    # not measured directly, but we will look at changes of 
    # enthalpy during reactions.
    # Change in enthalpy, also known as change in heat is written as: DH
    # (DH = Delta H)  = (Tf - Ti)
    # DH is equal to heat(q) for a process at constant pressure

    # If DH < 0 (is negative), the process is exothermic
    # If DH > 0 (is positive), the process is endothermic

    # ############################# Exothermic ###############################
    
    # https://youtu.be/cylIGRfhJQU - burning car

    # Fe2O3 + 2 Al → 2Fe + Al2O3
    # DH = -2044 kJ

    # DH is (-)
    exothermic = "Exothermic: Change in heat is (-) negative"
    # reaction (system) loses energy
    exothermic_System = "Exothermic system: Loses energy"
    # solution (surroundings) gain energy and get warmer
    exothermic_Surroundings = "Exothermic surroundings: Gain energy and get warmer"
    # heat written as a product 
    exothermic_Product = "Exothermic: (g)  >  (l)  >  (s) "

    def exothermic_Attributes(self):
        print(exothermic)
        print(exothermic_System)
        print(exothermic_Surroundings)
        print(exothermic_Product)

    ############################# Endothermic ################################ 

    # https://youtu.be/GQkJI-Nq3Os - Lab reaction

    # Ba(OH)2 + NH4Cl → BaCl2 + NH3 + H2O
    # DH = +164 kJ

    # DH is (+)
    endothermic = "Endothermic: Change in heat is (+) positive"
    # reaction(system) gains energy  
    endothermic_System = "Endothermic system: Gains Energy"
    # solution(surroundings) lose energy and get colder
    endothermic_Surroundings = "Endothermic surroundings: Lose Energy and get colder"
    # heat written as a reactant
    endothermic_Product = " Endothermic: (s)  >  (l)  >  (g) "

    def endothermic_Attributes(self):
        print(endothermic)
        print(endothermic_System)
        print(endothermic_Surroundings)
        print(endothermic_Product)

    ############################## Examples: ################################## 

    # Classify each process as exothermic or endothermic.  
    # What will be the sign of DH?

    # Water vapor condenses on a cold pipe.             : exo
    # Ice cube melts.                                   : endo
    # Natural gas burning on a stove                    : exo
    # Nail polish remover evaporates                    : endo
    # N2(g) + O2(g) + heat   >  2 NO(g)                 : endo
    # PCl3(g) + Cl2(g)  >  PCl5(g)......DH = – 88kJ     : exo

"""
    ################################## homework 7 ##################################
    #question 1 
    print("1>")
    #b
    kcal = 3495
    J = 4.184
    ans = kcal * J
    print(ans)
    #c
    joules = 8.74 * pow(10, 6)
    cal = joules / J
    kcal = cal / 1000
    print(kcal)
    #question 2
    print("2>")
    joules = 2264
    cal = joules / J
    print(cal)
    #question 4
    print("4>")
    #joules over grams celcius
    g = 55.84
    Ti = 29
    Tf = 131.4
    delta_t = Tf - Ti
    q = 1015
    ans = q / (g*delta_t)
    print(ans)
    #question 5
    print("5>")
    sh = 1.75
    kg = 2.54
    g = kg * 1000
    Tf = 191
    Ti = 23
    delta_t = Tf - Ti
    q = g * sh * delta_t
    print(q)
    #question 6
    print("6>")
    m = 19
    c = specificHeat_dict["water"]
    Tf = 49
    Ti = 27
    delta_t = Tf - Ti
    q = m * c * delta_t
    q = q / 4.184
    print(q)
    #q = 0
    #q6 = specifiedQ(q, m, sh, Ti, Tf)
    #print(q6)
    #b
    m = 93
    Ti = 17
    Tf = 79
    delta_t = Tf - Ti
    q = m * delta_t
    q /= 1000
    print(q)

    #question 7
    print('7>')
    c = specificHeat_dict["silver"]
    q = 271
    delta_t = 23.6
    m = q / (c*delta_t)
    print(m)
    
    #question 8
    print('8>')
    c = 0.128
    q = 305
    m = 92.1
    Ti = 20
    Tf = (q / (c * m)) + Ti
    print(Tf)
"""






