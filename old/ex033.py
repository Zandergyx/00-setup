num1 = int(input("Enter a number:  "))
num2 = int(input("Enter a number:  "))
num3 = int(input("Enter a number:  "))
smallest = min(num1, num2, num3)
biggest = max(num1, num2, num3)
middle = (num1+num2+num3)-(smallest+biggest)
print(f"The biggest number is {biggest} and the smallest number is {smallest} and the middle number is {middle}")