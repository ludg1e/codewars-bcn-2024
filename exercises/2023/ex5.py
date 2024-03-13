vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

inp = input("String: ")

for v in vowels:
    inp = inp.replace(v, "*")

print(inp)
