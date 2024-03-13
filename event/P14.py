inp1 = int(input(""))

if inp1 == 1:
    print(
        """
  H
  |
H-C-H
  |
  H          
"""
    )
else:
    var1 = """
  H
  |
H-C
  |
  H
"""
    var2 = """
    H
    |
    C
    |
    H
    """

    var3 = """
    H
    |
    C-H
    |
    H
    """

    # print(var1 + (var2 * (inp1 - 2)) + var3)
    res = var2 * (inp1 - 2)
    llista = []
    llista.append(var1)
    llista.append(res)
    llista.append(var3)
    print(
        f"""
{var1}{res}{var3}
"""
    )
    print("".join(llista))
