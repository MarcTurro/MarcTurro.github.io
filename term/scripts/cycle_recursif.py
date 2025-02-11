def cherche_cycle_rec(graphe, sommet, vus=None):
    if vus is None:
        vus = {sommet: None}
    precedent = vus[sommet]
    for voisin in graphe[sommet]:
        if voisin != precedent:
            if voisin in vus:
                return True
            else:
                vus[voisin] = sommet
                if cherche_cycle_rec(graphe, voisin, vus):
                    return True
    return False

# Tests
graphe_5 = {"A":["B", "C"], "B":["A", "E"], "C":["A"], "E":["B"]}
graphe_6 = {"A":["B", "C"], "B":["A"], "C":["A", "D", "E"], "D": ["C", "E"], "E":["C", "D"]}
assert cherche_cycle_rec(graphe_5, "A") == False
assert cherche_cycle_rec(graphe_6, "A") == True
print("😀")
