import networkx as nx

class Aff_alternatives:
    def __init__(self):
        self.name = 'aff-alternatives' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('aff')
        #adding edges
        G.add_edge('start', 'aff')
        G.add_edge('aff', 'aff')
        G.add_edge('aff', 'accept')
        return G