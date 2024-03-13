# multiline input; stack overflow
lines = []

print("Please avoid writing non-float numbers")
while True:
    line = input()
    if line == "#":
        break
    else:
        lines.append(line)

uinp = []
errors = []

for line in lines:
    try:
        flo = float(line)
        uinp.append(flo)
    except ValueError:
        errors.append(line)

if len(errors) == 0:
    print("No invalid inputs")
else:
    print("Invalid inputs: " + " | ".join(errors))

print(uinp)

sums = []
prod = []

for flot in uinp:
    sumres = sum(uinp) - flot
    prodls = [f for f in uinp if f != flot]
    """
    Per default fem init a 1 prodres
    Llavors iterem per cada float a prodls, llista que per cada iteració del
    loop parent exclou un float de la llista

    Per cada float a prodls, multipliquem prodres (init a 1) pel float, i el
    resultat és assignat directament a prodres

    A la següent iteració passarà el mateix però el float per el següent num
    de prodls (prodres = 120, llavors 120 * float = 250)
    """
    prodres = 1
    for f in prodls:
        prodres *= f

    sums.append(sumres)
    prod.append(prodres)

"""
map fun: for each item in iterable (obj?; a list for e.g), run a fun

In this case for each float in sums, convert it to a str, later (ext) join
each of the floats in an output where they're separated with a comma
"""
print(", ".join(map(str, sums)))
print(", ".join(map(str, prod)))
