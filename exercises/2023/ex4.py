# Output Oh Yeah phrase but with the vowels repeated n times

n = abs(int(input("Number of repetitions: ")))

o = "O" * n
e = "E" * n
a = "A" * n

res = o + "H! " + "Y" + e + a + "H!"
print(res)
