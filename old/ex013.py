cost = float(input("How much does all your goods cost:  "))
paying = float(input("How much are you paying:  "))
#penny 1¢, nickel 5¢, dime 10¢, quarters 25¢,loonies $1, toonies $2
costincents = cost*100
payingincents = paying*100
change = payingincents-costincents
toonie = change%200
numoftoonie = change//200
loonie = toonie%100
numofloonie = toonie//100
quarter = loonie%25
numofquarter = loonie//25
dime = quarter%10
numofdime = quarter//10
nickel = dime%5
numofnickel = dime//5
penny = nickel%1
numofpenny = nickel//1
print(f"You will recieve {numoftoonie} toonies, {numofloonie} loonies, {numofquarter} quarters, {numofdime} dimes and {numofpenny} pennies as change")