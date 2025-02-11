def parcours_largeur_opt(graphe, depart):   
    file = [depart]
    parcours = []
    etat = {sommet: "pas vu" for sommet in graphe}
    etat[depart] = "en attente"
    while file != []:
        sommet = file.pop(0)
        parcours.append(sommet) 
        etat[sommet] = "vu"
        for voisin in graphe[sommet]:
            if etat[voisin] == "pas vu":
                file.append(voisin) 
                etat[voisin] = "en attente"
    return parcours

