month = input("Enter your birth month:  ")
month = month.title()
day = int(input("Enter your birth date:  "))
if((month == 'Dec' and day >= 22 and day <= 30) or (month == 'Jan' and day >= 1 and day <= 19)):
    print("Capricorn")
elif((month == 'Jan' and day >= 20 and day <= 30) or (month == 'Feb' and day >= 1 and day <= 18)):
    print("Aquarius")
elif((month == 'Feb' and day >= 19 and day <= 30) or (month == 'Mar' and day >= 1 and day <= 20)):
    print("Pisces")
elif((month == 'Mar' and day >= 21 and day <= 30) or (month == 'Apr' and day >= 1 and day <= 19)):
    print("Aries")
elif((month == 'Apr' and day >= 20 and day <= 30) or (month == 'May' and day >= 1 and day <= 20)):
    print("Taurus")
elif((month == 'May' and day >= 21 and day <= 30) or (month == 'Jun' and day >= 1 and day <= 20)):
    print("Gemini")
elif((month == 'Jun' and day >= 21 and day <= 30) or (month == 'Jul' and day >= 1 and day <= 22)):
    print("Cancer")
elif((month == 'Jul' and day >= 23 and day <= 30) or (month == 'Aug' and day >= 1 and day <= 22)):
    print("Leo")
elif((month == 'Aug' and day >= 23 and day <= 30) or (month == 'Sep' and day >= 1 and day <= 22)):
    print("Virgo")
elif((month == 'Sep' and day >= 23 and day <= 30) or (month == 'Oct' and day >= 1 and day <= 22)):
    print("Libra")
elif((month == 'Oct' and day >= 23 and day <= 30) or (month == 'Nov' and day >= 1 and day <= 21)):
    print("Scorpio")
else:
    print("Sagittarius")