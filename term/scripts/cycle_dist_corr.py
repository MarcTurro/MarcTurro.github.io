def cycle_bfs(graphe, depart):
    distances = {depart : 0}
    file = [depart]
    while file != []:
        sommet = file.pop(0)
        for voisin in graphe[sommet]:
            if voisin not in distances:
                distances[voisin] = distances[sommet] + 1
                file.append(voisin)
            elif distances[voisin] >= distances[sommet]:
                return True
    return False

