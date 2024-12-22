# JU: Create an alternative:
# - Use str methods to make this solution fool proof.
# - Use a list instead of many == expressions. Watch all the list videos at https://tinyurl.com/lcclpython1playlist

month = str(input("Enter a month"))
month = month.capitalize()
if month == 'February':
    print('28 or 29')
elif month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'October' or month == 'December':
    print("31")
else:
    print('30')