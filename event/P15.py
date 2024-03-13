abc = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
ex = 0
llista = []
s = ""
llistap = []
while ex == 0:
    a = input()
    llista.append(a.lower())
    if "#" in a:
        ex = ex + 1
else:
    for n in llista:
        s = s + n
    for i in abc:
        if i not in s:
            llistap.append(i.lower())
    t = len(llistap)
    if t == 0:
        print("There are no letters lost!")
    else:
        for y in range(t):
            if y < (t):
                print(("    ") * (y) + llistap[y] + "_")
            else:
                print(("    ") * (y))
