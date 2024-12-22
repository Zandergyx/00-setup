SMALLDEPOSIT = 0.10
LARGEDEPOSIT = 0.25
smaller = int(input("How many bottles that have lesser than 1 liter are you depositing:  "))
greater = int(input("How many bottles that have greater than 1 liter are you depositing:  "))
refund = smaller*SMALLDEPOSIT+greater*LARGEDEPOSIT
print(refund)