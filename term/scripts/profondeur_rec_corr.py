def parcours_profondeur(graphe, depart, vus = None):
    if vus  is None:
        vus = []
    vus.append(depart)
    for voisin in graphe[depart]:
        if voisin not in vus:
            parcours_profondeur(graphe, voisin, vus)
    return vus
