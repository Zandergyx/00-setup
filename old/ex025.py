sec = int(input("Enter the amount of seconds"))
days = sec%86400
numofdays = sec//86400
hour = days%3600
numofhours = days//3600
min = hour%60
numofmin = hour//60
print(f"{numofdays}:{numofhours}:{numofmin}:{sec}")