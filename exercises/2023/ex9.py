# 4 inp
f = float(input("Actual frequency (Hz): "))
c = float(input("Speed of the sound waves in the medium (m/s): "))
vr = float(input("Velocity of the observer (km/h): ")) * (1000 / 3600)  # convert to m/s
vs = float(input("Velocity of the noisy object (km/h): ")) * (
    1000 / 3600
)  # convert to m/s

# doppler effect formula
fp = f * ((c + vr) / (c + vs))

print(str(round(fp, 2)) + " Hz")
