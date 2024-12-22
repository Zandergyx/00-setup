import math
radius = float(input("What is the radius:  "))
height = float(input("What is the height:  "))
area_of_circle = (radius**2)*math.pi
cylinder_vol = area_of_circle*height
print(f"The volume of a cylinder is {cylinder_vol}")