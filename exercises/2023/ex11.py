res = []

print("R3-AD can't distinguish currently between uppercase and lowercase letters")

known = input("Type the letters R3-AD knows currently: ")
knownls = list(known)

while True:
    try:
        nwords = abs(int(input("Type the number of words in the book: ")))
        break
    except ValueError:
        print("Please type a number")

# multiline inp
words = []

print(f"Type the words in the book ({nwords}):")
while len(words) < nwords:
    word = input()
    words.append(word)

# print(words)
# print(knownls)
# print(len(knownls))

knownls2 = [l for l in knownls if l.isalpha()]
letters = []
# print(knownls2)

for lett in knownls2:
    if lett.isupper():
        letti = lett.lower()
        letters.append(letti)
    else:
        letters.append(lett)
letters = list(dict.fromkeys(letters))
# print(letters)

defword = []
for word in words:
    wordi = list(word)
    # print(wordi)
    wordils = []
    for w in wordi:
        if w.isupper():
            wi = w.lower()
            wordils.append(wi)
        else:
            wordils.append(w)
    defword.append("".join(wordils))
# print(defword)


for word in defword:
    """
    Funció all() returns True si tots items in iterable (llista e.g) concorden/match amb condició, llavors False

    La condició és una list expression; pseudocodi: si algun(lletra a llistra_lletres
    per lletra a paraula)
    """
    # print(word)
    if all(lett in letters for lett in word):
        res.append("Yes")
    else:
        res.append("No")

print("\n".join(res))
