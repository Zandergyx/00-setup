heightfeet = int(input("Please type your height in feet:  "))
heightinches = int(input("Please type your remaining height in inches:  "))
feettoinch = heightfeet*12+heightinches
inchtocm = feettoinch*2.54
print(f"Your height is {inchtocm}cm")