# fire bad earth ice
# ice bad with fire erath
# earth bad with ice fire

eff = {
    "dragon": 7,
    "demon": 3,
    "golem": 2,
    "troll": 2,
}

neu = {
    "dragon": 9,
    "demon": 3,
    "golem": 2,
    "troll": 2,
}

inf = {
    "dragon": 7,
    "demon": 3,
    "golem": 2,
    "troll": 2,
}

number_monsters = abs(int(input("")))
lines = []
while True:
    line = input()
    if line == "#":
        break
    else:
        lines.append(line)
