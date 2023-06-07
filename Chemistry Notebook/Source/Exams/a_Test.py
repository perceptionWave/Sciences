from ch1_Conversions import conversions
from ch2_Density import density
from ch3_BalancingChemicalEquations import balancingChemicalEquations
from ch4_Moles import moles
from ch5_Gases import gases
from ch7_Energy import energy
from ch_8ElectronicStructure import electronicStructure
from ch11_Solutions import solutions

#b = balancingChemicalEquations()
#b.equation("NaOH6 + CH = Na5 + H4O+ H4")

m = moles()
a = ["Ag", "N", "O", "O", "O"]
m.input_Molecule(0, 61.7, 2, a)
b = ["Ag", "Ag", "Cr", "O", "O", "O", "O"]
m.input_Molecule(0.3632146557407931, 0 , 1, b)

gas = gases()
x = gas.standard_Conditions(2.77, 3.10, 0, 71.13)
x = gas.K_to_c_Converter(x)
print(x)

p1 = gas.Torr_to_atm_converter(761)
gas.Combined_Gas_Law(p1, 0.0620, 55.0, 0, 292.55, 264.36)

M = solutions()
c = ["K", "I", "O", "O", "O"]
m.input_Molecule(0, 565, 1, c)
n = 2.640
molar = M.molarity(n, 5.00, 0)

e = energy()
q22 = e.specifiedQ(634, 53.48, 0, 22.9, 102.6)
print("q22:\t" + str(q22))

con = conversions()
v = con.convert(6.65, "mm", "inch")
print(v)
# with open(r"C:\Users\jeric\Documents\School\Chemistry\Periodic Table of Elements.csv", "rt")as f:
    






        
        
