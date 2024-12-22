from math import *
a = int(input("What is a:  "))
b = int(input("What is b:  "))
c = int(input("What is c:  "))
descriminant = b**2 - 4*a*c
if descriminant < 0:
    print("There is no real root in this equation")
elif descriminant == 0:
    root0 = -b/2*a
    print(f"There is only one real root which has a value of {root0}")
else:
    root1 = (-b+sqrt(descriminant)/2)
    root2 = (-b-sqrt(descriminant)/2)
    print(f"There are two real roots which have values of {root1} and {root2} respectively.")
