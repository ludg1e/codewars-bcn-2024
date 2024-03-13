# formula kk

# x = x0+v0*cos(a) * t
# y = y0+v0*sin(a) * t - 0,5 * g * t2

# diam = 42.7mm

# mind = td - 3 + (0.0427/2)
# maxd = td +3 - (0.0427/2)

# etc...

import math

while True:
    try:
        td = abs(float(input("Target distance (m): ")))
        break
    except ValueError:
        print("Please type a valid number")

while True:
    try:
        alpha = abs(float(input("Target angle (degrees): ")))
        break
    except ValueError:
        print("Please type a valid number")

g = 9.8

alpharad = math.radians(alpha)

mind = td - 3 + (0.0427 / 2)
maxd = td + 3 - (0.0427 / 2)

mint = math.sqrt((2 * mind * math.sin(alpharad)) / (g * math.cos(alpharad)))
maxt = math.sqrt((2 * maxd * math.sin(alpharad)) / (g * math.cos(alpharad)))

minv = mind / (math.cos(alpharad) * mint)
maxv = maxd / (math.cos(alpharad) * maxt)

print("The maximum speed is: " + str(round(maxv, 2)) + " m/s.")
print("The minimum speed is: " + str(round(minv, 2)) + " m/s.")
