days = int(input(" What is the number of days"))
hours = int(input(" What is the number of hours"))
min = int(input(" What is the number of minutes"))

dayss = days*86400
hourss = hours*3600
mins = min*60
sum = dayss+hourss+mins
print(f"The total amt of seconds is {sum}")