meal = float(input("How much did your meal cost:  "))
tip = 18/100*meal
tax = 9/100*meal
grandtotal = meal+tax
txt = f"The grandtotal is  is {grandtotal:.2f} dollars and the tax is {tax:.2f}, the tip is {tip:.2f}"
print(txt)