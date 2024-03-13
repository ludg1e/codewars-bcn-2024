uinp = input("")

w = uinp.split()
print(w)

for word in w:
    num = word.find("42")
    print(num)
res = w.count("42")
print(res)
