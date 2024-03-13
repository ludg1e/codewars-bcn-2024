inp1 = input("")

chars = list(inp1)

res = []

for char in chars:
    resu = char * 2
    res.append(resu)

print("".join(res))
