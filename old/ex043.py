# JU: Solution is not correct.

from math import *
note_dict = {261.63:"C4", 293.66:"D4", 329.63:"E4", 349.23:"F4", 440.00:"A4", 493.88:"B4"}
note_freq = float(input("Enter the frequency of a note:  "))
formula = pow(2,4-4)
output = note_freq*formula
print(note_dict[output])