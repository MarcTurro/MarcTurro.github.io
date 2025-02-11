def essai_recherche_cycle(graphe, depart):   
    # parcours = []  # On ne cherche plus à mémoriser le parcours
    etat = {sommet: "pas vu" for sommet in graphe}
    pile = [depart]
    etat[depart] = "en attente"
    while len(pile) != 0:
        sommet = pile.pop()
        # parcours.append(sommet)  # On ne cherche plus à mémoriser le parcours
        etat[sommet] = "parcouru"
        voisins = graphe[sommet]
        for voisin in voisins:
            if etat[voisin] == "parcouru":  # On détecte un cycle
                return True
            if etat[voisin] == "pas vu":  
                pile.append(voisin)
                etat[voisin]= "en attente"
    return False

# Tests
graphe_1 =  {"A":["B"], "B":["A"]}
graphe_2 = {"A": ["B"], "B": []}
assert essai_recherche_cycle(graphe_1, "A") == False
assert essai_recherche_cycle(graphe_2, "A") == False
