sum = 0

llista = []

uinp = abs(int(input("")))

for x in range(uinp):
    if x % 3 == 0:
        llista.append(x)


for i in llista:
    sum = sum + int(i)

if uinp % 3 == 0:
    print(sum + uinp)
else:
    print(sum)
