import networkx as nx

class Collab_alternatives:
    def __init__(self):
        self.name = 'collab-alternatives' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('collab')
        #adding edges
        G.add_edge('start', 'collab')
        G.add_edge('collab', 'accept')
        return G