import math

class density:

    def __init__(self):
       self

    def desity_of_a_cube(self, mass, length, width, height):

        self.cube_mass = mass
        self.cube_height = height
        self.cube_length = length
        self.cube_width = width
        volume = height * width * length
        self.cube_volume = volume
        denSity = mass / volume
        self.cube_density = denSity
        
    def desity_of_a_cylinder(self, mass, height, radius):
        pi = math.pi
        self.cylinderMass = mass
        self.cylinderHeight = height
        self.cylinderRadius = radius
        volume = pi * height * (self.cylinderRadius**2)
        self.cylinderVolume = volume
        denSity = mass / volume
        self.cylinderDensity = denSity
    
    def density_of_a_liquid(self, mass, volume, denSity):
        if mass > 0:
            self.liquidMass = mass
        else:
            mass = denSity * volume
            self.liquidMass = mass 
        if volume > 0:
            self.liquidVolume = volume
        else:
            volume = mass/denSity
            self.liquidVolume = volume
        if density > 0:
            self.liquidDensity = denSity
        else:
            denSity = mass/volume
            self.denSity = denSity    

    def printCube(self):
        print("$.........Cube")
        print("Length:\t\t" + str(self.cube_length))
        print("Width:\t\t" + str(self.cube_width))
        print("Height:\t\t" + str(self.cube_height))
        print("Mass:\t\t" + str(self.cube_mass))
        print("Volume:\t\t" + str(self.cube_volume))
        print("Density:\t" + str(self.cube_density))
    
    def printCylinder(self):
        print("$.........Cylinder")
        print("Radius:\t\t" + str(self.cylinderRadius))
        print("Height:\t\t" + str(self.cylinderHeight))
        print("Mass:\t\t" + str(self.cylinderMass))
        print("Volume:\t\t" + str(self.cylinderVolume))
        print("Density:\t" + str(self.cylinderDensity))
        
    def printLiquid(self):
        print("$.........Liquid")
        print("Mass:\t\t" + str(self.liquidMass))
        print("Volume:\t\t" + str(self.liquidVolume))
        print("Density:\t\t" + str(self.liquidDensity))
        





