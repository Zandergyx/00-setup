pressure = float(input("What is the pressure of the item"))
vol = float(input("What is the volume of the item"))
temp = float(input("What is the temperature of the item"))

n = (pressure*vol)/(8.314*temp)
print(f"The amount of gas in moles is {n}")

