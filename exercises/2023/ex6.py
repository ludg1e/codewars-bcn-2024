# Inp is of single player
free_thr = abs(int(input("Free throws (1p): ")))
field_goal2 = abs(int(input("Field goals (2p): ")))
field_goal3 = abs(int(input("Field goals (3p): ")))
total_shots = abs(int(input("Total of shots performed during the match: ")))

totalp = free_thr + (field_goal2 * 2) + (field_goal3 * 3)
efp = int(((free_thr + field_goal2 + field_goal3) / total_shots) * 100)

print(str(totalp) + " " + str(efp) + "%")
