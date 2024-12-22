from math import *
length = float(input("What is the height of 1 side of your polygon"))
sides = float(input("What is the number of sides for your polygon"))
area = sides*length**2/4*tan(pi/sides)
print(f"The area of the regular polygon is {area}")