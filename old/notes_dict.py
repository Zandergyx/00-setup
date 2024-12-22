# capitals = ["Manila", "Kuala Lumpur", "Singapore", "Bangkok", "Ottawa"]

capitals = {
    "Phiippines":"Manila",
    "Malaysia":"Kuala Lumpur"}

# accessing a value
print(capitals["Malaysia"])

# adding a value
capitals["Indonesia"] = "Jakarta"

# changing a value
capitals["Indonesia"] = "Medan"

# Iterating through a dictionary
for k in capitals:
    print(k)

for k in capitals.keys():
    print(k)

for v in capitals.values():
    print(v)

for item in capitals.items():
    print(item)

for k, v in capitals.items():
    print(f"The capital of {k} is {v}.")

