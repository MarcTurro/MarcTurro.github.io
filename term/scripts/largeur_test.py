# Test
assert parcours_en_largeur({"A": ["B", "D", "E"],"B": ["A", "C"], "C": ["B", "D"],
"D": ["A", "C", "E"], "E": ["A", "D", "F", "G"], "F": ["E", "G"], "G": ["E", "F", "H"], 
"H": ["G"]},"A") == ['A', 'B', 'D', 'E', 'C', 'F', 'G', 'H']

# Autres tests
graphe = {"A":("B","D","E"),"B":("A","C"),"C":("B","D"),"D":("A","C","E"),
"E":("A","D","F","G"),"F":("E","G"),"G":("E","F","H"),"H":("G")}
assert parcours_en_largeur(graphe, "B") == ['B', 'A', 'C', 'D', 'E', 'F', 'G', 'H']
assert parcours_en_largeur(graphe, "C") == ['C', 'B', 'D', 'A', 'E', 'F', 'G', 'H']
assert parcours_en_largeur(graphe, "D") == ['D', 'A', 'C', 'E', 'B', 'F', 'G', 'H']
assert parcours_en_largeur(graphe, "E") == ['E', 'A', 'D', 'F', 'G', 'B', 'C', 'H']
assert parcours_en_largeur(graphe, "F") == ['F', 'E', 'G', 'A', 'D', 'H', 'B', 'C']
assert parcours_en_largeur(graphe, "G") == ['G', 'E', 'F', 'H', 'A', 'D', 'B', 'C']
assert parcours_en_largeur(graphe, "H") == ['H', 'G', 'E', 'F', 'A', 'D', 'B', 'C']

