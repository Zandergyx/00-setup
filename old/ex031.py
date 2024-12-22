kPa = float(input("Enter a pressure in KPa:  "))
MmHg = kPa*33.8
MmMe = kPa*0.0075
psi = kPa/6.89476
print(f"The pressure of your input is {MmHg} in millimeters of atmospheres , {MmMe} in millimeters of mercury and {psi} in pounds per square inch.")