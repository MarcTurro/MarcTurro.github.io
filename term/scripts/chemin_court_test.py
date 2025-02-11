# Tests
mon_graphe = {"A":["B", "C"], "B":["A", "D", "E"], "C":["A", "D"],
"D":["B", "C", "E"], "E":["B", "D", "F", "G"], "F":["E", "G"], "G":["E", "F", "H"],
"H":["G"]}

assert recherche_chemin(mon_graphe, "A", "G") == ["A", "B", "E", "G"]

# Autres tests
assert recherche_chemin(mon_graphe, "H", "C") == ["H", "G", "E", "D", "C"]
assert recherche_chemin(mon_graphe, "H", "M") == []
assert recherche_chemin(mon_graphe, "D", "H") == ["D", "E", "G", "H"]
assert recherche_chemin(mon_graphe, "D", "D") == ["D"]
