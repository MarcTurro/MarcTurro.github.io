#Tests
assert parcours_profondeur({"A": ["B", "D", "E"],"B": ["A", "C"], "C": ["B", "D"],
"D": ["A", "C", "E"], "E": ["A", "D", "F", "G"], "F": ["E", "G"], "G": ["E", "F", "H"], 
"H": ["G"]}, "A") == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Autres tests
graphe = {"A":("B","D","E"),"B":("A","C"),"C":("B","D"),"D":("A","C","E"),
"E":("A","D","F","G"),"F":("E","G"),"G":("E","F","H"),"H":("G")}
assert parcours_profondeur(graphe, "B") == ['B', 'A', 'D', 'C', 'E', 'F', 'G', 'H']
assert parcours_profondeur(graphe, "C") == ['C', 'B', 'A', 'D', 'E', 'F', 'G', 'H']
assert parcours_profondeur(graphe, "D") == ['D', 'A', 'B', 'C', 'E', 'F', 'G', 'H']
assert parcours_profondeur(graphe, "E") == ['E', 'A', 'B', 'C', 'D', 'F', 'G', 'H']
assert parcours_profondeur(graphe, "F") == ['F', 'E', 'A', 'B', 'C', 'D', 'G', 'H']
assert parcours_profondeur(graphe, "G") == ['G', 'E', 'A', 'B', 'C', 'D', 'F', 'H']
assert parcours_profondeur(graphe, "H") == ['H', 'G', 'E', 'A', 'B', 'C', 'D', 'F']
