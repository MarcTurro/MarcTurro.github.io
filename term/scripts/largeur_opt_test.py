# Tests
assert parcours_largeur_opt({"A": ["B", "D", "E"],"B": ["A", "C"], "C": ["B", "D"],
"D": ["A", "C", "E"], "E": ["A", "D", "F", "G"], "F": ["E", "G"], "G": ["E", "F", "H"], 
"H": ["G"]},"A") == ['A', 'B', 'D', 'E', 'C', 'F', 'G', 'H']

# Autres tests
g_2 = {1: [2, 3], 2: [1, 3, 4, 5], 3:[1, 2, 4, 5], 4: [2, 3, 5], 5:[2, 3, 4] }
graphe_6 = {"A":["B", "C"], "B":["A"], "C":["A", "D", "E"], "D": ["C", "E"], "E":["C", "D"]}
assert parcours_largeur_opt(g_2, 1) == [1, 2, 3, 4, 5]
assert parcours_largeur_opt(graphe_6, "A") == ['A', 'B', 'C', 'D', 'E']
