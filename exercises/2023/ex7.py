# 6 inp
gender = input("Patient gender: ").capitalize()
if gender not in ("Male", "Female"):
    print("Unknown gender or isn't on the world database yet.")
    quit()
else:
    m = "Male"
    f = "Female"

rbcsi = input("Red blood cells (million/mm\N{SUPERSCRIPT THREE}): ")
rbcs = abs(float(rbcsi))

wbcs = abs(int(input("White blood cells (per mm\N{SUPERSCRIPT THREE}): ")))
pla = abs(int(input("Platelets (per mm\N{SUPERSCRIPT THREE}): ")))

hemoi = input("Hemoglobin (g/dL): ")
hemo = abs(float(hemoi))

hemato = abs(int(input("Hematocrit (%): ")))

# default
if 4500 >= wbcs or wbcs >= 11000:
    wbcsr = "VISIT THE DOCTOR"
else:
    wbcsr = "NORMAL"

if 150000 >= pla or pla >= 400000:
    plar = "VISIT THE DOCTOR"
else:
    plar = "NORMAL"

# cases
if gender == m:
    if 4.3 >= rbcs or rbcs >= 5.9:
        rbcsr = "VISIT THE DOCTOR"
    else:
        rbcsr = "NORMAL"

    if 13.5 >= hemo or hemo >= 17.5:
        hemor = "VISIT THE DOCTOR"
    else:
        hemor = "NORMAL"

    if 41 >= hemato or hemato >= 53:
        hemator = "VISIT THE DOCTOR"
    else:
        hemator = "NORMAL"

if gender == f:
    if 3.5 >= rbcs or rbcs >= 5.5:
        rbcsr = "VISIT THE DOCTOR"
    else:
        rbcsr = "NORMAL"

    if 12.0 >= hemo or hemo >= 16.0:
        hemor = "VISIT THE DOCTOR"
    else:
        hemor = "NORMAL"

    if 36 >= hemato or hemato >= 46:
        hemator = "VISIT THE DOCTOR"
    else:
        hemator = "NORMAL"

print("Red blood cells: " + rbcsr)
print("White blood cells: " + wbcsr)
print("Platelets: " + plar)
print("Hemoglobin: " + hemor)
print("Hematocrit: " + hemator)
