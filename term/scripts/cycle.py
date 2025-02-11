def existe_cycle(graphe, depart):
    predecesseurs = {depart : None}
    pile = [...]
    while len(pile) != 0:
        sommet = ...
        for voisin in graphe[sommet]:
            if (voisin in predecesseurs) and (...):
                return ...
            elif ...:
                ...
                ...
    return ...

# Tests
graphe_5 = {"A":["B", "C"], "B":["A", "E"], "C":["A"], "E":["B"]}
graphe_6 = {"A":["B", "C"], "B":["A"], "C":["A", "D", "E"], "D": ["C", "E"], "E":["C", "D"]}
assert existe_cycle(graphe_5, "A") == False
assert existe_cycle(graphe_6, "A") == True

