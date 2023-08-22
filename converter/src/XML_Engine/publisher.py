import networkx as nx

class Publisher:
    def __init__(self):
        self.name = 'publisher' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('publisher-name')
        #adding edges
        G.add_edge('start', 'publisher-name')
        G.add_edge('publisher-name', 'accept')
        return G