import math
height = int(input("How high was the object dropped from"))
initial_speed = 0#m/s
acceleration = 9.8#m/s
vf = math.sqrt(initial_speed**2+2*acceleration*height)
print(f"The Final Speed is {vf}")