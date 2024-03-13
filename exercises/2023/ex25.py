# the sheldon prime

while True:
    try:
        uinp = abs(int(input("Type the number: ")))
        break
    except ValueError:
        print("Please type a number")

if uinp == 73:
    print("Sheldon prime")
elif uinp == 37:
    print("Sheldon prime")
elif uinp == 769:
    print("Relative")
elif uinp == 967:
    print("Relative")
elif uinp == 1409:
    print("Close friend")
elif uinp == 9041:
    print("Close friend")
elif uinp == 17:
    print("Friend")
elif uinp == 71:
    print("Friend")
else:
    print("Not related")
