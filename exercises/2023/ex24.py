coef = input("Dividend: ")
cc = input("Divisor: ")

nuinp = coef.split()
print(nuinp)

inputs = []
for inte in nuinp:
    num = int(inte)
    inputs.append(num)

print(inputs)


output = f"""
hELLO,
{inputs}

    | {rt1} {rt2} {rt3} {rt4}
{cc}|    {rb1 {rb2}} {rb3}
----------------------------------
    | {rbb1} {rbb2} {rbb3} {rbb4} 
"""

print(output)
