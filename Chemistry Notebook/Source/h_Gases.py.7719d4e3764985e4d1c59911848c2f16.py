## Chapter 6.1 Gases

import os, math, numpy
#import Moles

class gases:

    def __init__(self):
        (self)

    answers = []

    #fileName = "gases.txt"
    #fileLocation = os.chdir("C:\Users\jeric\OneDrive\School\Chemistry 101")
    #file myFile = open(fileName, "a")
    #myFile.write("Hello World")
    #myFile.close()

    ##### 6.1 Kenetic Theory of Gases

    # 1. Gases consist of tiny particles in constant motion.
    # 2. Gas particles are constantly colliding with each other and the
    #    walls of a container.
    # 3. Size of gas particles is negligible small compared to the 
    #    space between them.
    # 4. Gas particles don’t attract each other.
    # 5. The average speed of gas particles is proportional to the  
    #    temperature of the gas. (higher temp=faster speed)

    # Kinetic Theory of Gases explains the gas laws in this chapter.  
    # It was formulated after the gas laws were discovered.

    # An ideal gas is one that perfectly follows the statements in 
    # the kinetic theory.

    # Most gases are close to ideal under most conditions. 
    # At very low temperatures and high pressures the theory and 
    # laws don’t fit well.

    # http://intro.chem.okstate.edu/1314F00/Laboratory/GLP.htm

    # Pressure is defined as the force exerted on a given area

    F = "Force"
    A = "Area"
    P = "Pressure"
    V = "Volume"
    T = "Temperature(always in Kelvin for gas laws)"
    n = "Number of moles of gas"

    pressure = "Pressure = Force / Area" 

    print(pressure)

    # Properties can be:
    # Directly related – as one goes up, the other goes up
    # Indirectly related – as one goes up, the other goes down.





    ############################## Units Of Pressure #########################

    # The pressure of the atmosphere is about 14.7 pounds of force for every square inch of surface area: 14.7 lb/in2.
    # The formal, SI-approved unit of pressure is the pascal (Pa), which is defined as 1 N/m2 
    # (one newton of force over an area of one square meter). However, this is usually too small in magnitude to be useful. 
    # A common unit of pressure is the atmosphere (atm), which was originally defined as the average atmospheric pressure at sea level.
    # average atmospheric pressure at sea level” is difficult to pinpoint because of atmospheric pressure variations. 
    # A more reliable and common unit is millimeters of mercury (mmHg), which is the amount of pressure exerted by a column of 
    # mercury exactly 1 mm high. An equivalent unit is the torr, which equals 1 mmHg. (The torr is named after 
    # Evangelista Torricelli, a seventeenth-century Italian scientist who invented the mercury barometer.)
    # make round to significant figures class/method

    kelvin = 273.15
    const_atm = 1         # 1 unit of atmospheric pressure
    const_torr = 760      # millimeters of Murcury (mmHg)
    const_Hg = 29.92      # inches of Murcury (inHg)
    const_Pa = 101325     # Pascals
    const_kPa = 101.325   # kiloPascals
    const_psi = 14.7      # Pounds per square inch

    # c to k 
    # return degrees
    def c_to_K_Converter(self, degrees):
        degrees = degrees + kelvin
        return(degrees) 
    # k to c
    # return degrees
    def K_to_c_Converter(self, degrees):
        kelvin = 273.15
        degrees = degrees - kelvin
        return(degrees)
    # torr to atm
    # return pressure
    def Torr_to_atm_converter(self, pressure):
        const_torr = 760  
        pressure = pressure / const_torr
        return(pressure)
    # atm to torr
    #return pressure
    def atm_to_Torr_converter(self, pressure):
        pressure = pressure * const_torr
        return(pressure)
    # Hg to atm
    # return pressure
    def Hg_to_atm_converter(self, pressure):
        pressure = pressure / const_Hg
        return(pressure)
    # Pa to atm
    # return pressure
    def Pa_to_atm_converter(self, pressure):
        pressure = pressure / const_Pa
        return(pressure)
    # kPa to atm
    # return pressure
    def kPa_to_atm_converter(self, pressure):
        pressure = pressure / const_kPa
        return(pressure)
    # psi to atm
    # return pressure
    def psi_to_atm_converter(self, pressure):
        pressure = pressure / const_psi
        return(pressure)


   

    # Universal Gas constant = R

    ## Universal Gas constant = 0.08205 
    ## Using units = (L * atm) / (mol * K)

    ## Universal gas constant = 62.36
    ## Using units = (L * torr) / (mol * k) = (L * mmHg / mol * K)

    # change ml to L

    rAtm = 0.08205
    rTorr_rmmHg = 62.36




    ####################  Sandard Conditions  ################################

    # Standard temp and pressure
    # Pressure = 1atm
    # Temperature = 0C = 273.15K

    # the volume of 1 mole of any gas at STP is 22.4L

    # PV = nRT
    # V = nRT/P
    R = 0.08206

    def standard_Conditions(self, P, n, T, V):
        R = 0.08206

        if P > 0:
            self.P = P
        else:
            self.P = (n*R*T) / V
            return(self.P)
        if n > 0:
            self.n = n
        else:
            self.n = (P*V) / (R*T)
            return(self.n)
        if T > 0:
            self.T = T
        else:
            self.T = (P*V) / (n*R)
            return(self.T)
        if V > 0:
            self.V = V
        else:
            self.V = (n*R*T) / P
            return(self.V)


    stp = 22.4

    # STP example
    L = 6.6#Leters
    ans = L/stp
    print("Stp example:\t" + str(ans))
    answers.append(ans)

    V = 42 #Volume
    O = 15.994 # Oxygen 
    # two oxygen molecules
    ## make and import atoms / molecules class

    ans = 42 / (O*2) 
    print("STP Example 2:\t" + str(ans))
    answers.append(ans)

    ##


    ######################### Gas Mixtures ################################

    # Partial pressure - 
    # the pressure an individual gas exerts in a mixture


    # Dalton’s Law of Partial Pressures – the total pressure of
    # a gas mixture is equal to the sum of the partial pressures 
    # of all components:

    # P(total) = P1 + P2 + P3 + ...

    # Partial Pressures Example 
    # pressure of O2 .450 atm
    # change atm to torr
    # pressure of Helium 855 mmHg

    atm = 0.450

    mmHg = 855

    PO2 = atm * const_torr
    PHe = 855 
    pTot = PO2 + PHe

    answers.append(pTot)
    #print("Pressure Totals Example:\t" + str(pTot))

    def partialPressures(self, pArray, ptot):
        loneStar = ptot - sum(pArray)
        self.partialPressuresArray = pArray
        if ptot == 0:
            ptot = sum(pArray)
        self.partialPressuresTotal = ptot



    ########################## Gas Laws #####################################

    # Boyle's Law
    # Pressure and Volume are indirectly related
    # p1 * v1 = p2 * v2
    # at constant n and T 

    def Boyles_Law(self, p1, p2, v1, v2):
        print("Boyle's Law")
        if p1 > 0:
            p1 = p1
            print("The Volume of p1 = " + str(p1))
        else:
            p1 = (p2 * v2) / v1
            print("The Volume of p1 = " + str(p1))
            return(p1)
        if p2 > 0:
            p2 = p2
            print("The Volume of p2 = " + str(p2))
        else:
            p2 = (p1 * v1) / v2
            print("The Volume of p2 = " + str(p2))
            return(p2)
        if v1 > 0:
            v1 = v1
            print("The Volume of v1 = " + str(v1))
        else:
            v1 = (v2 * p2) / p1
            print("The Volume of v1 = " + str(v1))
            return(v1)
        if v2 > 0:
            v2 = v2
            print("The Volume of v2 = " + str(v2))
        else:
            v2 = (v1 * p1) / p2
            print("The Volume of v2 = " + str(v2))
            return(v2)


    # Gay-Lussac's Law
    # pressure and temperature are directly related
    # p1 / t1 = p2 / t2
    # at constant V and n
    def Gay_Lussacs_Law(self, p1, p2, t1, t2):
        print("Gay Lussacs Law")
        if t1 > 0:
            t1 = t1
            print("The Temperature of t1 = " + str(t1 - kelvin))
        else:
            t1 = (p1 * t2) / p2
            print("The Temperature of t1 = " + str(t1 - kelvin))
            return(t1)    
        if t2 > 0:
            t2 = t2
            print("The Temperature of t2 = " + str(t2 - kelvin))
        else:
            t2 = (p2 * t1) / p1
            print("The Temperature of t2 = " + str(t2 - kelvin))
            return(t2)
        if p1 > 0:
            p1 = p1
            print("The Volume of p1 = " + str(p1))
        else:
            p1 = (p2 * t1) / t2
            print("The Volume of p1 = " + str(p1))
            return(p1)
        if p2 > 0:
            p2 = p2
            print("The Volume of p2 = " + str(p2))
        else:    
            p2 = (p1 * t2) / t1
            print("The Volume of p2 = " + str(p2))
            return(p2)


    # Charles Law
    # volume and temperature are directly related 
    # v1/t1 = v2/t2
    # at constant P and n

    def Charles_Law(self, v1, v2, t1, t2):
        print("Charles Law")
        if t1 > 0:
            t1 = t1
            print("The Temperature of t1 = " + str(t1 - kelvin))
        else:
            t1 = (v1 * t2) / v2    
            print("The Temperature of t1 = " + str(t1 - kelvin))
            return(t1)
        if t2 > 0:
            t2 = t2
            print("The Temperature of t2 = " + str(t2 - kelvin))
        else:
            t2 = (v2 * t1) / v1
            print("The Temperature of t2 = " + str(t2 - kelvin))
            return(t2)
        if v1 > 0:
            v1 = v1
            print("The Volume of v1 = " + str(v1))
        else:
            v1 = (v2 * t1) / t2
            print("The Volume of v1 = " + str(v1))
            return(v1)
        if v2 > 0:
            v2 = v2
            print("The Volume of v2 = " + str(v2))
        else:    
            v2 = (v1 * t2) / t1
            print("The Volume of v2 = " + str(v2))
            return(v2)

    # Avogadro's Law
    # Volume and moles are directly related
    # v1/n1 = v2/n2
    # at constant P and T
    def Avogadros_Law(self, v1, v2, n1, n2):
        print("Avogadro's Law")
        if v1 > 0:
            v1 = v1
            print("The Volume of v1 = " + str(v1))
        else:
            v1 = (v2 * n1) / n2
            print("The Volume of v1 = " + str(v1))
            return(v1)
        if v2 > 0:
            v2 = v2
            print("The Volume of v2 = " + str(v2))
        else:    
            v2 = (v1 * n2) / n1
            print("The Volume of v2 = " + str(v2))
            return(v2)
        if n1 > 0:
            n1 = n1
            print("The Mole of n1 = " + str(n1))
        else:
            n1 = (v1 * n2) / v2
            print("The Mole of n1 = " + str(n1))
            return(n1)
        if n2 > 0:
            n2 = n2
            print("The Mole of n2 = " + str(n2))
        else:
            n2 = (v2 * n1) / v1
            print("The Mole of n2 = " + str(n2))
            return(n2)

    # Combined Gas Law
    # Used when three properties are changing instead of two
    # p1v1/t1 = p2v2/t2
    # at constant n
    # convert to kelvin
    def Combined_Gas_Law(self, p1, p2, v1, v2, t1, t2):
        print("Combined Gas Law")
        if t1 > 0:
            t1 = t1
            print("The Temperature of t1 = " + str(t1))
        else:
            t1 = (p1*v1*t2) / (p2*v2)
            print("The Temperature of t1 = " + str(t1))
            return(t1)
        if t2 > 0:
            t2 = t2
            print("The Temperature of t2 = " + str(t2))
        else:
            t2 = (p2*v2*t1) / (p1*v1)
            print("The Temperature of t2 = " + str(t2))
            return(t2)
        if p1 > 0:
            p1 = p1
            print("The Pressure of p1 = " + str(p1))
        else:
            p1 = (p2 * v2 * t1) / (t2 * v1)
            print("The Pressure of p1 = " + str(p1))
            return(p1)
        if p2 > 0:
            p2 = p2
            print("The Pressure of p2 = " + str(p2))
        else:
            p2 = (p1 * v1 * t2) / (t1 * v2)
            print("The Pressure of p2 = " + str(p2))
            return(p2)
        if v1 > 0:
            v1 = v1
            print("The Volume of v1 = " + str(v1))
        else:
            v1 = (v2 * t1 * p2) / (t2 * p2)
            print("The Volume of v1 = " + str(v1))
            return(v1)
        if v2 > 0:
            v2 = v2
            print("The Volume of v2 = " + str(v2))
        else:
            v2 = (v1 * t2 * p1) / (t1 * p2)
            print("The Final Volume of v2 = " + str(v2))
            return(v2)

   
