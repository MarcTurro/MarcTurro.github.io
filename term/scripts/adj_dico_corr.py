def conversion_dico(m):
    g = {}
    for i in range(len(m)):
        g[i] = []
        for j in range(len(m[i])):
            if m[i][j] == 1:
                g[i].append(j)
    return g
    