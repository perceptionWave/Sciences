import math
import numpy
import scipy
from ch1_Conversions import conversions 

#Electronic Structure

class electronicStructure():
    
    def __init__(self):
        self
        c = 3.00 * pow(10, 8)
        

cObj = conversions()

############################### 8.1 - Light ################################ 

# The wavelength of light is the distance between corresponding points in two adjacent light cycles, and the frequency of light is the number of # cycles of light that pass a given point in one second. Wavelength is typically represented by λ, the lowercase Greek letter lambda, while 
# frequency is represented by ν, the lowercase Greek letter nu (although it looks like a Roman “vee,” it is actually the Greek equivalent of the 
# letter “en”). Wavelength has units of length (meters, centimeters, etc.), while frequency has units of per second, written as s−1 and sometimes 
# called a hertz (Hz)

# One property of waves is that their speed is equal to their wavelength times their frequency.
# speed=λν

# For light, however, speed is actually a universal constant when light is traveling through a vacuum (or, to a very good approximation, air). 
# The measured speed of light (c) in a vacuum is 2.9979 × 108 m/s, or about 3.00 × 108 m/s.
# c=λν
# λ(nu) = "wavelength"
# v = "frequency"

# The mathematical equation that relates the energy (E) of light to its frequency is
# where ν is the frequency of the light, and h is a constant called Planck’s constant. Its value is (6.626 × 10−34 J·s)—a very small number that 
# is another fundamental constant of our universe, like the speed of light.
# E = hν
h = 6.626 * pow(10, -34) # planck's constant


# Because a light wave behaves like a little particle of energy, light waves have a particle-type name: the photon.

# Wavelengths, frequencies, and energies of light span a wide range; the entire range of possible values for light is called the electromagnetic 
# spectrum.

# visible light, which is light having a wavelength range between about 400 nm and 700 nm.

# The electromagnetic spectrum 
# https://imagine.gsfc.nasa.gov/science/toolbox/emspectrum2.html




################################################### 8.2 Quantum Numbers of Electrons ###########################################################

# There are two fundamental ways of generating light: either heat an object up so hot it glows or pass an electrical current through a sample of 
# matter (usually a gas). Incandescent lights and fluorescent lights generate light via these two methods, respectively.

# A hot object gives off a continuum of light. We notice this when the visible portion of the electromagnetic spectrum is passed through a prism: 
# the prism separates light into its constituent colors, and all colors are present in a continuous rainbow (part (a) in Figure 8.3 "Prisms and 
# Light"). This image is known as a continuous spectrum. However, when electricity is passed through a gas and light is emitted and this light is 
# passed though a prism, we see only certain lines of light in the image (part (b) in Figure 8.3 "Prisms and Light"). This image is called a line 
# spectrum. It turns out that every element has its own unique, characteristic line spectrum

c = "c is The speed of light in a constant"
print(c)

c_constant = 3.00 * pow(10,8)
print("c = " + str(c_constant))


######################################################## Examples #############################################################
#### Example 1 
print("Example 1:")
v = 88500000
ans = c_constant / v
print(ans)

#### Example 2
#Red light has a wavelength of 7.55 x 10-8 m, what is its frequency?	
print("Example 2:")
nu = 7.55 * pow(10, -8)
v = c_constant / nu
print(v)


# Example 3
# What is the frequency of light if its wavelength is 5.55 × 10−7 m?
print("Example 3:")
v = 5.55 * pow(10, -7)
ans = c_constant / v
print(ans)

############################################################ Homework ###########################################################
print("Homework 8")
#question 1
print("1>")
m = "m"
cm = "cm"
v = 440.00
c = 343.06
c = cObj.convert(c, m, cm)
nu = c / v
print(nu)

#question 2
print("2>")
#certain shade of blue
v = 7.31*pow(10,14)
e = v * h
print(e)

#question 3
print("3>")

nu = 12.9
cm = "cm"
m = "m"
nu = cObj.convert(nu, cm, m)
v = c_constant / nu
e = h * v
print(e)




################## 8.3 - Organization of Electrons in Atoms ################

################ 8.4 - Electron Structure and the Periodic table ###########

########################### 8.5 - Periodic Trends ##########################

