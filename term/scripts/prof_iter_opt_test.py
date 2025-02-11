# Tests
assert parcours_profondeur_iteratif({"A": ["B", "D", "E"],"B": ["A", "C"], "C": ["B", "D"],
"D": ["A", "C", "E"], "E": ["A", "D", "F", "G"], "F": ["E", "G"], "G": ["E", "F", "H"], 
"H": ["G"]}, "A") == ['A', 'E', 'G', 'H', 'F', 'D', 'C', 'B']

# Autres tests
graphe_7 = {"A":["B", "C"],"B":["A"],"C":["A", "D", "F"],
"D":["C","E"],"E":["D", "F"],"F":["C", "E"]}
assert parcours_profondeur_iteratif(graphe_7, "A") == ['A', 'C', 'F', 'E', 'D', 'B']
