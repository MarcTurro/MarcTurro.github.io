# --- PYODIDE:env --- #
import matplotlib.pyplot as plt       # Indispensable (provoque la déclaration de PyodidePlot)
import networkx as nx
figure_3 = PyodidePlot('cible_3')  # Disponible après l'import de matplotlib
figure_3.target()

class Graphe:

    def __init__ (self, sommets):
        self.sommets = sommets
        self.adjacents = {sommet: [] for sommet in self.sommets} # création par compréhension
    
    def ajouter_arete(self, x, y):
        if y not in self.adjacents[x]:
            self.adjacents[x].append(y)
        if x not in self.adjacents[y]:
            self.adjacents[y].append(x)
    
    def get_sommets(self):
        return self.sommets
    
    def get_voisins(self, x):
        return self.adjacents[x]
        
    def get_dictionnaire(self):
        return self.adjacents

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

adjacences = g.get_dictionnaire()
print(adjacences)
plt.cla()
graphe_1 = cree_graphe_non_oriente_nx(adjacences)
nx.draw_circular(graphe_1, with_labels = True)
plt.show()