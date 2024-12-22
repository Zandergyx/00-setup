month = input("Enter a month:  ")
month = month.title()
day = int(input("Enter a date:  "))
if((month == 'Mar' and day >= 20 and day <= 30) or (month == 'Apr' or month == 'May') or month == 'Jun' and day >=1 and day <= 20):
    print("Spring")
elif((month == 'Jun' and day >= 21 and day <= 30) or (month == 'Jul' or month == 'Aug') or month == 'Sep' and day >=1 and day <= 21):
    print("Summer")
elif((month == 'Sep' and day >= 22 and day <= 30) or (month == 'Oct' or month == 'Nov') or month == 'Dec' and day >=1 and day <= 20):
    print("Fall")
else:
    print("Winter")