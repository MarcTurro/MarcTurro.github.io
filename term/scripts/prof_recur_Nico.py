def parcours_profondeur_rec_N(graphe, sommet, vus = None):
    if vus is None:
        vus = {s: False for s in graphe}
    parcours = [sommet]
    vus[sommet] = True
    for voisin in graphe[sommet]:
        if not vus[voisin]:
            parcours += parcours_profondeur_rec_N(graphe, voisin, vus)
    return parcours

# Tests
print(parcours_profondeur_rec_N({"A": ["B", "D", "E"],"B": ["A", "C"], "C": ["B", "D"],
"D": ["A", "C", "E"], "E": ["A", "D", "F", "G"], "F": ["E", "G"], "G": ["E", "F", "H"], 
"H": ["G"]}, "A"))
