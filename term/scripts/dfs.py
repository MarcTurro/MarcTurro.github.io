def parcours_DFS(...):
    ...


# Test
mon_graphe = {"A":["B", "C"], "B":["A", "D", "E"], "C":["A", "D"],
"D":["B", "C", "E"], "E":["B", "D", "F", "G"], "F":["E", "G"], "G":["E", "F", "H"],
"H":["G"]}
print(parcours_DFS(mon_graphe, "A"))

