def cycle_bfs(graphe, depart):
    distances = {depart : 0}
    file = [depart]
    while file != []:
        sommet = ...
        for voisin in ...:
            if voisin not in distances:
                distances[voisin] = ...
                file.append(voisin)
            elif distances[voisin] >= distances[sommet]:
                return ...
    return ...

# Tests
graphe_5 = {"A":["B", "C"], "B":["A", "E"], "C":["A"], "E":["B"]}
graphe_6 = {"A":["B", "C"], "B":["A"], "C":["A", "D", "E"], "D": ["C", "E"], "E":["C", "D"]}
assert cycle_bfs(graphe_5, "A") == False
assert cycle_bfs(graphe_6, "A") == True
