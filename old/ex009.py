savings = float(input("Enter your savings:  "))
year = savings+((4/100)*savings)
year_two = year+((4/100)*year)
year_three = year_two+((4/100)*year_two)
print(f" first year = {year}, second year = {year_two}, third year = {year_three}")
