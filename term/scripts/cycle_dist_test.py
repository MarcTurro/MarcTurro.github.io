# Tests
graphe_5 = {"A":["B", "C"], "B":["A", "E"], "C":["A"], "E":["B"]}
graphe_6 = {"A":["B", "C"], "B":["A"], "C":["A", "D", "E"], "D": ["C", "E"], "E":["C", "D"]}
assert cycle_bfs(graphe_5, "A") == False
assert cycle_bfs(graphe_6, "A") == True

# Autres tests
graphe_1 = {"A":["B", "C"], "B":["A", "D", "E"], "C":["A", "D"],
"D":["B", "C", "E"], "E":["B", "D", "F", "G"], "F":["E", "G"], "G":["E", "F", "H"],
"H":["G"]}
graphe_2 =  {"A":["B", "C"], "B":["A", "E"], "C":["A"],
"E":["B", "F"], "F":["E"]}
graphe_3 =  {"A":["B"], "B":["A", "C"], "C":["B"]}
graphe_4 = {"A":["B", "D", "E"],"B":["A", "C"],"C":["B", "D"],
"D":["A","C","E"],"E":["A", "D", "F", "G"],"F":["E", "G"],"G":["E", "F", "H"],"H":["G"]}
graphe_7 = {"A":["B", "C"],"B":["A"],"C":["A", "D", "F"],
"D":["C","E"],"E":["D", "F"],"F":["C", "E"]}
assert cycle_bfs(graphe_1, "A") == True
assert cycle_bfs(graphe_2, "A") == False
assert cycle_bfs(graphe_3, "A") == False
assert cycle_bfs(graphe_4, "A") == True
assert cycle_bfs(graphe_7, "A") == True
