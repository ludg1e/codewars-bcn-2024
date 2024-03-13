phr = input("Input: ")

lp = list(phr)

for l in lp:
    if l.isalpha():
        if l.isupper():
            print(l)
