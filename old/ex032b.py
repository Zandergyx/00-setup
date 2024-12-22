num = int(input("Enter a 4 digit number:  "))
for i in range(3):
    value = num%10
    num//10

value1 = num%10
num1 = num//10
value2 = num1%10
num2 = num1//10
value3 = num2%10
num3 = num2//10
value4 = num3%10
num4 = num3//10
sum = value1+value2+value3+value4
print(f" The sum of all numbers in the place values ones tens hundreds and thousands is {sum}")