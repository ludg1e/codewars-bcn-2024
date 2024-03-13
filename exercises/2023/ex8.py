# even = parell
# odd = imparell

while True:
    uinp = abs(float(input("Number: ")))
    if not uinp > 1:
        print("Input must be greater than one")
        continue
    else:
        break

seq = [uinp]


def fun(inp):
    while inp != 1:
        if inp % 2 == 0:
            # print("Input is even")
            inp = float((inp / 2))
            seq.append(inp)
            # print(inp)
        else:
            # print("Input is odd")
            inp = float((inp * 3) + 1)
            seq.append(inp)
            # print(inp)


fun(uinp)
fseq = str(seq)
print(
    fseq.replace("[", "").replace("]", "").replace(", ", " -> ")
    + " ["
    + str(len(seq) - 1)
    + "]"
)
