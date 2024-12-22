import math
latitude = int(input("Input the latitude:  "))
longitude = int(input("Input the longitude:  "))
latitude2 = int(input("Input the latitude of the second place:  "))
longitude2 = int(input("Input the longitude of the second place:  "))
distance = 6371.01*math.acos(math.sin(latitude))*math.sin(latitude2)+math.cos(latitude)*math.cos(latitude2*math.cos(longitude-longitude2))
finaldistance = math.radians(distance)
print(f"The distance between the two places are:{finaldistance}km")