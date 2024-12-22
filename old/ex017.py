num1 = int(input("Enter the temperature of the water:  "))
num2 = int(input("Enter the temperature of the water you want it to be at:  "))
mass = int(input("Enter the mass of the water:  "))
ΔT = num2-num1
energy = mass*4.186*ΔT
kwh = energy*0.000000277777778
cost = kwh*8.9
print(f"Thw cost will be ${cost}")