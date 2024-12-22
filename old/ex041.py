# JU: what is the input sequence is 1, 1, 10000000 ?
# Is this a triangle?

side1 = int(input("Enter the length of a triangle:  "))
side2 = int(input("Enter the other length of a triangle:  "))
side3 = int(input("Enter the other length of a triangle:  "))
if side1 == side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles triangle")
else:
    print("Scalene Triangle")
if side1 < 1 or side2 < 1 or side3 < 1:
    print("Error Retype the values.")