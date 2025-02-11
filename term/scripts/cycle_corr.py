def existe_cycle(graphe, depart):
    predecesseurs = {depart : None}
    pile = [depart]
    while len(pile) != 0:
        sommet = pile.pop()
        for voisin in graphe[sommet]:
            if (voisin in predecesseurs) and (voisin != predecesseurs[sommet]):
                return True
            elif voisin not in predecesseurs:
                predecesseurs[voisin] = sommet
                pile.append(voisin)
    return False 

# Tests
graphe_5 = {"A":["B", "C"], "B":["A", "E"], "C":["A"], "E":["B"]}
graphe_6 = {"A":["B", "C"], "B":["A"], "C":["A", "D", "E"], "D": ["C", "E"], "E":["C", "D"]}
assert existe_cycle(graphe_5, "A") == False
assert existe_cycle(graphe_6, "A") == True

    