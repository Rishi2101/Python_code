#Q1
str1="Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star,\n\tHow I wonder what you are"
print(str1)

#Q2
import sys
print("python version")
print(sys.version)


#Q4
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r * r))

#Q15 Write a Python program to get the volume of a sphere with radius 6.
from math import pi
r=6
V=((4.0/3.0)* pi * r**2)
