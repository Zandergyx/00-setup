from math import *
note_dict = {"C":261.63,"D":293.66,"E":329.63,"F":349.23,"G":392.00,"A":440.00,"B":493.88}
note_name = input("Enter the name of a note:  ")
note_type = note_name[0]
octave = int(note_name[1])
formula = pow(2,4-octave)
output = note_dict[note_type] / formula
print(output)