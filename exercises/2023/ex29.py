types = [
    "Rustica",
    "Romana",
    "Prosciutto e funghi",
    "Funghi",
    "Pesto Genovese",
    "Bianca",
    "Carbonara",
    "Sicilian",
    "California",
    "Hawaiian",
    "Pinsa Romana",
    "Caprese",
    "Vegetariana",
    "Quattro formaggi",
    "Diavola",
    "Pepperoni",
    "Quattro stagioni",
    "Calzone",
    "Frutti di mare",
    "Margherita",
    "Prosciutto",
    "Napoletana",
]

lines = []

while True:
    line = input()
    if line == "#":
        break
    else:
        lines.append(line)

valid = []
invalid = []

for line in lines:
        if line not in types:
            invalid.append(line)
        else:
            valid.append(line)

counts = {pizza: valid.count(pizza) for pizza in types if pizza in valid}
sortedp = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            
print("Received valid pizza requests: " + str(len(valid)))

for pizza, count in sortedp:
    if count > 1:
        print(f"{pizza} {count}")
    else:
        print(pizza)

print("---")

print("Invalid requests: " + str(len(invalid)))
print("\n".join(invalid))

