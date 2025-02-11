def parcours_en_profondeur(graphe, depart):   
    pile = [depart]
    parcours = []
    while len(pile) != 0:
        sommet = pile.pop()
        parcours.append(sommet)
        voisins = graphe[sommet]
        for voisin in voisins:
            if not(voisin in parcours) and not(voisin in pile):
                pile.append(voisin)
    return parcours

