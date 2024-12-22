rating = float(input("Enter an employee's Performance(0.0/0.4/>0.6)"))
if rating != 0.0 or rating != 0.4 or rating != 0.6:
    print("Error input a different value.")
else:
    if rating == 0.0:
