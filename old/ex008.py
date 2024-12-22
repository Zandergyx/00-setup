widgets = int(input("How many widgets are you buying:  "))
gizmos = int(input("How many gizmos are you buying:  "))
weightg = (widgets*75)+(gizmos*112)
weightkg = ((widgets*75)+(gizmos*112))/1000
print(f"All of the items weighs {weightg} in grams and {weightkg} in kg")