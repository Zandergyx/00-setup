magnitude = float(input("Enter an earthquakes magnitude"))
if magnitude < 2.0:
    print("The magnitude is considered a Micro earthquake")
elif magnitude > 2.0 and magnitude < 3.0:
    print("The magnitude is considered a Very Minor earthquake")
elif magnitude > 3.0 and magnitude < 4.0:
    print("The magnitude is considered a Minor earthquake")
elif magnitude > 4.0 and magnitude < 5.0:
    print("The magnitude is considered a Light earthquake")
elif magnitude > 5.0 and magnitude < 6.0:
    print("The magnitude is considered a Moderate earthquake")
elif magnitude > 6.0 and magnitude < 7.0:
    print("The magnitude is considered a Strong earthquake")
elif magnitude > 7.0 and magnitude < 8.0:
    print("The magnitude is considered a Major earthquake")
elif magnitude > 8.0 and magnitude < 10.0:
    print("The magnitude is considered a Great earthquake")
elif magnitude < 10:
    print("The magnitude is considered a Meteoric earthquake")
