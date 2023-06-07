import math
print("################ HW week 2 ##############\n\n")
print("2. A student drove to the university from her home and noted that the odometer on her car increased by 12.0 km. The trip took 17.0 min.\n")
x = 12
t = 17

print("(a) What was her average speed in km/h?\n")
def avgSpeed(x, x0, t): 
    return ((x - x0) / t)
    
oneA = avgSpeed(12, 0, 17)
oneA *= 60
oneA = round(oneA, 6)
print("2. (a) " + str(oneA) + " km/h\n")

print("(b) If the straight-line distance from her home to the university is 10.3 km in a direction 25.0° south of east, what was her average velocity in km/h?\n")

# avgVelocity
# input: 
#       x = poistion
#       x0 = initial position
#       t = time
# Output:
#       avgVelocity
def avgVelocity(x, x0, t): 
    return((x-x0)/t)

# Acceleration
# input: 
#       v = velocity
#       v0 = initial velocity
#       t = time
# Output:
#       a = acceleration
def acceleration(v, v0, t): 
    return((v-v0)/t)

oneB = avgVelocity(10.3, 0, 17)
oneB *= 60
oneB = round(oneB, 6)
print("2. (b) " + str(oneB) + " mph\n")

print("(c) If she returned home by the same path 7 h 30 min after she left, what were her average speed and velocity in km/h for the entire trip?\n")

oneC = avgSpeed(20.6, 0, 7.5)
oneC = round(oneC, 6)
print("2. (c) " + str(oneC) + " s")
oneC = avgVelocity(20.6, 0, 7.5)
oneC = round(oneC, 6)
print("2. (c) " + str(oneC) + " km/h")

# displacement  
def displacement(x0, v0, t, a):
    return(x0+(v0*t)+((1/2)*a*t**2))


# 3
print("3. A commuter backs her car out of her garage with a constant acceleration of 1.20 m/s2.\n")
a = 1.20

#3a
print("(a) How long in seconds does it take her to reach a speed of 1.90 m/s?\n")
speed = 1.90
seconds = speed / a
print("3. (a)" + str(seconds))

# 3b
print("(b) If she then brakes to a stop in 0.8 s, what is her (constant) deceleration in m/s2?\n")
seconds = 0.8
a = speed / seconds
print("3. (b)"+ str(a))

# 4
print("Assume that an MX missile goes from rest to a suborbital velocity of 4.50 km/s in 50.0 s (the actual speed and time are classified). What is its average acceleration in m/s2? What is its average acceleration in multiples of g?\n")

v0 = 0 
v1 = 4.5
t = 50.0
g = 9.8
m = 1000

avgA = (v1 / t) * m
print("4. (a) " + str(avgA) + " m/s2\n")

avgAg = avgA / g
print("4. (b) " + str(avgAg) + " m/s2\n")

# 5
print("5. A light-rail commuter train accelerates at a rate of 1.15 m/s2. How long (in s) does it take to reach its top speed of 80.0 km/h, starting from rest?\n")

a = 1.15
topS = 80.0
t = 0
s = 60

topS *= m / s / s

tF = topS / a
print("5. " + str(topS) + " s\n")

print("The same train ordinarily decelerates at a rate of 1.55 m/s2. How long (in s) does it take to come to a stop from its top speed?\n")
s = 8.3
eD = topS / s 

print("5. (b) " + str(eD) + " m/s2\n")


# 6
print("6. An unwary football player collides with a padded goalpost while running at a velocity of 6.40 m/s and comes to a full stop after compressing the padding and his body 0.320 m.\n")

v = 6.4
x0 = 0
x = 0.320
# a
print("A. What is his deceleration in m/s2?\n")
t = x / v

a = v / t
print("A. "  +str(a) + " m/s2\n")

# b
print("How long in seconds does the collision last?\n")
t = x / a
print("b. " + str(t) + " s\n")


