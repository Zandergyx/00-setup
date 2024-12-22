loaves = int(input("How many loaves of bread do you want to buy:  "))
discount = 3.49*(60/100)
original_total = loaves*3.49
round(discount,2)
total = original_total-discount
total_discount = discount*loaves
dis = round(total_discount,2)
Nett = original_total-dis
print(f"""         --------------------
         Checkout  |    Count
         --------------------
         Bread ($3.49)      {loaves}
         Total:        ${original_total}
         Discount:      ${dis}
         --------------------
         Nett:          ${Nett}""")

