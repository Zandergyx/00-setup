from math import*
height = float(input("What is the height of the triangle"))
base = float(input("What is the base of the triangle"))
hypotenuse = float(input("What is the hypotenuse of the triangle"))
sum = (height+base+hypotenuse)/2
area = sqrt(sum*(sum-height)*(sum-base)*(sum-hypotenuse))
print(f"The Area of  the triangle is {area}")