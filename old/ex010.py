import math
a = int(input("Choose a number:  "))
b = int(input("Choose another number:  "))
sum = a+b
diff = a-b
product = a*b
quotient = a/b
remainder = a%b # % Gives Remainder
resultlog10 = math.log10(a)
resultpowerof = math.pow(a,b) # ** is pwr of
print(f"{a}+{b}={sum},\n{a}-{b}={diff},\n{a}*{b}={product},\n{a}/{b}={quotient},\n{a}%{b}={remainder}, \n{a}log10{b}={resultlog10},\n{a} to the power of {b}={resultpowerof}")
