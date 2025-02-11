# --- PYODIDE:env --- #
import matplotlib.pyplot as plt       # Indispensable (provoque la déclaration de PyodidePlot)
import networkx as nx
figure_2 = PyodidePlot('cible_2')  # Disponible après l'import de matplotlib
figure_2.target()

def cree_graphe_non_oriente_nx(dictionnaire: dict) -> nx.Graph:
    """
    Cette fonction premet de transformer une représentation en dictionnaire en
    une représentation «complexe» d'un objet graphe orienté.

    - Précondition : l'entrée est un dictionnaire
    - Postcondition : la sortie est un graphe orienté (Graph) de Networkx
    """
    Gnx = nx.Graph() 
    for sommets in dictionnaire.keys():
        Gnx.add_node(sommets) # Creation des sommets
    for sommet in dictionnaire.keys():
        for sommets_adjacents in dictionnaire[sommet]:
            Gnx.add_edge(sommet, sommets_adjacents) # Creation des arcs
    return Gnx

# --- PYODIDE:code --- #
# import matplotlib.pyplot as plt : déjà importé dans du code caché
# import networkx as nx : déjà importé dans du code caché

plt.cla()  # Pour effacer les figures précédentes
dico = ...
G = cree_graphe_non_oriente_nx(dico)
# nx.draw_circular(G, with_labels=True)
nx.draw(G,with_labels = True) # Pour une representation classique
plt.show()