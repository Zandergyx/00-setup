# JU: create an alternative solution, using a list, and a certain math property
#     of the years with the same zodiac.
shapes = ['Triangle', 'Square', 'Pentagon', 'Hexagon', 'Septagon', 'Octagon', 'Nonagon', 'Decagon']
sides = int(input("Enter the number of sides of the polygon"))
if sides <= 2 or sides > 10:
    print("Error Enter a positive number greater than 2 and a positive number lesser than 10")
    sides = int(input("Enter the number of sides of the polygon"))
else:
    i = sides - 3
    print(shapes[i])

