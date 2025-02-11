def recherche_chemin(graphe, depart, arrivee):   
    parents = {depart: None}
    file = [depart]
    while file != []:
        sommet = file.pop(0)
        if sommet == arrivee:
            return remonte_chemin(depart, arrivee, parents) 
        for voisin in graphe[sommet]:
            if voisin not in parents:
                file.append(voisin) 
                parents[voisin] = sommet
    return []

def remonte_chemin(depart, arrivee, parents):
    sommet = arrivee
    chemin = [arrivee]
    while sommet != depart:
        sommet = parents[sommet]
        chemin = [sommet] + chemin
    return chemin
