square = str(input("Enter the coordinate:  "))
rank = square[1]
file = square[0]
if (file == 'a' or file == 'c' or file == 'e' or file == 'g')and (rank == '1' or rank == '3' or rank == '5' or rank == '7'):
    print("The square is black")
elif (file == 'b' or file == 'd' or file == 'f' or file == 'h') and (rank == '2' or rank == '4' or rank == '6' or rank == '8'):
    print("The square is black")
else:
    print("The square is white")