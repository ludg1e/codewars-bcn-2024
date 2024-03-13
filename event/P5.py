inp1 = abs(int(input("")))
inp2 = abs(int(input("")))


if int(inp2 / 13) < 1:
    res = inp1
else:
    res = inp1 * 2 ** int(inp2 / 13)

# res = (inp1 * int(inp2 / 13)) * 2
print(res)
