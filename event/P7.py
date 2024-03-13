lines = []

while True:
    line = input()
    if line == "#":
        break
    else:
        lines.append(line)

ex = 0
ym = 0
for line in lines:
    xm = len(line)
# xm = len(uinp)

llista = []

for x in llista:
    ss = ss + str(x)
for a in ss:
    if a == "o":
        pos = ss.find(a)
        cx = pos % ym
        cy = int(pos / xm)
        print(cx + ", " + cy)
