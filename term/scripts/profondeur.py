def parcours_en_profondeur(graphe, depart):   
    pile = ...
    parcours = []
    ...

    return parcours

#Tests
assert parcours_en_profondeur({"A": ["B", "D", "E"],"B": ["A", "C"], "C": ["B", "D"],
"D": ["A", "C", "E"], "E": ["A", "D", "F", "G"], "F": ["E", "G"], "G": ["E", "F", "H"], 
"H": ["G"]},"A") == ['A', 'E', 'G', 'H', 'F', 'D', 'C', 'B']


