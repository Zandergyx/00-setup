#28Sept - 4Oct
month = input("What is the month:  ")
day = int(input("What is the day:  "))
if month == 'Sep' and day >= 28 and day <= 30 or month == 'Oct' and day <= 1 and day>= 4:
    print('PSLE DAY')
else:
    print('NON-PSLE DAY')