num = int(input("Enter a number:  "))
if num < 2 and num < 0:
    print("Error Enter a positive number greater than 1")
    num = int(input("Enter a number:  "))
additional = num - 2
dog_years = 10.5+(4*additional)
print(f"Your number in dogs years is {dog_years}")