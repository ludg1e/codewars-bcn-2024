# 1mmHg = 133,322 Pa
# convert hPa to mmHg

uinp = abs(float(input("")))

res = (uinp * 100) / 133.322

print(round(res, 2))
