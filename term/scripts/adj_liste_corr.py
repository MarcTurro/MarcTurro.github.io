def conversion_liste(m):
    liste = []
    for i in range(len(m)):
        liste.append([])
        for j in range(len(m[i])):
            if m[i][j] == 1:
                liste[i].append(j)
    return liste
