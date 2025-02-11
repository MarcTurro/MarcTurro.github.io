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
