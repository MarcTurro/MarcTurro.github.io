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

g = Graphe(['A', 'B', 'C', 'D', 'E'])
g.ajouter_arete('A', 'B')
g.ajouter_arete('A', 'C')
g.ajouter_arete('A', 'D')
g.ajouter_arete('A', 'E')
g.ajouter_arete('B', 'C')
g.ajouter_arete('C', 'D')
g.ajouter_arete('D', 'E')

dictionnaire_graphe = ...
print(...)
