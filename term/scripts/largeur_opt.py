def parcours_largeur_opt(graphe, depart):   
    file = [depart]
    parcours = []
    etat = {sommet: "pas vu" for sommet in graphe}
    etat[depart] = "en attente"
    while file != []:
        sommet = file.pop(0)
        parcours.append(sommet) 
        etat[sommet] = ...
        for voisin in graphe[sommet]:
            if etat[voisin] == ...:
                ...
                ...
    return parcours

# Test
assert parcours_largeur_opt({"A": ["B", "D", "E"],"B": ["A", "C"], "C": ["B", "D"],
"D": ["A", "C", "E"], "E": ["A", "D", "F", "G"], "F": ["E", "G"], "G": ["E", "F", "H"], 
"H": ["G"]},"A") == ['A', 'B', 'D', 'E', 'C', 'F', 'G', 'H']
