# --- PYODIDE:env --- #
import matplotlib.pyplot as plt       # Indispensable (provoque la déclaration de PyodidePlot)
import networkx as nx
figure_5 = PyodidePlot('cible_5')  # Disponible après l'import de matplotlib
figure_5.target()

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
# La fonction cree_graphe_non_oriente_nx est déjà présente dans le code caché

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

# Créer le graphe
g2 = ...

# Ajouter les arêtes
...

# récupérer le dictionnaire liste d'adjacences
dict_2 = ...
print(dict_2)

plt.cla()  # Pour effacer les figures précédentes

# Faire le graphique
graphe_2 = cree_graphe_non_oriente_nx(...)
nx.draw_circular(..., with_labels = True)
plt.show()
