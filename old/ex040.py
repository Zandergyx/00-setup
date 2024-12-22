# JU: Handle this requirement:
# "If the user enters a number of decibels between the noises 
# listed then your program should display a message indicating 
# which noises the value is between."
# 
# Also:
# "Ensure that your program also generates reasonable output for
# a value smaller than the quietest noise in the table, and for 
# a value larger than the loudest noise in the table."


decibel = int(input("Enter a Decibel value:  "))
if decibel == 40:
    print("That decibel value is as loud as a Quiet Room")
elif decibel == 70:
    print("That decibel value is as loud as an Alarm Clock")
elif decibel == 106:
    print("That decibel value is as loud as a Gas Lawnmower")
elif decibel == 130:
    print("That decibel value is as loud as a Jackhammer")
elif decibel < 40:
    print("Enter a higher decibel value")
    decibel = int(input("Enter a Decibel value:  ")) # JU: printing a reasonable message is enough. An input here is not handled.
elif decibel > 130:
    print("Enter a lower decibel value")
    decibel = int(input("Enter a Decibel value:  ")) # JU: printing a reasonable message is enough. An input here is not handled.
elif decibel > 40 and decibel < 70:
    print("The decibel volume is between a Quiet Room and an Alarm Clock")
elif decibel > 70 and decibel < 106:
    print("The decibel volume is between an Alarm Clock and a Gas Lawnmover")
elif decibel > 106 and decibel < 130:
    print("The decibel volume is between a Gas Lawnmower and a Jackhammer")