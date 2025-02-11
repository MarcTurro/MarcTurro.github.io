def parcours_BFS(graphe, depart):
    ...


# Test
mon_graphe = {"A":["B", "C"], "B":["A", "D", "E"], "C":["A", "D"],
"D":["B", "C", "E"], "E":["B", "D", "F", "G"], "F":["E", "G"], "G":["E", "F", "H"],
"H":["G"]}
assert parcours_BFS(mon_graphe, "B") == ...
print("Bravo !")
