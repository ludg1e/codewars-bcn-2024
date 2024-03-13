# Convert numb to Excel's base-26, and reverse

# From AA to 27 (e.g)
def from_ex(x):
    print("fdsfs")


# From 27 to AA (e.g)
def to_ex(x):
    print("rgeskgjrewklg")


while True:
    inp = input("Type a number or a letter: ")

    if inp.isalnum():
        if inp.isnumeric():
            print("Input: " + inp)
            # to_ex()
            break
        else:
            print("Input: " + inp)
            # from_ex()
        break
    else:
        print("Please type a positive number or a letter")
