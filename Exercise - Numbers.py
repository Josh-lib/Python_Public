#--Create a program to calculate the area in circumference of a circle.
#--Ask the user for the radius.
#-- Area=Pi*r^2 ; Circumference =2*Pi*r where r=radius
from cmath import pi
import math

print("This program is go to help you Calculate the Area & Circumference of a circle")

r = float (input("Enter the radius of the circle: "))
Area = pi*(r**2)
C = 2 * pi * r
print("the Area of the circle is: ",Area,"cm \n the Circumference of the circle is: ",C,"cm")