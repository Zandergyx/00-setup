Ta = float(input("What is the wind temperature in degrees celsius:  "))
V = float(input("What is the wind speed in km/h:  "))
WCI = 13.12+0.215*Ta-11.37*V**0.16+0.3965*Ta*V**0.16
print(f"The wind chill Index is {WCI}")