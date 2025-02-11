def parcours_profondeur(graphe, depart, vus = None):
    if vus  is None:
        vus = []
    vus.append(depart)
    for voisin in graphe[depart]:
        ...
    return vus

#Tests
assert parcours_profondeur({"A": ["B", "D", "E"],"B": ["A", "C"], "C": ["B", "D"],
"D": ["A", "C", "E"], "E": ["A", "D", "F", "G"], "F": ["E", "G"], "G": ["E", "F", "H"], 
"H": ["G"]}, "A") == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
