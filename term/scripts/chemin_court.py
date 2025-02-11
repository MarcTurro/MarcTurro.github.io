def recherche_chemin(graphe, depart, arrivee):   
    parents = {depart: None}
    file = [depart]
    while file != []:
        sommet = ...
        if sommet == arrivee:
            ... 
        for voisin in graphe[sommet]:
            if ... not in ...:
                file.append(...) 
                parents[...] = ...
    return []


def remonte_chemin(depart, arrivee, parents):
    sommet = arrivee
    chemin = [arrivee]
    while sommet != depart:
        sommet = parents[...]
        chemin = ... + ...
    return chemin

# Test
mon_graphe = {"A":["B", "C"], "B":["A", "D", "E"], "C":["A", "D"],
"D":["B", "C", "E"], "E":["B", "D", "F", "G"], "F":["E", "G"], "G":["E", "F", "H"],
"H":["G"]}

assert recherche_chemin(mon_graphe, "A", "G") == ["A", "B", "E", "G"]
