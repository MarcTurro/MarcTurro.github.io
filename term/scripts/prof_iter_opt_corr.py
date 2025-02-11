def parcours_profondeur_iteratif(graphe, depart):   
    parcours = []
    etat = {sommet: "pas vu" for sommet in graphe}
    pile = [depart]
    etat[depart] = "en attente"
    while len(pile) != 0:
        sommet = pile.pop()
        parcours.append(sommet)
        etat[sommet] = "parcouru"
        voisins = graphe[sommet]
        for voisin in voisins:
            if etat[voisin] == "pas vu":  
                pile.append(voisin)
                etat[voisin]= "en attente"
    return parcours
