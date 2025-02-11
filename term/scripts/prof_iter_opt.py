def parcours_profondeur_iteratif(graphe, depart):   
    parcours = []
    etat = {sommet: "pas vu" for sommet in graphe}
    pile = [...]
    etat[depart] = "en attente"
    while len(pile) != 0:  # ou pile != []
        sommet = ...
        parcours.append(...)
        etat[sommet] = "parcouru"
        voisins = ...
        for voisin in ...:
            if etat[voisin] == "pas vu":  
                pile.append(...)
                etat[voisin]= ...
    return parcours

# Tests
assert parcours_profondeur_iteratif({"A": ["B", "D", "E"],"B": ["A", "C"], "C": ["B", "D"],
"D": ["A", "C", "E"], "E": ["A", "D", "F", "G"], "F": ["E", "G"], "G": ["E", "F", "H"], 
"H": ["G"]}, "A") == ['A', 'E', 'G', 'H', 'F', 'D', 'C', 'B']


