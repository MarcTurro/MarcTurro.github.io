# --- PYODIDE:code --- #

def profondeur_opt(graphe, depart, vu = None, parcours = None):
    if vu is None:
        vu = {sommet : False for sommet in graphe}
    if parcours  is None:
         parcours = []
    vu[depart] = True
    parcours.append(...)
    for voisin in graphe[depart]:
        if ...:
            ...
    return vu, parcours


# --- PYODIDE:corr --- #

def profondeur_opt(graphe, depart, vu = None, parcours = None):
    if vu is None:
        vu = {sommet : False for sommet in graphe}
    if parcours  is None:
         parcours = []
    vu[depart] = True
    parcours.append(depart)
    for voisin in graphe[depart]:
        if not vu[voisin]:
            profondeur_opt(graphe, voisin, vu, parcours)
    return vu, parcours


# --- PYODIDE:tests --- #

assert profondeur_opt({"A": ["B", "D", "E"],"B": ["A", "C"], "C": ["B", "D"],
"D": ["A", "C", "E"], "E": ["A", "D", "F", "G"], "F": ["E", "G"], "G": ["E", "F", "H"], 
"H": ["G"]}, "A") ==  ({'A': True, 'B': True, 'C': True, 'D': True, 'E': True, 'F': True, 'G': True, 'H': True}, 
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])


# --- PYODIDE:secrets --- #

graphe_6 = {"A":["B", "C"], "B":["A"], "C":["A", "D", "E"], "D": ["C", "E"], "E":["C", "D"]}
assert profondeur_opt(graphe_6, "A") == ({'A': True, 'B': True, 'C': True, 'D': True, 'E': True}, 
['A', 'B', 'C', 'D', 'E'])
