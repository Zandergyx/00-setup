Gradepts = float(input("What is your Grade Point:  "))
if Gradepts >= 4.0:
    print("A+")
elif Gradepts < 4.0 and Gradepts >= 3.7:
    print("A-")
elif Gradepts < 3.7 and Gradepts >= 3.3:
    print("B+")
elif Gradepts < 3.3 and Gradepts >= 3.0:
    print("B")
elif Gradepts < 3.0 and Gradepts >= 2.7:
    print("B-")
elif Gradepts < 2.7 and Gradepts >= 2.3:
    print("C+")
elif Gradepts < 2.3 and Gradepts >= 2.0:
    print("C")
elif Gradepts < 2.0 and Gradepts >= 1.7:
    print("C-")
elif Gradepts < 1.7 and Gradepts >= 1.3:
    print("D+")
elif Gradepts < 1.3 and Gradepts >= 1.0:
    print("D")
else:
    print("F")