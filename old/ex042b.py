

from math import *
note_name = input("Enter the name of a note:  ")
note_type = note_name[0]
octave = int(note_name[1])
formula = pow(2,4-octave)
if note_type == 'C':
    output = 261.63 / formula
elif note_type == 'D':
    output = 293.66 / formula
elif note_type == 'E':
    output = 329.63 / formula
elif note_type == 'F':
    output = 349.23 / formula
elif note_type == 'G':
    output = 392.00 / formula
elif note_type == 'A':
    output = 440.00 / formula
elif note_type == 'B':
    output = 493.88 / formula
print(output)