# JU: Improve on line 5 by using "in" to cehck dict keys

money_dict = {"1":"George Washington","2":"Thomas Jefferson","5":"Abraham Lincoln","10":"Alexander Hamilton","20":" Andrew Jackson","50":" Ulysses S. Grant","100":"Benjamin Franklin"}
banknote_denomination =input("Enter the denomination of the banknote:  ")
if banknote_denomination == '1' or banknote_denomination == '2' or banknote_denomination == '5' or banknote_denomination == '10' or banknote_denomination == '20' or banknote_denomination == '50' or banknote_denomination == '100':
    print(money_dict[banknote_denomination])
else:
    print("Your banknote denomination does not exist try another one!")

