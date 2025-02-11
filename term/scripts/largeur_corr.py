def parcours_en_largeur(graphe, depart):   
    file = [depart]
    parcours = []
    while len(file) != 0:
        sommet = file.pop(0)
        parcours.append(sommet)
        for voisin in graphe[sommet]:
            if not(voisin in parcours) and not(voisin in file):
                file.append(voisin)     
    return parcours

